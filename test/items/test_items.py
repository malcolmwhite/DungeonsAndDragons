from unittest import TestCase

from src.beans.items.sword import Sword
from src.beans.items.shield import Shield
from src.beans.items.shoes import Shoes
from src.beans.items.spooky_hat import SpookyHat


class TestItems(TestCase):
    def testSword(self):
        for _ in xrange(100):
            sword = Sword()
            self.assertEquals(sword.DEFENSE_BOOST, 0)
            self.assertEquals(sword.SPEED_BOOST, 0)
            self.assertEquals(sword.SPOOK_RATE, 0)
            self.assertEquals(sword.SPOOK_POWER, 0)
            self.assertTrue(sword.ATTACK_BOOST > 0)

    def testShield(self):
        for _ in xrange(100):
            shield = Shield()
            self.assertEquals(shield.ATTACK_BOOST, 0)
            self.assertEquals(shield.SPEED_BOOST, 0)
            self.assertEquals(shield.SPOOK_RATE, 0)
            self.assertEquals(shield.SPOOK_POWER, 0)
            self.assertTrue(shield.DEFENSE_BOOST > 0)

    def testShoes(self):
        for _ in xrange(100):
            shoes = Shoes()
            self.assertEquals(shoes.ATTACK_BOOST, 0)
            self.assertEquals(shoes.SPOOK_RATE, 0)
            self.assertEquals(shoes.SPOOK_POWER, 0)
            self.assertEquals(shoes.DEFENSE_BOOST, 0)
            self.assertTrue(shoes.SPEED_BOOST > 0)

    def testSpookyHat(self):
        for _ in xrange(100):
            hat = SpookyHat()
            self.assertEquals(hat.ATTACK_BOOST, 0)
            self.assertEquals(hat.DEFENSE_BOOST, 0)
            self.assertEquals(hat.SPEED_BOOST, 0)
            self.assertTrue(hat.SPOOK_RATE > 0)
            self.assertTrue(hat.SPOOK_POWER > 0)