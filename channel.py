#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Ce fichier contient une classe représentant un channel.
    ----- CODE DE LA CLASSE A IMPLEMENTER -----
"""


class Channel:
    def __init__(self, server_identifier, server_name, channel_identifier, channel_name, group, icon_path=None, participants=None):
        self.server_identifier = server_identifier
        self.server_name = server_name
        self.channel_identifier = channel_identifier
        self.channel_name = channel_name
        self.group = group
        self.icon_path = icon_path
        self.participants = participants

    def join(self):
        """
            Méthode permettant à un utilisateur de rejoindre ce channel.
        """
        pass

    def leave(self):
        """
            Méthode permettant à un utilisateur de quitter ce channel.
        """
        pass

    def get_participants_status(self):
        pass

    def get_message_history(self):
        pass

    def send_message(self):
        pass
