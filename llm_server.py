import sys
from flask import Flask, request
from generate_reply import generate_reply

port = 5050
if len(sys.argv) > 1:
    port = sys.argv[1]

app = Flask(__name__)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/', methods=['GET'])
def get():
    prompt = request.args.get('p')
    reply = generate_reply(prompt)
    return reply

if __name__ == '__main__':
    app.run(debug=False, host='::', port=port)
