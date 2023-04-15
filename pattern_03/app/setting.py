from typing import Optional

from pydantic import BaseSettings
from pydantic.env_settings import SettingsError


class Settings(BaseSettings):
    """設定管理クラス"""

    # ローカルスタック用 endpoint
    LOCAL_STACK_ENDPOINT: Optional[str]

    AWS_REGION = "ap-northeast-1"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
