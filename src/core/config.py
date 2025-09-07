from pydantic_settings import BaseSettings, SettingsConfigDict

class AISettings(BaseSettings):
    api_key: str
    model_name: str

    model_config = SettingsConfigDict(env_prefix="AI_", env_file=".env", extra="ignore")

class TGSettings(BaseSettings):
    token: str

    model_config = SettingsConfigDict(env_prefix="TG_", env_file=".env", extra="ignore")

ai_settings = AISettings()
tg_settings = TGSettings()