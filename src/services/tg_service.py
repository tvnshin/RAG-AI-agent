from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from src.services.agent_service import generate_agent_response


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я — ИИ агент, созданный для вывода информации о пользователях. Напиши id пользователя, которого хочешь увидеть.",
    )


async def show_help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Я — ИИ агент, созданный для вывода информации о пользователях. Напиши id пользователя, которого хочешь увидеть."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.message.chat_id
    if "history" not in context.chat_data:
        context.chat_data["history"] = {"messages": []}
    print(f"Обновленная история для чата {chat_id}: {context.chat_data['history']}")
    try:
        res = await generate_agent_response(message=user_text, messages=context.chat_data["history"]["messages"])
    except:
        await update.message.reply_text("Что-то пошло не так.")
        return
    context.chat_data["history"]["messages"].append(
        {"sender_type": "user", "text": user_text}
    )
    context.chat_data["history"]["messages"].append(
        {"sender_type": "ai", "text": res.output}
    )
    await update.message.reply_text(res.output)