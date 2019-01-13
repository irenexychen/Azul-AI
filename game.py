from table import Table
from player import Player
from ai_player import AiPlayer


class Game:
    players = []
    last_round = False
    winner = " "
    maximum_scores = 0

    def __init__(self):
        self.az_table = Table()
        self.az_player = Player("MyPlayer", self.az_table)
        self.ai_player = AiPlayer("AiPlayer", self.az_table)
        self.players.append(self.az_player)
        self.players.append(self.ai_player)
        self.ai_player.get_opponents(self.players)

    def play_game(self):
        self.az_table.fill_boxes()
        while not self.last_round:
            self.az_table.print_table()
            if self.az_table.has_tile():
                for player in self.players:
                    if self.az_table.has_tile():
                        print("Player = %s" % player.name)
                        player.play()
                    else:
                        break

            for player in self.players:
                if player.is_last_round():
                    self.last_round = player.is_last_round()

            for player in self.players:
                player.move_tiles_to_board()

            if not self.last_round and not self.az_table.has_tile():
                self.az_table.fill_boxes()

        for player in self.players:
            player.calculate_scores_after_round()
            if player.scores > self.maximum_scores:
                self.maximum_scores = player.scores
                self.winner = player.name

        print("The winner is %s" % self.winner)


if __name__ == '__main__':
    az_game = Game()
    az_game.play_game()
