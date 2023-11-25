from sortedcontainers import SortedList


class Trade:
    def __init__(self, person, amount, side, shares):
        self.amount = amount
        self.side = side
        self.shares = shares
        self.person = person

    def __lt__(self, other):
        if (self.amount != other.amount):
            return self.amount < other.amount
        else:
            return self.shares < other.shares

    def __repr__(self):
        return f"Name: {self.person}, Side: {self.side}, Shares: {self.shares}, Amount: {self.amount}"


class Exchange:
    # implement this!

    def __init__(self, initialBalance):
        """Initial Balance is the amount that each account should start with."""
        self.initialBalance = initialBalance
        self.buyTrades = SortedList()
        self.sellTrades = SortedList()
        self.peopleAmounts = {}
        self.peopleShares = {}

    def add_trade(self, trade):
        """Adds a trade to the exchange (validation required)
        and returns a match if required. It is up to you on how you will
        handle representing trades. """
        if (trade.person not in self.peopleAmounts):  # Each Person starts off with 10 Shares and specified initial balance
            self.peopleAmounts[trade.person] = self.initialBalance
            self.peopleShares[trade.person] = 10
        if (trade.side == "BUY"):
            if (self.peopleAmounts[trade.person] < trade.shares * trade.amount):
                return False
            while (trade.shares > 0):
                index = self.sellTrades.bisect_left(trade)
                if (len(self.sellTrades) == 0 or self.sellTrades[index].price > trade.price):
                    break
                curTrade = self.sellTrades[index]
                if (self.peopleShares[trade.person] < trade.shares):
                    self.sellTrades.remove(curTrade)
                    continue
                avgPrice = (trade.amount + curTrade.amount)/2
                if (trade.shares >= curTrade.shares):
                    self.peopleAmounts[curTrade.person] += avgPrice * \
                        curTrade.shares
                    self.peopleAmounts[trade.person] -= avgPrice * \
                        curTrade.shares
                    self.peopleShares[trade.person] += curTrade.shares
                    trade.shares -= curTrade.shares
                    self.peopleShares[curTrade.person] -= curTrade.shares
                    self.sellTrades.remove(curTrade)
                else:
                    self.peopleAmounts[curTrade.person] += avgPrice * \
                        trade.shares
                    self.peopleAmounts[trade.person] -= avgPrice * trade.shares
                    self.peopleShares[trade.person] += trade.shares
                    self.peopleShares[curTrade.person] -= trade.shares
                    curTrade.shares -= trade.shares
                    trade.shares = 0

            if (trade.shares > 0):
                self.buyTrades.add(trade)
            return True
        else:
            # Check that person actually has the number of shares they want to sell

            if (self.peopleShares[trade.person] < trade.shares):
                return False

            while (trade.shares > 0):
                # Find all trades that have a price higher than the sell price
                index = self.buyTrades.bisect_right(trade)
                # Sell price is higher than all buy trade prices
                if (len(self.buyTrades) == 0 or index >= len(self.buyTrades)):
                    break
                curTrade = self.buyTrades[index]
                # Check that person who wants to buy has enough balance
                if (self.peopleAmounts[curTrade.person] < curTrade.shares * curTrade.amount):
                    self.buyTrades.remove(curTrade)
                    continue

                avgPrice = (trade.amount + curTrade.amount)/2
                if (trade.shares >= curTrade.shares):
                    self.peopleAmounts[trade.person] += avgPrice * \
                        curTrade.shares
                    self.peopleAmounts[curTrade.person] -= avgPrice * \
                        curTrade.shares
                    self.peopleShares[curTrade.person] += curTrade.shares
                    trade.shares -= curTrade.shares
                    self.peopleShares[trade.person] -= curTrade.shares
                    self.buyTrades.remove(curTrade)
                else:
                    self.peopleAmounts[trade.person] += avgPrice * \
                        trade.shares
                    self.peopleAmounts[curTrade.person] -= avgPrice * \
                        trade.shares
                    self.peopleShares[trade.person] -= trade.shares
                    self.peopleShares[curTrade.person] += trade.shares
                    curTrade.shares -= trade.shares
                    trade.shares = 0

            if (trade.shares > 0):
                self.sellTrades.add(trade)
            return True
