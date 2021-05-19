from SMWinservice import SMWinservice

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

    
    def checkConnection():
        pass

    def main(self):
        pass

if __name__ == '__main__':
    pass