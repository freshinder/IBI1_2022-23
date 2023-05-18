# make a dictionary
# plot a pie chart using matplotlib
# output the number of students who prefer a movie genre (given genre)
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

# output the number of students which the given genre is their favorite
genre = "Comedy" # variable can be modified to output number of students that like other genre
print(Dic["Comedy"])

# number of students who prefer a movie genre input
print('Do you want to find number of students that prefer a specific movie genre, Yes/No')
a = 'Yes'
while a == 'Yes':    # repeat until user doesn't want to continue
       print('Input the movie genre which you want to find about')
       m_genre = input()
       if m_genre == Dic.keys():
              print(Dic[m_genre])
       else:
              print("Wrong input")
       print('Do you still want to go on? Yes/No')
       a = input()
print('Goodbye')