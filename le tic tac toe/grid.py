#creation de la classe qui gere la grille

class Grid:
	def __init__(self):
		self.clearGrid()

	def clearGrid(self):
		self.grid = [["" for i in range(3)] for i in range(3)]

	def win(self):
		for i in range(3):
			if (self.grid[0][i] == self.grid[1][i] == self.grid[2][i]) and self.grid[0][i] != "":
				return (True,"r"+str(i))
			if (self.grid[i][0] == self.grid[i][1] == self.grid[i][2]) and self.grid[i][0] != "":
					return (True,"c"+str(i))
		if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[1][1] != "":
			return (True,"d0")
		elif self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] != "": 
			return (True,"d1")
		return False,(None,None)
		
	def fullGrid(self):
		for i in range(3):
			for o in range(3):
				if self.grid[i][o] == '':
					return False
		return True

	
	



