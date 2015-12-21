class Musician(object):
	def __init__(self, sounds):
		self.sounds = sounds
		
	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()
		
class Bassist(Musician):
	def __init__(self):
		super().__init__(["Twang", "Thrumb", "Bling"])
		
	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()
		
class Guitarist(Musician):
	def __init__(self):
		super().__init__(["Boink", "Bow", "Boom"])
		
	def tune(self):
		print("Be with you in a moment")
		print("Twoning, sproing, splang")
		
class Bassist(Musician):
	def __init__(self):
		super().__init__(["Bang", "Bong", "Boom", "Clang"])
		
	def solo(self, length):
		for i in range(length):
			print(self.sounds[i % len(self.sounds)], end=" ")
		print()
		
	def count(self):
		
		

david = Bassist()
derek = Guitarist()
nigel = Guitarist()


david.solo(6)
derek.solo(6)
nigel.solo(6)