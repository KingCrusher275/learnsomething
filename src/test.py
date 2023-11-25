import unittest
import interface as inter


class TestInterfaceMethods(unittest.TestCase):

    def testPersonCreation(self):
        t = inter.Exchange(30)
        Trade1 = inter.Trade("Sam", 10, "BUY", 2)
        t.add_trade(Trade1)
        self.assertEqual(t.peopleAmounts["Sam"], 30)
        self.assertEqual(t.peopleShares["Sam"], 10)
        self.assertEqual(Trade1, t.buyTrades[0])

        Trade2 = inter.Trade("Alice", 12, "SELL", 3)
        t.add_trade(Trade2)
        self.assertEqual(t.peopleAmounts["Alice"], 30)
        self.assertEqual(t.peopleShares["Alice"], 10)
        self.assertEqual(Trade2, t.sellTrades[0])

    def testExchangeMatching(self):
        t = inter.Exchange(30)
        Trade1 = inter.Trade("Sam", 10, "BUY", 2)
        res1 = t.add_trade(Trade1)
        Trade2 = inter.Trade("Alice", 8, "SELL", 3)
        res2 = t.add_trade(Trade2)

        Trade3 = inter.Trade("Bob", 15, "BUY", 4)
        res3 = t.add_trade(Trade3)

        Trade4 = inter.Trade("Emma", 12, "SELL", 11)
        res4 = t.add_trade(Trade4)

        self.assertTrue(res1)
        self.assertTrue(res2)

        self.assertFalse(res3)
        self.assertFalse(res4)

        self.assertEqual(t.peopleAmounts["Sam"], 12)
        self.assertEqual(t.peopleAmounts["Alice"], 48)
        self.assertEqual(t.peopleShares["Sam"], 12)
        self.assertEqual(t.peopleShares["Alice"], 8)
        self.assertEqual(t.sellTrades[0].shares, 1)

    def testAll(self):
        t = inter.Exchange(100)
        Trade1 = inter.Trade("Sam", 10, "BUY", 4)
        t.add_trade(Trade1)
        Trade2 = inter.Trade("Alice", 20, "BUY", 2)
        t.add_trade(Trade2)

        Trade3 = inter.Trade("Sam", 30, "BUY", 1)
        t.add_trade(Trade3)

        Trade4 = inter.Trade("Bob", 40, "SELL", 2)
        t.add_trade(Trade4)
        Trade5 = inter.Trade("Joe", 16, "SELL", 3)
        t.add_trade(Trade5)

        self.assertEqual(t.peopleAmounts["Alice"], 64)
        self.assertEqual(t.peopleAmounts["Joe"], 159)
        self.assertEqual(t.peopleAmounts["Sam"], 77)
        self.assertEqual(t.peopleAmounts["Bob"], 100)

        self.assertEqual(t.peopleShares["Alice"], 12)
        self.assertEqual(t.peopleShares["Joe"], 7)
        self.assertEqual(t.peopleShares["Sam"], 11)
        self.assertEqual(t.peopleShares["Bob"], 10)


if __name__ == '__main__':
    unittest.main()
