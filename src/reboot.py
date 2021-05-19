from SMWinservice import SMWinservice
from requests import get
from base64 import b64encode
from urllib.request import urlopen
from urllib.parse import quote
import time
import pywintypes
import win32api
import sys

tplink = '192.168.0.254'
user = 'admin'
password = 'admin'
url_template = 'http://{}/userRpm/SysRebootRpm.htm?Reboot=Reboot'

class Reboot(SMWinservice):
    _svc_name_ = 'TP-LINK Auto-reboot'
    _svc_display_name_ = 'TP-LINK Auto-reboot'
    _svc_description_ = 'Reboot router/AP when there are not internet connection'

    def __init__(self, args):
        super().__init__(args)
        self.isRunning = False

    def start(self):
        self.isRunning = False

    def stop(self):
        self.isRunning = True

    @staticmethod
    def checkConnection():
        try:
            urlopen('https://www.google.com', timeout=10)
            return True
        except:
            return False

    def main(self):
        while self.isRunning:
            if not Rebooter.internet():
                auth_bytes = bytes(user + ':' + password, 'utf-8')
                auth_b64_bytes = b64encode(auth_bytes)
                auth_b64_str = str(auth_b64_bytes, 'utf-8')
                auth_str = quote('Basic {}'.format(auth_b64_str))
                auth = {
                    'Referer': 'http://' + tplink + '/',
                    'Authorization': auth_str,
                }
                reboot_url = url_template.format(tplink)
                get(reboot_url, headers=auth)
                time.sleep(120)
            time.sleep(60)


if __name__ == '__main__':
    Rebooter.parse_command_line()