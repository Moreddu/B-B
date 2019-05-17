from googleapiclient import discovery
from oauth2client import client
import httplib2
from flask import *
import logging
import os

#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

client_secret_path = r"controllers/client_secret.json"

class GoogleLogin():
    def __init__(self):
        self.flow = client.flow_from_clientsecrets(
            client_secret_path,
            scope='https://www.googleapis.com/auth/userinfo.email',
            redirect_uri='http://fast-lysis-iot-4.appspot.com/authorization')

    def step1(self):
        self.auth_uri = self.flow.step1_get_authorize_url()
        logging.info(self.auth_uri)
        return self.auth_uri

    def step2(self):
        self.auth_code = request.args.get('code')
        self.credentials = self.flow.step2_exchange(self.auth_code)
        session['credentials'] = self.credentials.to_json()

    def userinfo(self):
        self.credentials = client.OAuth2Credentials.from_json(
            session['credentials'])
        self.http_auth = self.credentials.authorize(httplib2.Http())
        self.user_service = discovery.build('oauth2', 'v2', self.http_auth,
                                            cache_discovery=False)
        self.userinfor = self.user_service.userinfo().get().execute()
        return self.userinfor
