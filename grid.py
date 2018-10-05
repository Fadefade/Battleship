WATER_CHAR = " "
SHIP_CHAR = "■"
HIT_SHIP_CHAR = "□"
HIT_CHAR = "X"
MISS_CHAR = "O"

class Cell:
	def __init__(self, raw, column):
		self.fired = False
		self.raw = raw
		self.column = column

class Ship:
	def __init__(self, name, size):
		self.name = name
		self.size = size
		self.cells = []

class Grid:
	def __init__(self, size = 10):
		self.ships = {}
		self.size = size
		self.ships["Carrier"] = Ship("Carrier", 5)
		self.ships["Battleship"] = Ship("Battleship", 4)
		self.ships["Cruiser"] = Ship("Cruiser", 3)
		self.ships["Submarine"] = Ship("Submarine", 3)
		self.ships["Destroyer"] = Ship("Destroyer", 2)

		self.grid = []
		for i in range(size):
			self.grid.append([])
			for j in range(size):
				self.grid[i].append(Cell(i, j))

	def display_grids(self, other_grid):
		print("     1   2   3   4   5   6   7   8   9   10||"\
			+ "     1   2   3   4   5   6   7   8   9   10")
		for raw in range(10):
			letter = chr(65 + raw)
			print(letter + "  ", end = "")
			for column in range(10):
				print("| ", end = "")
				if not other_grid.grid[raw][column].fired:
					print(WATER_CHAR + " ", end = "")
				elif other_grid.ship_presence(raw, column):
					print(HIT_CHAR + " ", end = "")
				else:
					print(MISS_CHAR + " ", end = "")
			print("||", end = "")
			print(letter + "  ", end = "")
			for column in range(10):
				print("| ", end = "")
				if not self.ship_presence(raw, column):
					print(WATER_CHAR + " ", end = "")
				elif self.grid[raw, column].fired:
					print(HIT_SHIP_CHAR + " ", end = "")
				else:
					print(SHIP_CHAR + " ", end = "")
			print("")

	def ship_presence(self, raw, column):
		return False
