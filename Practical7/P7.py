import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir ("/cygwin64/home/IBI1_2022-23/Practical7")
covid_data = pd.read_csv('full_data.csv')
#covid_data.describe()
#print(covid_data.loc[2:4,'date'])
#print(covid_data.loc[0:81,'total_cases'])

print(covid_data.iloc[0:1000:100,1])


# extract data of location from the dataframe
# turn the locations into true or false form
# find the results

a = covid_data.iloc[:,1]
L = []
for i in a:
    if i == 'Afghanistan':
        b = True
    else:
        b = False
    L.append(b)
print(covid_data.loc[L,'total_cases'])



count = []
tempstore1 = covid_data.loc[:,'location']
for i in tempstore1:
    if i == 'World':
        b = False
    else:
        b = True
    count.append(b)
data_without_world = covid_data.loc[count,:]
tempstore2 = data_without_world.loc[:,'date']
count = []
for i in tempstore2:
    if i == '2020-03-31':
        b = True
    else:
        b = False
    count.append(b)
new_case = data_without_world.loc[count,'new_cases']
new_death = data_without_world.loc[count,'new_deaths']

print('mean of new deaths is',new_death.mean())
print('mean of new cases is',new_case.mean())
prop = new_death.div(new_case)
print(prop)


value = []
value.append(new_case)
value.append(new_death)
label = ['new_cases', 'new_death']
plt.boxplot(value,labels=label)
plt.ylabel('Number of cases')
plt.title('New cases and new deaths')
plt.show()


a = covid_data.loc[:,'location']
count = []
for i in a:
    if i == 'World':
        b = True
    else:
        b = False
    count.append(b)
world_dates = covid_data.loc[count,'date']
world_new_cases = covid_data.loc[count, 'new_cases']
world_new_deaths = covid_data.loc[count,'new_deaths']
plt.plot(world_dates,world_new_cases,'bo')
plt.plot(world_dates,world_new_deaths,'ro')
plt.ylabel('Number of cases')
plt.title('New cases and new deaths in world')
plt.xticks(world_dates.iloc[0:len(world_dates):4],rotation=-90)
plt.show()

# Answer for question.txt
# How have new cases and total cases developed over time in the UK?

# Extract data about UK using Boolean
# Plot a graph of new cases and total cases using matplotlib
# Correctly labeled them

count = []
a = covid_data.loc[:,'location']
for i in a:
    if i == 'United Kingdom':
        b = True
    else:
        b = False
    count.append(b)
UK_new_cases = covid_data.loc[count,'new_cases']
UK_total_cases = covid_data.loc[count,'total_cases']
UK_date = covid_data.loc[count,'date']
plt.plot(UK_date,UK_new_cases,'ro')
plt.plot(UK_date,UK_total_cases,'bo')
plt.xticks(UK_date.iloc[0:len(UK_date):4], rotation = -90)
plt.title('New cases and total cases in UK')
plt.ylabel('Number of cases')
plt.xlabel('Time')
plt.show()