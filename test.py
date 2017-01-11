class Person:
	def __init__(self, name, age, favorite_foods):
	self.name = name
	self.age = age
	self.favorite_foods = favorite_foods
	
	def birth_year(self):
		return 2016 - self.age
	
people = [Person("Ed", 11, ["hotdogs", "jawbreakers"])
	, Person("Edd", 11, ["broccoli"])
	, Person("Eddy", 12, ["chunky puffs", "jawbreakers"])]
	


