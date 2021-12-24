from connectdb import ConnectToDb
from datetime import *


class Message:
    def __init__(self, data, user):
        self.__data = data
        now = datetime.now()
        msg_date = now.strftime("%d/%m/%Y %H:%M")
        self.__date = msg_date
        self.__user = user

    def send_to_db(self):
        message = {
            "data": self.__data,
            "date": self.__date,
            "user": self.__user
        }
        ConnectToDb().messages.insert_one(message)
