from abc import abstractmethod, ABC

from config import Configuration


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
