from DBIface import DBIface
from interface import implements,Interface
from DBRecord import DBRecord
import logging


class FileDB(implements(DBIface)):

    def __init__(self, db_name):
        self.__db_name = db_name
        self.__db_handle = None

    def start(self):
        logging.info("Starting FileDB...")

    def stop(self):
        logging.info("Stoppping FileDB...")

    def connect(self):
        try:
            self.__db_handle = open(self.__db_name, "r+")
        except IOError:
            logging.error("Failed to DB: " + self.__db_name)

    def disconnect(self):
        #logging.info("__db_handle type: " + str(type(self.__db_handle)))
        if isinstance(type(self.__db_handle), file):
            self.__db_handle.close()

    def write_data(self, user_data):
        if str == type(user_data):
            record_obj = DBRecord(user_data)
            record_obj.set_no(1)
            record_obj.set_state(1)

            self.__db_handle.write(record_obj)