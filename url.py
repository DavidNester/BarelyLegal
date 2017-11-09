class URL:
	time = float()
	date = str()
	keywords = dict()
	visited = bool()
	address = ""

	def __init__(self, time = 0.0, date = "", keywords = {}, visited = False, address = ""):
		self.time = time
		self.date = date
		self.keywords = keywords
		self.visited = visited
		self.address = address

	def toString(self):
		return [self.time, self.date, self.keywords, self.visited, self.address]