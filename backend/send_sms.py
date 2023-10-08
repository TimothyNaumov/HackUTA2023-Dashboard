# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

VOICE_ASSISTANT_NUMBER = os.environ["VOICE_ASSISTANT_NUMBER"]

user = "Tim"

message = client.messages.create(
    body=f"Hey {user}, my name is Amelia, and I am your personal State Farm AI assistant. I noticed your tires look a little worn. Let's chat about how you can save money by doing some preventative maintenance. Please give me a call at:\n\n {VOICE_ASSISTANT_NUMBER}",
    from_="+18443871906",
    to="+14696056677",
)

print(message.sid)
