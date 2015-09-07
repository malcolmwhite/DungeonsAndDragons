from unittest import TestCase

from src.beans.items.sword import Sword
from src.beans.items.shield import Shield
from src.beans.items.shoes import Shoes
from src.beans.items.spooky_hat import SpookyHat
from src.managers.items.item_manager import ItemManager


class TestItemManager(TestCase):
    def testAddSword(self):
        mgr = ItemManager()
        expected_attack_boost = 6
        sword = Sword(attack=expected_attack_boost)
        mgr.add_item(sword)
        retrieved_sword = mgr.get_sword()
        self.assertEquals(retrieved_sword, sword)
        actual_attack_boost = mgr.get_atk_boost()
        self.assertEqual(expected_attack_boost, actual_attack_boost)

    def testAddShield(self):
        mgr = ItemManager()
        expected_defense_boost = 6
        shield = Shield(defense=expected_defense_boost)
        mgr.add_item(shield)
        retrieved_shield = mgr.get_shield()
        self.assertEquals(retrieved_shield, shield)
        actual_defense_boost = mgr.get_def_boost()
        self.assertEqual(expected_defense_boost, actual_defense_boost)

    def testAddShoes(self):
        mgr = ItemManager()
        expected_speed_boost = 6
        shoes = Shoes(speed=expected_speed_boost)
        mgr.add_item(shoes)
        retrieved_shoes = mgr.get_shoes()
        self.assertEquals(retrieved_shoes, shoes)
        actual_seed_boost = mgr.get_speed_boost()
        self.assertEqual(expected_speed_boost, actual_seed_boost)

    def testAddSpookyHat(self):
        mgr = ItemManager()
        expected_spook_rate = 25
        expected_spook_power = 2
        hat = SpookyHat(spook_rate=expected_spook_rate, spook_power=expected_spook_power)
        mgr.add_item(hat)
        retrieved_hat = mgr.get_hat()
        self.assertEquals(retrieved_hat, hat)
        actual_spook_rate, actual_spook_power = mgr.get_spook_params()
        self.assertEqual(expected_spook_rate, actual_spook_rate)
        self.assertEqual(expected_spook_power, actual_spook_power)

    def testSwordAutoSort(self):
        mgr = ItemManager()
        expected_attack_boost = 11
        sword1 = Sword(attack=5)
        sword2 = Sword(attack=7)
        strongest_sword = Sword(attack=11)
        sword4 = Sword(attack=9)
        sword5 = Sword(attack=1)
        really_attacky_shield = Shield(attack=11000)
        mgr.add_items([sword1, sword2, strongest_sword, sword4, sword5, really_attacky_shield])
        retrieved_sword = mgr.get_sword()
        self.assertEquals(retrieved_sword, strongest_sword)
        actual_attack_boost = mgr.get_atk_boost()
        self.assertEqual(expected_attack_boost, actual_attack_boost)

    def testDumpItems(self):
        original_manager = ItemManager()
        expected_attack_boost = 11
        sword1 = Sword(attack=5)
        sword2 = Sword(attack=7)
        strongest_sword = Sword(attack=11)
        sword4 = Sword(attack=9)
        sword5 = Sword(attack=1)
        original_manager.add_items([sword1, sword2, strongest_sword, sword4, sword5])
        dumped_items = original_manager.dump_all_items()
        old_attack_boost = original_manager.get_atk_boost()
        self.assertEqual(old_attack_boost, 0)
        self.assertEqual(len(dumped_items), 5)
        new_manager = ItemManager()
        new_manager.add_items(dumped_items)
        new_attack_boost = new_manager.get_atk_boost()
        self.assertEqual(expected_attack_boost, new_attack_boost)
