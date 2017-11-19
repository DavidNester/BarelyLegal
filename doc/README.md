# Developer Documentation Guidelines - Job Scraper
Software Engineering Class 2017 @ EMU

## Naming conventions

All **function names** should be descriptive. All functions names are lowercase and words are seperated by underscores. Parameters are also lowercase and underscore seperated.

Example:
```
def distance_between_two_points(point_1, point_2):
	...
	return ...
``` 

All **variables** should be descriptive, lowercase, and underscore seperated. Use CAPITALS to specify constants and make the names as descriptive as reasonably possible. "Magic numbers" should not be used.

Example:
```
PI = 3.14159
radius = 2
area_of_circle = PI * radius ** 2
``` 

**Class names** should begin with a capital and generally should be one word. Accessor and mutator methods should be lowercase and underscore seperated.

Example:
```
class Person:
	""" A single human being"""
	def __init__(self):
		"""Instantiate a new person with default values"""
		self.height = 0
		...

	def set_height(self, height):
		"""
		Sets the height of the person.
		Returns void.
		"""
		self.height = height

``` 

## Comments

All **function declarations** should be followed by a docstring which describes the function, its parameters, and its return value.

Example:
```
def distance_between_two_points(point_1, point_2):
	"""
	Finds the distance between two points.
	point_1 - the first point as a tuple (x1,y1)
	point_2 - the second point as a tuple (x2, y2)
	Returns the distance as a floating point number.
	"""
	x1, y1 = point_1
	x2, y2 = point_2
	return ((x1-x2)**2 + (y1-y2) **2)**.5
``` 

All **in-line comments** should start with a space (for readability) and may follow the code if the line is not too long.

Example:
```
X_OFFSET = 10
my_point = [15, 25]

my_point[0] += X_OFFSET # Increase the x-value of my_point
``` 


All other [PEP-8](https://www.python.org/dev/peps/pep-0008/) style guidelines should be followed.