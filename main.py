import freeclimb
from flask import Flask
import os
from dotenv import load_dotenv


load_dotenv()
account_id = os.environ.get("ACCOUNT_ID")
api_key = os.environ.get("API_KEY")


app = Flask(__name__)

configuration = freeclimb.Configuration(
    username=account_id,
    password=api_key
)


# Voice URL
@app.route('/incomingCall', methods=['POST', 'GET'])
def post_incoming_call():

    message = "Hello, World!"
    say = freeclimb.Say(text=message)
    script = freeclimb.PerclScript(commands=[say])
    return script.to_json()


def quickstart_tutorial():
    obfuscated_api_key = '*'*(len(api_key) - 4)+api_key[-4:]

    print("\nWelcome to FreeClimb!\n")
    print("Your account id: {0}".format(account_id))
    print("Your api key is: {0}\n".format(obfuscated_api_key))
    print("Your web server is listening at: http://127.0.0.1:3000")
    print("View an example perCl JSON response to FreeClimb at: http://127.0.0.1:3000/incomingCall\n")
    print("Your NEXT STEP is to use NGROK to proxy HTTP Traffic to this local web server.")
    print("\t1. In NGROK, configure the dynamic url to proxy to http://127.0.0.1:3000")
    print("\t2. In the Dashboard or API, set your FreeClimb Application Voice Url to the dynamic endpoint NGROK generated.\n")


if __name__ == '__main__':
    quickstart_tutorial()
    app.run()
