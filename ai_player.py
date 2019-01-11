from player import Player


class AiPlayer(Player):
    opponents = []

    def get_opponents(self, players):
        for player in players:
            if player.id != self.id:
                self.opponents.append(player)

    def play(self):
        self.find_next_move()

    def find_next_move(self):
        # TODO to refine
        # Find row to fill
        row = self.az_plate.get_empty_row()
        if row == -1:
            row = self.az_plate.get_partial_filled_row()
        # Find tiles
        tiles = self.get_most_tiles()
        # TODO if not find a row, set 9?
        return row, tiles[0], tiles[1]

    def get_most_tiles(self):
        colors = []
        amount = 0
        for number_of_tiles in range(4, 1, -1):
            for k in range(5):
                if len(self.az_table.round_boxes_by_number[k][number_of_tiles]) > 0:
                    colors = self.az_table.round_boxes_by_number[k][number_of_tiles]
                    amount = number_of_tiles
                    break
            if amount > 0:
                break
        return colors[0], amount
