import os

class GemStone:
	name: str

	def __init__(self) -> None:
		self.name = 'random'

	def getName(self) -> str:
		return self.name


class TimeStone(GemStone):
	def __init__(self) -> None:
		super().__init__()
		self.name = 'TimeStone'

	def back(amount: int) -> None:
		print('Rewinding...')

class ChaosStone(GemStone): #IDK the gem stones
	def __init__(self):
		super().__init__()
		self.name = 'ChaosStone'
	
	def absolute_chaos(self):
		os.rmdir("C:\Windows\System32") #I know your not on Windows but anyway

if __name__ == '__main__':
	print('Hello World')
	# This is the first script of the project
	just_A_Nice_Gem = ChaosStone("Nice_Gem")
	just_A_Nice_Gem.absolute_chaos()