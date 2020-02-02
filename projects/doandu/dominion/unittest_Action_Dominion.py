import testUtility
import Dominion

class TestAction:

    def test_init(self):

        #make variables
        cost = 1
        actions = 1
        cards = 1
        buys = 1
        coins = 1
        #call function
        actionCard = Dominion.Action_card("MegaCard",cost,actions,cards,buys,coins)

        # assert
        assert actionCard.name == "MegaCard"
        assert actionCard.cost == 1
        assert actionCard.actions == 1
        assert actionCard.cards == 1
        assert actionCard.buys == 1
        assert actionCard.coins == 1

    def test_use(self):
        # define variables
        # call function
        # assert calls

        #use calls for a player and trash.
        # thus we need a trash bin and a player
        # we can then test the size of each deck respectively to ensure use is properly used

        #initalize variables
        # note assert to make sure they have nothing in them
        player = Dominion.Player("Duke")
        trash = []
        #assert len(trash) == 0
        assert len(player.played) == 0
        assert len(player.hand) == 5
        actionCard = Dominion.Action_card("MegaCard",1, 1, 1, 1, 1)
        player.hand.append(actionCard)
        assert len(player.hand) == 6


        #call function
        actionCard.use(player, trash)

        #assert
        assert len(player.played) == 1
        # trash is never used in the function and can be omitted.
        # assert len(trash) == 1


    def test_augment(self):
        #Think augment as the effect of each action card
        # when played it will alter the player's stats by the level of the card.
        # use it similarly as use.
        player = Dominion.Player("Duke")
        actionCard = Dominion.Action_card("MegaCard",1, 1, 1, 1, 1)
        player.actions = 0
        player.buys = 0
        player.purse = 0
        assert player.actions == 0
        assert player.buys == 0
        assert player.purse == 0
        assert len(player.hand) == 5

        #call function
        actionCard.augment(player)
        #because the cards are all plus 1
        assert player.actions == 1
        assert player.buys == 1
        assert player.purse == 1
        assert len(player.hand) == 6

    def test_play(self):
        pass
