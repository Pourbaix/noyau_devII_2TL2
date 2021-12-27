from src.models.connectdb import ConnectToDb
from datetime import *


class Message:
    def __init__(self, data, user, room, server):
        self.data = data
        now = datetime.now()
        msg_date = now.strftime("%d/%m/%Y %H:%M")
        self.date = msg_date
        self.user = user
        self.room = room
        self.server = server

    def db_formatting(self):
        return {
            "room": self.room,
            "timestamp": str(self.date),
            "msg": self.data,
            "sender": self.user
        }

    def send_to_db(self):
        message = {
            "server": self.server,
            "room": self.room,
            "data": self.data,
            "date": self.date,
            "user": self.user
        }
        ConnectToDb().messages.insert_one(message)
