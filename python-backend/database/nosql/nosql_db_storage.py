#!/usr/bin/python3
"""
Contains the class for NoSQLDBStorage using PyMongo
"""

from pymongo import MongoClient
from os import getenv


class NoSQLDBStorage:
    """Interacts with a MongoDB database"""

    def __init__(self):
        """Initialize the database connection"""
        MONGO_HOST = getenv('MONGO_HOST', 'localhost')
        MONGO_PORT = int(getenv('MONGO_PORT', 27017))
        MONGO_DB = getenv('MONGO_DB', 'myDatabase')
        self.client = MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.client[MONGO_DB]

    def all(self, collection_name):
        """Retrieve all documents from a collection"""
        return list(self.db[collection_name].find())

    def get(self, collection_name, query):
        """Retrieve a single document by query"""
        return self.db[collection_name].find_one(query)

    def insert(self, collection_name, document):
        """Insert a new document into a collection"""
        return self.db[collection_name].insert_one(document).inserted_id

    def update(self, collection_name, query, update_data):
        """Update documents in a collection"""
        return self.db[collection_name].update_many(query, {'$set': update_data})

    def delete(self, collection_name, query):
        """Delete documents from a collection"""
        return self.db[collection_name].delete_many(query)

    def count(self, collection_name, query=None):
        """Count documents in a collection"""
        if query is None:
            query = {}
        return self.db[collection_name].count_documents(query)

    def close(self):
        """Close the database connection"""
        self.client.close()
