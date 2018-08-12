import logging
from AppIface import AppIface
from interface import implements
from FileDB import FileDB


class Todo(implements(AppIface)):

    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.db_obj = FileDB("user-db.txt")


    def start(self):
        logging.info("Starting Todo application...")
        """
        -Recover if crashed
        -Start and connect to data base for storing user input
        -Generate UI
        """

    def stop(self):
        self.db_obj.disconnect()
        logging.info("Stopping Todo application...")