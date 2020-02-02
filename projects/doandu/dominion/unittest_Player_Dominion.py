import Dominion

class TestPlayer:
    def makeMegaCard(self):
        # for the sake of calculations mega card has a set value of 1 for all and name "mega Card"
        #make variables
        cost = 1
        actions = 1
        cards = 1
        buys = 1
        coins = 1
        #call function
        actionCard = Dominion.Action_card("MegaCard",cost,actions,cards,buys,coins)
        return actionCard

    def test_draw(self):
        # draws a card from player deck. else if will use the discard pile, if still none nothing happens

        #initate variables
        player = Dominion.Player("Duke")

        #set hand, and hand to 0
        # reset discard to contain new Dominion cards
        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0
        # add additional cards to change the expected points to be different
        # original from deck and stack == 3
        player.discard = [Dominion.Province()]*10

        #call function
        player.draw()

        #assert
        # hand size should be 1 and deck should be at 9
        assert len(player.hand) == 1
        assert len(player.deck) == 9


    def test_action_balance(self):
        # Per piazza - action_balance is a calculation of value that is use by the computer player to do their Auto Acts

        #initalize variables
        player = Dominion.Player("Duke")
        card = self.makeMegaCard()
        # to make a positive and easier number to calculate
        card.actions = 2
        player.deck.append(card)
        ## checking that the stack should now have 11
        assert len(player.stack()) == 11

        #call function
        actionBal = player.action_balance()

        #assert
        # 1 action card with (+) 2 act thus... balance = 1
        # 70*1 = 70
        # 11 cards
        # 6 ( rem 4)
        checkBal = 70/11
        assert actionBal == checkBal



    def test_cardsummary(self):

        #This function will iterate and calculate cards in the deck.
        # it will filter out and register card names and count total number of cards
        #initate variables
        player = Dominion.Player("Duke")

        #set hand, and hand to 0
        # reset discard to contain new Dominion cards
        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0
        # this way we can change and modify to show proper results
        player.deck = [Dominion.Province()]*10 + [Dominion.Gold()]*10

        # call function
        testSummary = player.cardsummary()

        # assert
        assert testSummary['Gold'] == 10
        assert testSummary['Province'] == 10
        assert testSummary['VICTORY POINTS'] == 60
    def test_calcpoints(self):
        #used to calculate Victory Points.

        #variables
        player = Dominion.Player("Duke")
        #empty card collections
        player.hand = []
        player.deck = []
        assert len(player.stack()) == 0
        # add additional cards to change the expected points to be different
        # original from deck and stack == 3
        player.deck = [Dominion.Province()]*10 + [Dominion.Duchy()]*10 + [Dominion.Gardens()]*10
        # 60 + 30 = 90 + ( 3*10) = 120; 30 Cards
        #call function
        playPoints = player.calcpoints()

        #assert
        assert playPoints == 120
