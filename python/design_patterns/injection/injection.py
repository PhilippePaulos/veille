from abc import abstractmethod, ABC

from injector import Injector, Module, provider, singleton
from pydantic_settings import BaseSettings


class Configuration(BaseSettings):
    provider: str
    bucket_name: str = ""
    storage_account: str = ""


class Provider(ABC):
    @abstractmethod
    def mount(self):
        pass


class AWSProvider(Provider):
    def __init__(self, config: Configuration) -> None:
        self.bucket_name = config.bucket_name

    def mount(self) -> str:
        return f"aws://{self.bucket_name}"


class AzureProvider(Provider):
    def __init__(self, config: Configuration) -> None:
        self.storage_account = config.storage_account

    def mount(self) -> str:
        return f"azure://{self.storage_account}"


class UnsupportedProviderError(Exception):
    def __init__(self, provider, message="Provider is not supported"):
        self.provider = provider
        self.message = message
        super().__init__(f"{message}: {provider}")


class ProviderFactory:
    @staticmethod
    def create_provider(configuration: Configuration) -> Provider:
        if configuration.provider == "AWS":
            return AWSProvider(configuration)
        elif configuration.provider == "AZURE":
            return AzureProvider(configuration)
        else:
            raise UnsupportedProviderError("Unsupported provider type")


class ProviderModule(Module):
    @singleton
    @provider
    def provide_provider(self, configuration: Configuration) -> Provider:
        return ProviderFactory.create_provider(configuration)


def configure(binder):
    config = Configuration(_env_file=".env")
    binder.bind(Configuration, to=config, scope=singleton)


if __name__ == "__main__":
    injector = Injector([configure, ProviderModule()])
    provider = injector.get(Provider)
    print(provider.mount())
