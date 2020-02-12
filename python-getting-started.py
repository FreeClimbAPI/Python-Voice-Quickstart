import freeclimb
from flask import Flask, request
import json

app = Flask(__name__)

# Specify this route with 'Voice URL' in App Config
@app.route('/incomingCall', methods=['POST'])
def incomingCall():
    if request.method == 'POST':

        percl = freeclimb.PerCLScript()

        message = "Hello! This is a message sent using FreeClimb's Python SDK."
        percl.append(freeclimb.Say(text=message))
        print(percl)
        return json.dumps(percl)

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
