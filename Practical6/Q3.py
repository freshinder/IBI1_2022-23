

# create lists containing the name & cost of the olympic game
# sort the both lists
# output the sorted values for the cost
# create a bar chart using sorted data
# create title, y-axis label, format of the graph

import matplotlib.pyplot as plt
costs = {'Los Angeles 1984':1, 'Seoul 1988':8, 'Barcelona 1992':15, 'Atlanta 1996':7, 'Sydney 2000':5, 'Athens 2003':14, 'Beijing 2008':43, 'London 2012':40}
print(sorted(costs, key=costs.get))
labels = sorted(costs, key=costs.get)
CoO = sorted(costs.values())
print(CoO)
width = 0.5
plt.bar(labels, CoO, width)
plt.xticks(fontsize=8, rotation=25)
plt.ylabel('Cost($ billions)')
plt.title('Olympic Costs')
plt.show()
