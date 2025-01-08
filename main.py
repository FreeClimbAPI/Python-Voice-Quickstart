import freeclimb
from flask import Flask, jsonify
import os

app = Flask(__name__)

# Specify this route with 'VOICE URL' in App Config
@app.route('/incomingCall', methods=['POST', 'GET'])
def post_incoming_call():
    message = "Hello, World!"
    say = freeclimb.Say(text=message)
    script = freeclimb.PerclScript(commands=[say])
    return script.to_json()

# Specify this route with 'STATUS CALLBACK URL' in App Config
@app.route('/status', methods=['POST'])
def status():
    return jsonify({'success':True}), 200, {'ContentType':'application/json'} 

def quickstart_tutorial():
    print("\nWelcome to FreeClimb!\n")
    print("Your web server is listening at: http://127.0.0.1:3000")
    print("View an example perCl JSON response to FreeClimb at: http://127.0.0.1:3000/incomingCall\n")
    print("Your NEXT STEP is to use NGROK to proxy HTTP Traffic to this local web server.")
    print("\t1. In NGROK, configure the dynamic url to proxy to http://127.0.0.1:3000")
    print("\t2. In the Dashboard or API, set your FreeClimb Application Voice Url to the dynamic endpoint NGROK generated.\n")

# Liveness probe endpoint
@app.route('/live', methods=['GET'])
def live():
    return jsonify({'status': 'live'}), 200, {'ContentType':'application/json'}

# Readiness probe endpoint
@app.route('/ready', methods=['GET'])
def ready():
    return jsonify({'status': 'ready'}), 200,  {'ContentType':'application/json'}

if __name__ == '__main__':
    quickstart_tutorial()
    app.run(host='0.0.0.0', port=3000)
