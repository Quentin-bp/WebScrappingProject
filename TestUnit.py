import unittest
from unittest import mock
from Database import *
from Pages.WeaponPage import *
from unittest.mock import Mock, PropertyMock


class DatabaseTest(unittest.TestCase):
    def test_get_all_weapons(self):
        data = getAllWeapons()
        self.assertTrue(type(data), list)

    def test_find_weapon_exists(self):
        name = "Dagger(短刀)"
        self.assertEqual(type(findWeaponByName(name)), dict, "Name unknown")

    def test_find_weapon_doesnt_exist(self):
        nameSecond = "null"
        self.assertEqual(findWeaponByName(nameSecond), None, "Name exists")

    def test_remove_weapon(self):
        weapon = Mock()
        # prendre l'id dans la bdd, pour plus de facilite
        weapon.id = "PUT_AN_EXISTENT_ID"
        self.assertEqual(removeWeapon(weapon), "Deleted", "Id unknown")

    def test_update_weapon(self):
        weapon = Mock()
        weapon.id = "PUT_AN_EXISTENT_ID"
        weapon.name = "nullName"
        weapon.owner = "Test-Owner"
        weapon.price = "Test-Price"
        weapon.description = "Test-Description"
        self.assertEqual(type(updateWeapon(weapon)), dict, "Bad class return")
        self.assertEqual(updateWeapon(weapon)["response"], False, "ID unknown")

    def test_add_weapon_already_added(self):
        weapon = Mock()
        weapon.name = "nullName"
        weapon.owner = "Test-Owner"
        weapon.price = "Test-Price"
        weapon.description = "Test-Description"
        self.assertEqual(insertWeapon(weapon)["response"], False, "Already Added")

    def test_add_weapon(self):
        weapon = Mock()
        weapon.name = "nullName"
        weapon.owner = "Test-Owner"
        weapon.price = "Test-Price"
        weapon.description = "Test-Description"
        self.assertEqual(insertWeapon(weapon), "Added", "Already Exists")


class ScrapperTest(unittest.TestCase):
    def test_get_data_from_path(self):
        scraper = Scraper("https://danmachi.fandom.com/wiki/Items")
        data = scraper.getDataFromPath("table", "wikitable")
        self.assertIsNotNone(data, "Data are null")

testBDD = DatabaseTest()

#testBDD.test_get_all_weapons()
#testBDD.test_find_weapon_exists()
#testBDD.test_find_weapon_doesnt_exist()
#testBDD.test_remove_weapon()
#testBDD.test_update_weapon()
#testBDD.test_add_weapon_already_added()
#testBDD.test_add_weapon()

testScrapper = ScrapperTest()

#testScrapper.test_get_data_from_path()
