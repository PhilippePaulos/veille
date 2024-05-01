from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    provider: str
    bucket_name: str = ""
    storage_account: str = ""
