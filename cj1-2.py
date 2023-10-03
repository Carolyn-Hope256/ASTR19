#Basic mathematics demo
def main():
	fp1 = 2.7
	fp2 = 0.9
	int1 = 10
	int2 = 9
	sumfp = fp1 + fp2
	print(str(fp1) + " + " + str(fp2) + " = " + str(sumfp))
	print(type(sumfp))
	difint = int1 - int2
	print(str(int1) + " - " + str(int2) + " = " + str(difint))
	print(type(difint))
	prod = int2 * fp2
	print(str(int2) + " * " + str(fp2) + " = " + str(prod))
	print(type(prod))

if __name__ =="__main__":
	main()