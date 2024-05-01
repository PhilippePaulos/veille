from injector import Injector, Module, provider, singleton

from config import Configuration
from factory import ProviderFactory
from providers import Provider


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
