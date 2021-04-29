import math, random
import twilio
from twilio.rest import Client
from decouple import config

def generateOTP() :# to generate OTP
	string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	OTP = ""
	length = len(string)
	for i in range(8) :
		OTP += string[math.floor(random.random() * length)]

	return OTP


def sendOTP(mobile,otp):
	# from twilio docs.
	account_sid = config('ACCOUNT_SID')
	auth_token = config('AUTH_TOKEN')
	from_mobile = config('MOBILE')

	client = Client(account_sid,auth_token)
	# to create customized message.
	message = client.messages.create(
		body='OTP For E-Voting Login : ' + (otp) + '\nIt will work for 5 min only',
		from_= from_mobile,
		to='+91'+ str(mobile)
	)
