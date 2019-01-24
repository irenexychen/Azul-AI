from player import Player
from tile_type import TileType
from used_tile import UsedTile


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
        self.az_plate.add(tile_to_move.destination_row, switcher[tile_to_move.type], tile_to_move.quantity)
        self.az_table.adjust_fetched_tiles(tile_to_move.source_box, switcher[tile_to_move.type])
        self.az_plate.print_plate()

    def find_next_move(self):
        # TODO to refine
        # Find row to fill
        row = self.az_plate.get_empty_row()
        if row == -1:
            row = self.az_plate.get_partial_filled_row()
        # Find tiles
        tiles = self.get_most_tiles_from_pool()
        # TODO this is the spot to apply AI and searching algorithm
        if tiles.quantity == 0:
            tiles = self.get_most_tiles_from_box()
        tiles.destination_row = row
        return tiles

    def get_most_tiles_from_box(self):
        amount = 0
        tile_to_fetch: UsedTile
        for number_of_tiles in range(4, 0, -1):
            for k in range(5):
                if len(self.az_table.round_boxes_by_number[k][number_of_tiles]) > 0:
                    tiles = self.az_table.round_boxes_by_number[k][number_of_tiles]
                    amount = number_of_tiles
                    tile_to_fetch = UsedTile(k, tiles[0], amount)
                    break
            if amount > 0:
                break
        return tile_to_fetch

    def get_most_tiles_from_pool(self):
        amount_to_fetch = 0
        found = False
        for color in self.az_table.pool.keys():
            if self.az_table.pool[color] > amount_to_fetch:
                amount_to_fetch = self.az_table.pool[color]
                found = True
                break
        return UsedTile(-1, color, amount_to_fetch) if found else UsedTile(-1, color, amount_to_fetch)
