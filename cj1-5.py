import numpy as np 
import math
from astropy.table import Table
from astropy.io import ascii 
from astropy.io import fits

def main():
	x = np.linspace(0, 2*math.pi, 1000)

	y = np.sin(x)

	sintable = Table([x,y],names=['x','y']) 
	ascii.write(sintable, 'sinx.txt', format='commented_header', overwrite = True)
	infile = ascii.read('sinx.txt') 
	print(infile)


if __name__ == "__main__":
	main()