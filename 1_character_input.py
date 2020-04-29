name = input('Enter your name: ')
age = input('Enter your age: ')
number = input('Enter a number: ')
yearwhen100 = (100 - int(age)) + 2020

for x in range(int(number)):
    print('{0}, you will turn 100 in the year {1}'.format(name, yearwhen100))
