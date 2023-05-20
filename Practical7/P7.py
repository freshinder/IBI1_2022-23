# import python libraries
# read file 'full_data.csv'


# import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

os.chdir("/cygwin64/home/IBI1_2022-23/Practical7")
print(os.getcwd())
print(os.listdir())

# read file
covid_data = pd.read_csv('full_data.csv')

# covid_data.describe()
#   the mean of new cases is 194.546773
#   the standard deviation of new cases is 2083.395028
#   the maximum is 65162, minimum is -9
#   the range is 65171
# print(covid_data.loc[2:4,'date'])
# print(covid_data.loc[0:81,'total_cases'])

# output the second column from every 100th row from the first 100 rows
print(covid_data.iloc[0:1001:100, 1])

# extract data of location from the dataframe
# turn the locations into true or false form
# find the results

location = covid_data.iloc[:, 1]
L = []
for i in location:
    if i == 'Afghanistan':
        a = True
    else:
        a = False
    L.append(a)
print(covid_data.loc[L, 'total_cases'])

# find the mean number of new cases and new deaths on 31 March 2020
# remove the data of 'world'
# select rows that has '2020-03-31'  in the 'date' column
# extract data of new cases and new deaths from the selected rows
count = []
tempstore1 = covid_data.loc[:, 'location']
for i in tempstore1:
    if i == 'World':
        b = False
    else:
        b = True
    count.append(b)
data_without_world = covid_data.loc[count, :]
tempstore2 = data_without_world.loc[:, 'date']
count = []
for i in tempstore2:
    if i == '2020-03-31':
        b = True
    else:
        b = False
    count.append(b)
new_case = data_without_world.loc[count, 'new_cases']
new_death = data_without_world.loc[count, 'new_deaths']
# use numpy to find the mean
m_new_case = np.mean(new_case)
m_new_death = np.mean(new_death)
print('mean of new deaths is', m_new_death)
print('mean of new cases is', m_new_case)
prop = np.divide(m_new_death,m_new_case)
print('the proportion of new deaths as a proportion of new cases is',prop)


# plotting boxplot of new cases and new deaths
value = []
value.append(new_case)
value.append(new_death)
label = ['new_cases', 'new_death']
plt.boxplot(value, labels=label)
plt.ylabel('Number of cases')
plt.title('New cases and new deaths')
plt.show()


# plot another graph of new cases and new deaths in the world
# select rows that has value 'World' in the column 'location'
# extract the data, new cases and new deaths from the selected rows
# plot a graph
# label the graph
a = covid_data.loc[:, 'location']
count = []
for i in a:
    if i == 'World':
        b = True
    else:
        b = False
    count.append(b)
world_dates = covid_data.loc[count, 'date']
world_new_cases = covid_data.loc[count, 'new_cases']
world_new_deaths = covid_data.loc[count, 'new_deaths']
plt.plot(world_dates, world_new_cases, 'bo')
plt.plot(world_dates, world_new_deaths, 'ro')
plt.ylabel('Number of cases')
plt.title('New cases and new deaths in the world')
plt.xticks(world_dates.iloc[0:len(world_dates):5], rotation=-90)
plt.show()

# Answer for question.txt
# How have new cases and total cases developed over time in the UK?

# Extract data about UK using Boolean
# Plot a graph of new cases and total cases using matplotlib
# Correctly labeled them

count = []
a = covid_data.loc[:, 'location']
for i in a:
    if i == 'United Kingdom':
        b = True
    else:
        b = False
    count.append(b)
UK_new_cases = covid_data.loc[count, 'new_cases']
UK_total_cases = covid_data.loc[count, 'total_cases']
UK_date = covid_data.loc[count, 'date']
plt.plot(UK_date, UK_new_cases, 'ro')
plt.plot(UK_date, UK_total_cases, 'bo')
plt.xticks(UK_date.iloc[0:len(UK_date):4], rotation=-90)
plt.title('New cases and total cases in UK')
plt.ylabel('Number of cases')
plt.xlabel('Time')
plt.show()
