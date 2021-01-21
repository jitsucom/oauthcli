#!/usr/bin/env python3

import argparse
import json
import threading
import time
import logging
import webbrowser
from urllib.parse import urlunsplit, urlencode

import requests
from flask import Flask
from flask import request

client_id = ""
client_secret = ""
port = 5000
scope = 'https://www.googleapis.com/auth/analytics.readonly'

GET_CODE_ENDPOINT = '/oauth'
first_call_executed = False

app = Flask(__name__)


@app.route("/")
def health_check():
    return "ok"


@app.route(GET_CODE_ENDPOINT)
def exchange_for_auth_token():
    response_data = request.args
    if 'error' in response_data:
        return {"message": "Failed to get authorization code from Google", "error": response_data['error']}
    parameters = {
        'client_id': client_id,
        'client_secret': client_secret,
        'code': response_data['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': f'http://localhost:{port}{GET_CODE_ENDPOINT}'
    }
    url = urlunsplit(('https', "oauth2.googleapis.com", '/token', urlencode(parameters), ""))
    resp = requests.post(url)
    print(json.dumps(resp.json(), sort_keys=True, indent=4, separators=(',', ': ')))
    return resp.json()


@app.before_first_request
def send_auth_request():
    global first_call_executed
    if not first_call_executed:
        parameters = {
            'client_id': client_id,
            'redirect_uri': f'http://localhost:{port}{GET_CODE_ENDPOINT}',
            'response_type': 'code',
            'scope': scope,
            'access_type': 'offline',
            'prompt': 'consent'
        }
        path = '/o/oauth2/v2/auth'
        query = urlencode(parameters)
        url = urlunsplit(('https', 'accounts.google.com', path, query, ""))
        first_call_executed = True
        webbrowser.open_new_tab(url)


def start_runner():
    def wait_server_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                url = f'http://localhost:{port}/'
                r = requests.get(url)
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                    send_auth_request()
            except:
                logging.exception("Cannot connect to server")
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=wait_server_loop)
    thread.start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='OAuth tool')
    parser.add_argument("--client_id", help='Google client_id', required=True)
    parser.add_argument("--client_secret", help='Google client_secret', required=True)
    parser.add_argument("--port", help='Port to run application, 5000 by default', required=False, default=5000)
    parser.add_argument("--scope", help='OAuth scope (default is https://www.googleapis.com/auth/analytics.readonly)', required=False, default='https://www.googleapis.com/auth/analytics.readonly')
    
    args = parser.parse_args()
    client_id = args.client_id
    client_secret = args.client_secret
    port = args.port
    start_runner()
    app.run()
