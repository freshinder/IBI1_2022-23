# let n equal to the nth hexagonal
# let h to be the number of dots required to make up hexagons with formula h=2n*(2n-1)
# repeat:
#	use n = 1, 2, 3, 4, 5
#	calculate h using 
#	print h

for n in range (1,6):
	h = n*(2*n-1)
	print(n,":",h)