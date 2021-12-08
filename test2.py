from pymongo import MongoClient
import certifi
from datetime import *
import threading

ca = certifi.where()
URL = "mongodb+srv://useradmintest:thisisapassword@cluster0.nehju.mongodb.net/Messages?retryWrites=true&w=majority"
cluster = MongoClient(URL, tlsCAFile=ca)
db1 = cluster["Chat1"]
db2 = cluster["Chat2"]
users1 = db1["Users"]
message1 = db1["msg"]
users2 = db2["Users"]
message2 = db2["msg"]


def connecting():
    """Little function to simulate the connection with a user and get the user id."""
    incorrect_name = True
    while incorrect_name:
        name = input("Please enter your name and password or type create to create a new user:")
        if name == "create":
            # We create a new user
            create = ""
            not_created = True
            while not_created:
                not_created = False
                create = input("Enter the name and the password of the new user:")
                for user in list_users:
                    if create.split(" ")[0] == user["Name"]:
                        print("This user already exist, please enter another name.")
                        not_created = True
                        break
            message = {"_id": maxId, "Name": create.split(" ")[0], "pwd": create.split(" ")[1]}
            users1.insert_many([message])
            print(f"Successfully logged with the user {create.split(' ')[0]}!")
            return maxId, create.split(" ")[0]
        else:
            # We log we a user already existing
            for user in list_users:
                if name.split(" ")[0] == user["Name"] and name.split(" ")[1] == user["pwd"]:
                    print(f"Successfully logged with the user {name.split(' ')[0]}!")
                    return user["_id"], name.split(" ")[0]
        print("This user doesn't exist or the password is wrong.")


def chat():
    user = connecting()
    while True:
        msg_maxid = 0
        msg = message1.find()
        for line in msg:
            list_users.append(line)
            msg_maxid = int(line["_id"]) + 1
        message = input(f"{user[1]}:")
        now = datetime.now()
        msg_date = now.strftime("%d/%m/%Y %H:%M")
        to_send = {"_id": msg_maxid, "user_id": user[0], "msg": message, "date": msg_date}
        message1.insert_one(to_send)


def get_message():
    list_messages = []
    for i in message1.find():
        list_messages.append(i)
        print(i["msg"])
    past_len = len(list_messages)
    while True:
        list_messages = []
        for i in message1.find():
            list_messages.append(i)
        actual_len = len(list_messages)
        if actual_len > past_len:
            for message in list_messages:
                print(f"{message['msg']}")
        past_len = actual_len


if __name__ == "__main__":
    list_users = []
    maxId = 0
    test = users1.find()
    for thing in test:
        list_users.append(thing)
        maxId = int(thing["_id"]) + 1
    print(list_users)
    sendingTHREAD = threading.Thread(target=chat)
    sendingTHREAD.start()
    receivingTHREAD = threading.Thread(target=get_message)
    receivingTHREAD.start()
