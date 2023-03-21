from abc import ABC

class Shape(ABC):
	def __init__(self):
		print("area: " + self.area())
	
	@abstractmethod
	def 
