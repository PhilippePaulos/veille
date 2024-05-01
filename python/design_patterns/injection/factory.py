from config import Configuration
from providers import Provider, AWSProvider, AzureProvider


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
