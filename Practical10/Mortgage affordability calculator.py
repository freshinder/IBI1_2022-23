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

# Example
print('Please input the value of the house:')
value = int(input())
print('Please input your annual salary:')
salary = int(input())
results = mortgage_affordability_calculator(value, salary)
print(results)
