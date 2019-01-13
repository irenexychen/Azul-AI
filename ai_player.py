from player import Player
from tile_type import TileType


class AiPlayer(Player):
    opponents = []

    def get_opponents(self, players):
        for player in players:
            if player.id != self.id:
                self.opponents.append(player)

    def play(self):
        switcher = {
            1: TileType.BLUE,
            2: TileType.YELLOW,
            3: TileType.RED,
            4: TileType.BLACK,
            5: TileType.WHITE,
        }
        tile_to_move = self.find_next_move()
        self.az_plate.add(tile_to_move[1], switcher[tile_to_move[2]], tile_to_move[3])
        self.az_table.adjust_fetched_tiles(tile_to_move[0], switcher[tile_to_move[2]], tile_to_move[3])

    def find_next_move(self):
        # TODO to refine
        # Find row to fill
        row = self.az_plate.get_empty_row()
        if row == -1:
            row = self.az_plate.get_partial_filled_row()
        # Find tiles
        tiles = self.get_most_tiles()
        # TODO if not find a row, set 9?
        return tiles[0], row, tiles[1], tiles[2]

    def get_most_tiles(self):
        tiles = []
        amount = 0
        for number_of_tiles in range(4, 0, -1):
            for k in range(5):
                if len(self.az_table.round_boxes_by_number[k][number_of_tiles]) > 0:
                    tiles = self.az_table.round_boxes_by_number[k][number_of_tiles]
                    amount = number_of_tiles
                    break
            if amount > 0:
                break
        return k, tiles[0], amount
