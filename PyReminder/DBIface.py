from interface import Interface


class DBIface(Interface):

    def start(self):
        pass

    def stop(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass