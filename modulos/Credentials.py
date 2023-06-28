from os import environ as env
from dotenv import load_dotenv


def getCredentials():
    load_dotenv(r'C:\Temp\smartCompletions.env')
    username = env['user_name']
    password = env['password']
    return username, password