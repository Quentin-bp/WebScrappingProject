from Weapon import Weapon
from Scraper import Scraper
from Database import *
from decouple import config


link = config('LINK_SCRAPPER')
print(link)
scraper = Scraper(link) # in .env file


def insertAllData():
    data =getAllWeaponsFromWeb()
    insertAllWeapon(data)


def getAllWeaponsFromWeb():
    table = scraper.getDataFromPath("table", "wikitable")
    rows = table.find_all("tr")
    i = 0
    list_weapon = []

    for weapon in rows:
        if (i != 0):
            column = weapon.find_all("td")
            weapon = Weapon(column[0].text.rstrip(), column[1].text.rstrip(), column[3].text.rstrip(), column[2].text.rstrip())
            list_weapon.append(weapon)
        i += 1

    return list_weapon

insertAllData()