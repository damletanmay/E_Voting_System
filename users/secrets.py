from E_Voting_System import settings

account_sid = settings.ACCOUNT_SID
auth_token = settings.AUTH_TOKEN
from_mobile= settings.MOBILE

def getSid():
    return account_sid

def getToken():
    return auth_token

def getFromMobile():
    return from_mobile
