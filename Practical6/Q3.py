# create a list containing the cost
import matplotlib.pyplot as plt

costs = [1,8,15,7,5,14,43,40]
costs.sort()
for i in costs: # repeat for all value in sorted costs
    print(i)

# plot a barchart using matplotlib
# y axis label is 'Cost ($ billions)'
# title is 'Olympic Costs'

labels = ['Los Angeles 1984','Seoul 1988','Barcelona 1992','Atlanta 1996','Sydney 2000','Athens 2003','Beijing 2008','London 2012']
cost = [1,8,15,7,5,14,43,40]
width = 0.5
#fig, ax = plt.subplots()
plt.figure(figsize=(12,4))  # size of the figure produced (x,y)
plt.bar(labels,cost,width)
plt.ylabel('Cost ($ billions)')  # name y axis
plt.xticks(fontsize = 8, rotation = 25) # rotation by 25 degree & customize fontsize
plt.title('Olympic Costs')   # name title
plt.show()