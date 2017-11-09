class URL:
	domain = str()
	date = str()
	keywords = dict()
	visited = bool()
	address = ""

	def __init__(self, domain = "", date = "", keywords = {}, visited = False, address = ""):
		self.domain = domain
		self.date = date
		self.keywords = keywords
		self.visited = visited
		self.address = address

	def toString(self):
		return [self.domain, self.date, self.keywords, self.visited, self.address]