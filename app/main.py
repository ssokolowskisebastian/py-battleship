class Deck:
    def __init__(self, row, column, is_alive=True):
        self.row = row
        self.column = column
        self.is_alive = is_alive


class Ship:
    def __init__(self, start, end, is_drowned=False):
        self.is_drowned = is_drowned
        self.decks = []

        r1, c1 = start
        r2, c2 = end

        if r1 == r2:
            for c in range(min(c1, c2), max(c1, c2) + 1):
                self.decks.append(Deck(r1, c))
        else:
            for r in range(min(r1, r2), max(r1, r2) + 1):
                self.decks.append(Deck(r, c1))

    def get_deck(self, row, column):
        for deck in self.decks:
            if deck.row == row and deck.column == column:
                return deck
        return None

    def fire(self, row, column):
        deck = self.get_deck(row, column)
        if deck is None or not deck.is_alive:
            return

        deck.is_alive = False

        if all(not d.is_alive for d in self.decks):
            self.is_drowned = True


class Battleship:
    def __init__(self, ships):
        self.field = {}

        for start, end in ships:
            ship = Ship(start, end)

            for deck in ship.decks:
                self.field[(deck.row, deck.column)] = ship

    def fire(self, location: tuple):

        if location not in self.field:
            return "Miss!"

        row, column = location
        ship = self.field[location]
        deck = ship.get_deck(row, column)

        if deck is None or not deck.is_alive:
            return "Miss!"

        ship.fire(row, column)

        if ship.is_drowned:
            return "Sunk!"
        return "Hit!"
