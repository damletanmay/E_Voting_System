import math, random
import twilio
from twilio.rest import Client

def generateOTP() :# to generate OTP
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

def sendOTP(mobile,otp,account_sid,auth_token,from_mobile):
	# from twilio docs.
	client = Client(account_sid,auth_token)
	# to create customized message.
	message = client.messages.create(
		body='OTP For E-Voting Login : ' + (otp) + '\nIt will work for 5 min only',
		from_=from_mobile,
		to='+91'+ str(mobile)
	)
