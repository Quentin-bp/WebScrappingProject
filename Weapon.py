import bson
from pydantic import BaseModel
from typing import Union
class Weapon:

    def __init__(self, name, owner, price, description):
        self.name = name
        self.owner = owner
        self.price = price
        self.description = description

    def getFormattedJson(self):
        return {
            "name": self.name,
            "owner": self.owner,
            "price": self.price,
            "description": self.description
        }



class WeaponModel(BaseModel):
    id: str
    name: str
    owner: str
    price: float
    description: str