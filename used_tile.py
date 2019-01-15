from tile import Tile


class UsedTile(Tile):
    origination: 0
    source_box: 0
    destination_row: 0

    def __init__(self, color, amount):
        self.type = color
        self.quantity = amount

    def __init__(self, source_box, color, amount):
        self.destination_row = 0
        self.source_box = source_box
        self.type = color
        self.quantity = amount

    def print_tiles(self):
            print("From box: %d, Put into: %d, Color: %s, Amount: %d" % (
                self.source_box, self.destination_row, self.type, self.quantity))
