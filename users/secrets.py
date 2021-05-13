import environ

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

account_sid = env('ACCOUNT_SID')
auth_token = env('AUTH_TOKEN')
from_mobile= env('MOBILE')

def getSid():
    return account_sid

def getToken():
    return auth_token

def getFromMobile():
    return from_mobile
