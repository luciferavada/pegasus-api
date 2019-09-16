import os

from sugar_odm import MongoDBModel
from sugar_api import JSONAPIMixin


class APIModel(MongoDBModel, JSONAPIMixin):

    __connection__ = {
        'host': os.getenv('MONGODB_URI', 'mongodb://localhost'),
        'retrywrites': False
    }

    __database__ = {
        'name': os.getenv('MONGODB_DB', 'pegasus')
    }
