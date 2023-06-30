from azure.identity import DefaultAzureCredential, InteractiveBrowserCredential
from azure.keyvault.secrets import SecretClient

credential = InteractiveBrowserCredential(
    client_id="07420c3d-c141-4c67-b6f3-f448e5adb67b",
)
# credential = DefaultAzureCredential()

secret_client = SecretClient(vault_url="https://kv-kpd-scus-epl-dev.vault.azure.net/", credential=credential)
secret = secret_client.get_secret("SmartCompletionsWeb-XOM-UserName")

print(secret.name)
print(secret.value)