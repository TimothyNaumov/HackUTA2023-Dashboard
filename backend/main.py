from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)


@app.route("/record", methods=["GET", "POST"])
def record():
    """Returns TwiML which prompts the caller to record a message"""
    # Start our TwiML response
    response = VoiceResponse()

    # Use <Say> to give the caller some instructions
    response.say("Hello. Please leave a message after the beep.")

    # Use <Record> to record the caller's message
    response.record()

    # End the call with <Hangup>
    response.hangup()

    return str(response)


@app.route("/voice", methods=["GET", "POST"])
def voice():
    """Respond to incoming phone calls with a 'Hello world' message"""
    # Start our TwiML response
    resp = VoiceResponse()

    # Read a message aloud to the caller
    resp.say("Hello world!")

    return str(resp)


if __name__ == "__main__":
    app.run()
