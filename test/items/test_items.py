from unittest import TestCase

from main.items.sword import Sword
from main.items.shield import Shield
from main.items.shoes import Shoes
from main.items.spooky_hat import SpookyHat


class TestItems(TestCase):
    def testSword(self):
        sword = Sword()
        self.assertEquals(sword.DEFENSE_BOOST, 0)
        self.assertEquals(sword.SPEED_BOOST, 0)
        self.assertEquals(sword.SPOOK_RATE, 0)
        self.assertEquals(sword.SPOOK_POWER, 0)
        self.assertTrue(sword.ATTACK_BOOST > 0)

    def testShield(self):
        shield = Shield()
        self.assertEquals(shield.ATTACK_BOOST, 0)
        self.assertEquals(shield.SPEED_BOOST, 0)
        self.assertEquals(shield.SPOOK_RATE, 0)
        self.assertEquals(shield.SPOOK_POWER, 0)
        self.assertTrue(shield.DEFENSE_BOOST > 0)

    def testShoes(self):
        shoes = Shoes()
        self.assertEquals(shoes.ATTACK_BOOST, 0)
        self.assertEquals(shoes.SPOOK_RATE, 0)
        self.assertEquals(shoes.SPOOK_POWER, 0)
        self.assertEquals(shoes.DEFENSE_BOOST, 0)
        self.assertTrue(shoes.SPEED_BOOST > 0)

    def testSpookyHat(self):
        hat = SpookyHat()
        self.assertEquals(hat.ATTACK_BOOST, 0)
        self.assertEquals(hat.DEFENSE_BOOST, 0)
        self.assertEquals(hat.SPEED_BOOST, 0)
        self.assertTrue(hat.SPOOK_RATE > 0)
        self.assertTrue(hat.SPOOK_POWER > 0)