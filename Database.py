from pymongo import MongoClient
from bson.objectid import ObjectId
import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

client = MongoClient('mongodb://localhost:27017/')

db = client['DanMachiScraping']
WeaponsCollection = db['Weapons']


def insertAllWeapon(weapons_list):
    data = []
    if (type(weapons_list) != list):
        return False

    for _weapon in weapons_list:
        weapon = { 
            "name": _weapon.name,
            "owner": _weapon.owner,
            "price": _weapon.price,
            "description": _weapon.description
        }
        data.append(weapon)
    WeaponsCollection.insert_many(data)
    return data


def insertWeapon(weapon):
    if (findWeaponByName(weapon.name)) :
        return {"response": False}
    if (hasattr(weapon, "id") and ObjectId.is_valid(weapon.id)):
        _id = ObjectId(weapon.id)
    else :
        _id = ObjectId()
    WeaponsCollection.insert_one({'_id': _id,'name':weapon.name, 'owner': weapon.owner, 'price': str(weapon.price), 'description': weapon.description})
    return "Added"

def updateWeapon(weapon):
    if WeaponsCollection.find_one({"_id": ObjectId(weapon.id)}):
        WeaponsCollection.update_one({'_id': ObjectId(weapon.id)},{"$set": {'name':weapon.name, 'owner': weapon.owner, 'price': str(weapon.price), 'description': weapon.description}})
        return WeaponsCollection.find_one({"_id": ObjectId(weapon.id)})
    else:
        return False
def getAllWeapons():
    data = WeaponsCollection.find({})
    return list(data)

def findWeaponByName(name):
    return WeaponsCollection.find_one({"name": name})

def removeWeapon(weapon):
    if WeaponsCollection.find_one({"_id": ObjectId(weapon.id)}):
        WeaponsCollection.delete_one({"_id":ObjectId(weapon.id)})
        return "Deleted"
    else :
        return "Error, doesn't exists"

def RemoveById(_id):
    if WeaponsCollection.find_one({"_id":ObjectId(_id)}):
        WeaponsCollection.delete_one({"_id":ObjectId(_id)})
        return True
    else :
        return False
     


