class animal:
	def __init__(self, armLen, legLen, eyeNum, hasTail, isFurry):
		self.armLen = float(armLen)
		self.legLen = float(legLen)
		self.eyeNum = int(eyeNum)
		self.hasTail = bool(hasTail)
		self.isFurry = bool(isFurry)

	def printFeatures(self):
		print("Arm length: " + str(self.armLen) + " cm")
		print("\nLeg length: " + str(self.legLen) + " cm")
		print("\nNumber of eyes: " + str(self.eyeNum))
		if(self.hasTail):
			print("\nHas a tail")
		else:
			print("\nDoes not have a tail")

		if(self.isFurry):
			print("\nIs furry\n")
		else:
			print("\nIs not furry\n")
		

def main():
	#Moths have 6 legs so im treating those as arms and legs. also an exact leg length was hard to find so i'm estimating based on a framed DHM i have at home.
	#Also i dont think an abdomen counts as a tail so im putting down false
	DeathsHeadMoth = animal((1.2), (1.2), 2, False, True)

	print("Physical characteristics of the Death's Head Moth!\n")
	DeathsHeadMoth.printFeatures()

if __name__ =="__main__":
	main()