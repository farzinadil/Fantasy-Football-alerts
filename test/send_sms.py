from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

# Your Account SID from twilio.com/console
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
# Your Auth Token from twilio.com/console
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
# Your cell phone number
phone_number = os.getenv("PHONE_NUMBER")
# Your Tweilio phone number
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")


client = Client(account_sid, auth_token)


message = client.messages.create(
    to=phone_number,
    from_=twilio_phone_number,
    body="Hello from Python!")

print(message.sid)
