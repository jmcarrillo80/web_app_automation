from modules.KeyVault import getSmartCompletionsCredentials, getSharepointCredentials

username, password = getSmartCompletionsCredentials()
print(username)
print(password)
account, password = getSharepointCredentials()
print(account)
print(password)