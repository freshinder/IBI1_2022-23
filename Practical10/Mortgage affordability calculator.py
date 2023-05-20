# write a function called mortgage_affordability_calculator
# ask the user to input the value of house & his annual salary
# store the values in variables, 'value' & 'salary'
# do calculations & comparisons
# output 'Yes' if value is less than 5 times the salary
# if not output 'No'

def mortgage_affordability_calculator(value, salary):
    if value <= 5*salary:
        i = 'Yes'
    else:
        i = 'No'
    return i

# ask user to input the value of house and their salaries
# check if the input is valid
# use the function called to return the decisions made
print('Please input the value of the house:')
value = int(input())
while not isinstance(value,int):
    print("Incorrect input")
    print("Input a correct input")
    value = int(input())
print('Please input your annual salary:')
salary = int(input())
while not isinstance(salary,int):
    print("Incorrect input")
    print("Input a correct input")
    salary = int(input())
results = mortgage_affordability_calculator(value, salary)
print(results)

# Example
value = 100000
salary = 25000
print(mortgage_affordability_calculator(value,salary))