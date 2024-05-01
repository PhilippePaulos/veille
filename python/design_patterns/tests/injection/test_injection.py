import unittest
from unittest.mock import patch
from injector import Injector, singleton

from injection.app import ProviderModule, Configuration, Provider


def configure_for_aws(binder):
    configuration = Configuration(provider="AWS", bucket_name="test-bucket")
    binder.bind(Configuration, to=configuration, scope=singleton)


def configure_for_azure(binder):
    configuration = Configuration(provider="AZURE", storage_account="test-storage")
    binder.bind(Configuration, to=configuration, scope=singleton)


class TestProviderMount(unittest.TestCase):
    @patch("injection.AWSProvider")
    @patch("injection.AzureProvider")
    def test_aws_provider_mount(self, mock_azure, mock_aws):
        mock_aws.return_value.mount.return_value = "aws://mocked-bucket"
        mock_azure.return_value.mount.return_value = "azure://mocked-storage"

        injector = Injector([configure_for_aws, ProviderModule()])
        aws_provider = injector.get(Provider)

        self.assertEqual(aws_provider.mount(), "aws://mocked-bucket")

        injector = Injector([configure_for_azure, ProviderModule()])
        azure_provider = injector.get(Provider)

        self.assertEqual(azure_provider.mount(), "azure://mocked-storage")
