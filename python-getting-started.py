import freeclimb
from flask import Flask, request
import json

app = Flask(__name__)

# Specify this route with 'Voice URL' in App Config
@app.route('/incomingCall', methods=['POST'])
def incomingCall():
    if request.method == 'POST':

        message = "Hello, World!"
        say = freeclimb.Say(text=message)
        script = freeclimb.PerclScript(commands=[say])
        return script.to_json()

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
