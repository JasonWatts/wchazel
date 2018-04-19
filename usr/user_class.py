
class user:
    name = ""
    connect = False
    def __init__(self, name, connect, ip):
        self.name = name
        self.connet = connect
        self.ip = ip

    def set_name(self, name):
        self.name = name

    def set_connect(self, connect):
        self.connect = connect

    def set_ip(self, ip):
        self.ip = ip;

    def get_name(self):
        return self.name

    def get_connect(self):
        return self.connect

    def get_ip(self):
        return self.ip
