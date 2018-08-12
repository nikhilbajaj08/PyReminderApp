
class DBRecord:

    def __init__(self, user_data):
        self.__user_data = user_data
        self.__no = 0
        self.__state = 0

    def set_no(self, record_no):
        self.__no = record_no

    def set_state(self, state):
        self.__state = state
