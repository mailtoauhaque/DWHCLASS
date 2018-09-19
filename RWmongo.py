from pymongo import *
from Config import Configuration
import sys

MongoStore = Configuration().GetData()['MongoDb']
MongoIP = Configuration().GetData()['PrivateIp']
MonngoPort = Configuration().GetData()['MongoPort']
print ('Current DB Configuration on Mongo for BDME:', MongoIP, MonngoPort, MongoStore)

def WriteValue(collectionName, KN, Value):
    try:

        client = MongoClient(MongoIP, MonngoPort)
        db = client[str(MongoStore)]
        collection = db[collectionName]
        post_data = {
            'Key': str(KN),
            'Data': str(Value)
        }
        collection.insert_one(post_data)
    except IOError as e:
        print ("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print ("Could not convert data to an integer.")
    except:
        print ("Unexpected error:", sys.exc_info()[0])



def ReadValue(collectionName, KN):
    try:
        print (MongoStore, collectionName, KN, MongoIP, MonngoPort)
        client = MongoClient(MongoIP, MonngoPort)
        db = client[str(MongoStore)]
        collection = db[collectionName]
        value = collection.find_one({'Key': str(KN)})
        return value
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])


def ReadAll(collectionName):
    try:
        client = MongoClient(MongoIP, MonngoPort)
        db = client[str(MongoStore)]
        collection = db[collectionName]
        value = collection.find({})
        return value
    except IOError as e:
        print("I/O error({0}): {1}".format(e.errno, e.strerror))
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])
