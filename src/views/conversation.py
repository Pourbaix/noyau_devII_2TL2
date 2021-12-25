#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    [BASE]
    Ce fichier représente une zone de conversation.
"""
import json

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.scrollview import ScrollView

from src.config import config
from src.libs.bot.commands import Commands
from src.models.gen_message import Message
from src.models.connectdb import ConnectToDb
from src.views.teams_container import TeamsContainer

Builder.load_file("{0}/conversation.kv".format(config.VIEWS_DIR))


class InputsContainer(BoxLayout):
    pass


class MessageLabel(Label):
    pass


class MessageSent(MessageLabel):
    pass


class MessageReceived(MessageLabel):
    pass


class ConversationContainer(ScrollView):

    def __init__(self, channel_id):
        super(ConversationContainer, self).__init__()
        self.channel_id = channel_id
        self.messages_box = self.ids.messages_container

        # Démarrer la mise à jour régulière de la conversation
        self.constant_update(channel_id)

    def constant_update(self, channel_id):
        self.init_conversation(channel_id)
        # time.sleep(1)

    def init_conversation(self, conv_id):
        # conv_file_path = config.PUBLIC_DIR + "/tmp_conversations/basic.json"
        messages = ConnectToDb().messages
        print(conv_id)
        for shit in TeamsContainer.get_data_from_db():
            print(shit)
        if messages.find():
            pass
        else:
            test = Message("testMessage", "User1", conv_id)
            test.send_to_db()
        """ 
        with open(conv_file_path) as json_file:
            conv = json.load(json_file)
            if conv:
                print("pas vide")
            else:
                print("vide")
        """

        for message in messages.find():
            print(message)
            if message["room"] == conv_id:
                msg = MessageSent(text=message["date"] + " - " + message["user"] + "\n" + message["data"])
                self.messages_box.add_widget(msg, len(self.messages_box.children))

    def add_message(self, msg_obj, pos="left"):
        msg = MessageSent()

        if pos == "right":
            msg = MessageReceived()

        msg.text = str(msg_obj.date) + " - " + msg_obj.user + "\n" + msg_obj.data
        self.messages_box.add_widget(msg, len(self.messages_box.children))


class Conversation(RelativeLayout):

    def __init__(self, channel_id):
        super(Conversation, self).__init__()
        self.messages_container = ConversationContainer(channel_id)
        self.inputs_container = InputsContainer()
        self.channel = channel_id

        self.add_widget(self.messages_container)
        self.add_widget(self.inputs_container)

    def send_message(self):
        txt = self.inputs_container.ids.message_input.text

        if txt:
            msg = Message(txt, "Moi", self.channel)
            self.messages_container.add_message(msg)
            msg.send_to_db()

            if txt[0] == "/":
                bot = Commands(txt)
                response_from_bot = bot.result
                msg_res = Message(response_from_bot, "E-Bot", self.channel)
                self.messages_container.add_message(msg_res, pos="right")

            self.inputs_container.ids.message_input.text = ""
