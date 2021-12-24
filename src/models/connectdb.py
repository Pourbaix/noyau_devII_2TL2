from pymongo import MongoClient


class ConnectError(Exception):
    pass


class ConnectToDb:
    """Class representing connection to a mongoDb database.

        This class allows you to connect to a db and gives you some operation to do with it.
    """
    def __init__(self):
        """This initialise the connection with the database.

            PRE:name is the name of the user used to connect to the database,
                password is the password of the user used to connect to the database.
            POST: initialise the connection to the database.
            :raise: Error if: -A connection Errors occurs

        """
        certificate_path = "../../X509-cert-3909330471699738491.pem"
        uri = "mongodb+srv://cluster0.nehju.mongodb.net/myFirstDatabase?authSource=" \
              "%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"
        try:
            cluster = MongoClient(uri, tls=True, tlsCertificateKeyFile=certificate_path)
            db1 = cluster["dbOo"]
            users = db1["Users"]
            messages = db1["Messages"]

            self.__users = users
            self.__db = db1
            self.__messages = messages
        except:
            raise ConnectError("\n\n-----------------------------"
                               "An error has occurred while connecting to the database."
                               "\n\n-----------------------------")

    def db(self):
        """Return an object that points to the database.

        PRE: -
        POST:Returns the pointer Object

        """
        return self.__db

    @property
    def users(self):
        """Return an object that points to the users document in the database.

        PRE: -
        POST:Returns the pointer Object

        """
        return self.__users

    @property
    def messages(self):
        """Return an object that points to the messages document in the database.

        PRE: -
        POST:Returns the pointer Object

                """
        return self.__messages

    @property
    def number_user(self):
        """This returns the number of users in the database.

        PRE: -
        POST: Return the number of users present in the database

        """
        doc_count = self.__users.count_documents({})
        return doc_count

    @property
    def number_message(self):
        """This returns the number of messages in the database.

        PRE: -
        POST: Return the number of messages present in the database

        """
        doc_count = self.__messages.count_documents({})
        return doc_count
