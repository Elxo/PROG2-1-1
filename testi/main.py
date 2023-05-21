class Persona:
	def __init__(self, vards, gadi):
		self.vards = vards
		self.gadi = gadi
	def __str__(self):
		return f"{self.vards} ir {self.gadi} gadus vecs"

x = Persona ("Roberts", 17)
print (x) 