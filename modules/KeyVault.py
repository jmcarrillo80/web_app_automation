from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient


credential = DefaultAzureCredential()
secret_client = SecretClient(vault_url="https://kv-kpd-scus-epl-dev.vault.azure.net/", credential=credential)

def getSmartCompletionsCredentials():
    username_secret = secret_client.get_secret("SmartCompletionsWeb-XOM-UserName")
    password_secret = secret_client.get_secret("SmartCompletionsWeb-XOM-Password")
    return username_secret.value, password_secret.value

def getSharepointCredentials():
    account_secret = secret_client.get_secret("ADServiceAccount-PDW-SVC-UserName")
    password_secret = secret_client.get_secret("ADServiceAccount-PDW-SVC-Password")
    return f'{account_secret.value}@Kiewit.com', password_secret.value