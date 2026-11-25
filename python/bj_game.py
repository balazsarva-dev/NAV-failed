from black_jack.process import Process
from menu import Menu
from logsettings import logger

class Blackjack(Menu):
    def __init__(self) -> None:
        super().__init__(game="Blackjack")

    def play(self) -> None:
        process = Process()
        process.display_bets()
        logger.info('\nFirst card of the players and the dealer!\n')
        players = process.blackjack.get_players()
        process.get_one_round(process.blackjack.deal_first_card, players)
        process.view_hands()
        process.insurance_against_blackjack(players)
        logger.info('\nFirst 2 cards of the players and the dealer!\n')
        process.get_one_round(process.blackjack.deal_second_card, players)
        process.view_hands()
        process.surrender(players)
        process.view_hands()
        logger.info(f'Here are your winnings:\n{process.check_winnings()}')
