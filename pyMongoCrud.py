from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.

        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30390
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary 
            return True
        else:
            return False

    def read(self, criteria):
        # An example of how to use this method:
        #  criteria = {"key": "value"}
        #  result = animal_shelter.read(criteria)  #Returns a list of documents matching that criteria

        foundList = []
        cursor = self.collection.find(criteria)
        for document in cursor:
            foundList.append(document)
        return foundList if foundList else None
    
    def update(self, criteria, changes):
        #How to use this method:
        #criteria = {"key: "Value", "key2": "value2", etc.}
        #changes = {"key": "newValue", "key2": "newValue2", etc.}
        #result = animal_shelter.update(criteria, changes)    #Returns number of modifications
        
        if criteria is not None and changes is not None:
            result = self.collection.update_many(criteria, {"$set": changes } )
            return result.modified_count
        else: 
            return 0
       
    def delete(self, criteria):
        if criteria is not None:
            result = self.collection.delete_many(criteria)
            return result.deleted_count
        else:
            return 0