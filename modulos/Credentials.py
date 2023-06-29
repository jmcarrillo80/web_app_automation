from os import environ as env
from dotenv import load_dotenv
from cryptography.fernet import Fernet


def getCredentials():
    with open(r'C:\Temp\filekey.key', 'rb') as filekey:
        key = filekey.read()
    fernet = Fernet(key)
    with open('smartCompletions.env', 'rb') as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    with open('smartCompletions.env', 'wb') as dec_file:
        dec_file.write(decrypted)
    load_dotenv('smartCompletions.env')
    username = env['user_name']
    password = env['password']
    with open('smartCompletions.env', 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open('smartCompletions.env', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)        
    return username, password
    
