from pydantic_ai import Agent, RunContext
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider
from pydantic_ai.messages import ModelRequest, ModelResponse, UserPromptPart, TextPart
from src.core.config import ai_settings
from src.schemas.user import UserOut, UserFuncResponse
from src.core.fake_db import get_user
from typing import Any
import openai

system_prompt_file = 'src/prompts/agent_prompt.txt'
with open(system_prompt_file, 'r', encoding='utf-8') as file:
    system_prompt = file.read()

model = OpenAIModel(
    ai_settings.model_name,
    provider=OpenAIProvider(openai_client=openai.AsyncOpenAI(api_key=ai_settings.api_key))
)
agent = Agent(
    model=model,
    deps_type=dict,
    output_type=str,
    system_prompt=system_prompt,
    retries=1
)


@agent.tool
async def search_user(ctx: RunContext[dict], user_id: int) -> UserFuncResponse:
    """
    Поиск пользователя в базе данных по id.
    """
    try:
        user = await get_user(user_id)
        return UserFuncResponse(
            user_found=True,
            user=UserOut(
                id=user.id,
                name=user.name,
                status=user.status
            )
        )
    except:
        return UserFuncResponse(
            user_found=False,
            user=None
        )


async def generate_agent_response(message: str, messages: list[Any]):
    history = []
    for m in messages:
        if m["sender_type"] == "user":
            history.append(ModelRequest(parts=[UserPromptPart(content=m.get("text"))]))
        elif m["sender_type"] == "ai":
            history.append(ModelResponse(parts=[TextPart(content=m.get("text"))]))
    res = await agent.run(
        user_prompt=message,
        message_history=history,
        deps={}
    )
    return res
