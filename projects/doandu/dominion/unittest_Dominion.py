import testUtility
import Dominion

class TestCard:
    def setUp(self):
        self.player_name = testUtility.getPlayerNames()
        self.nV = testUtility.getNumberCurse(self.player_name)
        self.nC = testUtility.getNumberVictory(self.player_name)
        self.box = testUtility.getBoxes(self.nV)
        self.supply_order = testUtility.getSupplyOrder()

        # pick cards from box to be in supply
        self.supply = testUtility.getSupply(self.box, self.player_name, self.nV, self.nC)
        self.trash = []
        self.player = Dominion.Player('Annie')

    def test_init(self):
        self.setUp()
        cost = 1
        buypower = 5

        #instantiate the card object
        card = Dominion.Coin_card(self.player.name, cost, buypower)

        # verify
        '''      
        self.assertEqual('Annie', card.name)
        self.assertEqual(buypower, card.buypower)
        self.assertEqual(cost, card.cost)
        self.assertEqual("coin", card.category)
        self.assertEqual(0, card.vpoints)
        '''

        assert card.name == 'Annie'
        assert card.buypower == buypower
        assert card.cost == cost
        assert card.category == "coin"
        assert card.vpoints == 0

    def test_react(self):
        pass
