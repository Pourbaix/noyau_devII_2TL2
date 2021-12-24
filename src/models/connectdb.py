from pymongo import MongoClient
from src.config import config


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
        certificat_path = config.ROOT_DIR + "/2TL2-G3.pem"
        uri = "mongodb+srv://cluster0.5i6qo.gcp.mongodb.net/ephecom?authSource=%24external&authMechanism=MONGODB-X509&" \
              "retryWrites=true&w=majority&ssl_cert_reqs=CERT_NONE"
        try:
            cluster = MongoClient(uri, tls=True, tlsCertificateKeyFile=certificat_path)
            db1 = cluster["ephecom-2TL2"]
            messages = db1["messages"]

            self.__db = db1
            self.__messages = messages
        except:
            raise ConnectError("\n\n-----------------------------"
                               "An error has occurred while connecting to the database."
                               "\n\n-----------------------------")

    @property
    def db(self):
        """Return an object that points to the database.

        PRE: -
        POST:Returns the pointer Object

        """
        return self.__db

    @property
    def messages(self):
        """Return an object that points to the messages document in the database.

        PRE: -
        POST:Returns the pointer Object

                """
        return self.__messages

    @property
    def number_message(self):
        """This returns the number of messages in the database.

        PRE: -
        POST: Return the number of messages present in the database

        """
        doc_count = self.__messages.count_documents({})
        return doc_count
