"""A good program will make sure that the data its users enter is valid. Write a program that
asks the user for a weight and converts it from kilograms to pounds. Whenever the user
enters a weight below 0, the program should tell them that their entry is invalid and then ask
them again to enter a weight.

[Hint: Use a while loop, not an if statement].

"""

weight = int(input(' Enter weight in Kg : '))
while weight <= 0:
    weight = eval(input('impossible. enter a new weight: '))
print(f' you weight in pounds is {weight /0.45} lb')
