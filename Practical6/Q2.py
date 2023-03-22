# make a dictionary
# plot a pie chart using matplotlib
# output the number of students who prefer a movie genre
# if user wants to find number of student who prefer a movie genre
# repeat
#      output the corresponding value of a movie genre
# until user doesn't want to continue

# setting up a dictionary
Dic = {"Comedy": 73, "Action": 42, "Romance": 38, "Fantasy": 28, "Science-fiction": 22, "Horror": 19, "Crime": 18,
       "Documentary": 12, "History": 8, "War": 7}

# pie chart
import matplotlib.pyplot as plt
labels = Dic.keys()
sizes = Dic.values()
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.1f%%')
plt.show()

# number of students who prefer a movie genre input
print('Do you want to find number of students that prefer a specific movie genre, Yes/No')
a = input()
while a == 'Yes':    # repeat until user doesn't want to continue
       print('Input the movie genre')
       m_genre = input()
       print(Dic[m_genre])
       print('Do you still want to go on? Yes/No')
       a = input()
print('Goodbye')