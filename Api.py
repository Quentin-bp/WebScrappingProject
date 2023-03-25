from fastapi import FastAPI
from Database import *
from Weapon import WeaponModel

app = FastAPI()

@app.get("/weapons")
async def weapons():
    data = getAllWeapons()
    return data

@app.post("/weapons/add")
async def addWeapon(weapon: WeaponModel):
    return insertWeapon(weapon)

@app.put("/weapons/edit")
async def editWeapon(weapon: WeaponModel):
    return updateWeapon(weapon)

@app.delete("/weapons/remove")
async def deleteWeapon(weapon: WeaponModel):
    return removeWeapon(weapon)