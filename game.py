from table import Table
from player import Player
from ai_player import AiPlayer


class Game:
    players = []
    last_round = False
    winner = " "
    maximum_scores = 0

    def __init__(self):
        self.az_player = Player()
        self.ai_player = AiPlayer()
        self.players.append(self.az_player)
        self.players.append(self.ai_player)
        self.az_table = Table()

    def play_game(self):
        while not self.last_round:
            if self.az_table.has_tile():
                for player in self.players:
                    if self.az_table.has_tile():
                        player.play()
                    else:
                        break

            for player in self.players:
                self.last_round = player.is_last_round()

            if not self.last_round:
                self.az_table.fill_boxes()

        for player in self.players:
            player.move_tile_to_board()
            player.calculate_score_after_round()
            if player.scores > self.maximum_scores:
                self.maximum_scores = player.scores
                self.winner = player.name

        print("The winner is %s" % self.winner)
