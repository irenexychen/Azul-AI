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
        self.az_player = Player(self.az_table)
        self.ai_player = AiPlayer(self.az_table)
        self.players.append(self.az_player)
        self.players.append(self.ai_player)
        self.ai_player.get_opponents(self.players)

    def play_game(self):
        self.az_table.fill_boxes()
        self.print_table()
        while not self.last_round:
            if self.az_table.has_tile():
                for player in self.players:
                    if self.az_table.has_tile():
                        used_tile = player.play()
                        self.az_table.fetch_tiles(used_tile[0], used_tile[1], used_tile[2])
                    else:
                        break

            for player in self.players:
                self.last_round = player.is_last_round()

            if not self.last_round:
                self.az_table.fill_boxes()

            for player in self.players:
                player.move_tile_to_board()

        for player in self.players:
            player.calculate_scores_after_round()
            if player.scores > self.maximum_scores:
                self.maximum_scores = player.scores
                self.winner = player.name

        print("The winner is %s" % self.winner)

    def print_table(self):
        for box_number in range(5):
            for tile_number in range(4):
                tiles = " %s" % self.az_table.round_boxes[box_number][tile_number]
            print(tiles)


if __name__ == '__main__':
    az_game = Game()
    az_game.play_game()
