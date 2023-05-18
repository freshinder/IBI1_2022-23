# let n to be the number of generation, inital generation = first generation
# let r to be the number of rabbits, initial number of rabbits = 2
# repeat
#	number rabbits doubles in every generations
#	generation no. increase 
#	stop repeating until number of rabbits just exceed 100

n = 0
# initial number of generation is 0
r = 2
# initial number of rabbits is 2
while r <= 100:
# repeat the following commands until r (number of rabbits) exceed 100
    n += 1
    # n (number of generation) increase by 1 in each loop
    r = 2 * r
    # r (number of rabbits) double in each generation
print("After", n, "generation, over 100 rabbits have been born.")
