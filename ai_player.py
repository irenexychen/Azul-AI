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
        tiles = self.get_the_most_tiles()
        # TODO if not find a row, set 9?
        return row, tiles

    def get_the_most_tiles(self):
        color = 0
        amount = 0
        for number_of_tiles in range(5, 1, -1):
            if self.az_table.round_boxes_by_number[number_of_tiles] > 0:
                color = self.az_table.round_boxes_by_number[number_of_tiles][0]
                amount = number_of_tiles
        return color, amount
