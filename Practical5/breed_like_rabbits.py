# let n to be the number of generation, inital generation = first generation
# let r to be the number of rabbits, initial number of rabbits = 2
# repeat
#	number rabbits doubles in every generations
#	generation no. increase 
#	stop repeating until number of rabbits just exceed 100

n=0
r=2
while r <= 100:
	n += 1
	r=2*r
print(n)
