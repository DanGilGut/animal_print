"""
It's not working for some reason. What's wrong with it?

step = 666
counter += step
print(counter)

"""

step = 666
counter = 10 # esta variable no estaba definida

counter += step
print(counter)

"""
 Python student is trying to write a program that gets two numbers from 
 the user and prints the sum of those numbers. 
 Unfortunately, something is wrong with the code and 
 it doesn't work as expected:
 
 Change the last line to correct the mistake!


first_number = input()
second_number = input()

print(first_number + second_number)

"""

first_number = input()
second_number = input()

print(int(first_number) + int(second_number))