import math, random
import twilio
from twilio.rest import Client

def generateOTP() : 
	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = "" 
	length = len(string) 
	for i in range(8) : 
		OTP += string[math.floor(random.random() * length)] 

	return OTP 

'''
Don't run this code, it will cut 1$ from twilio account.
There is another way, way2sms.
'''

otp = generateOTP()

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'AC98af503fee4678cfdc8de78003b74065'
auth_token = '778774a46653ae476f6d6d1abfbcda91'
client = Client(account_sid, auth_token)

message = client.messages.create(
         body='OTP: ' + (otp) + '\nIt will work for 30min only',
         from_='+13345390737',
         to='+918469208311'
     )

print(message.sid)
