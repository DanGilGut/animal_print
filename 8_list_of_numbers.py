"""
how many numbers were given until 55
their sum
their average: sum / the number of given numbers

"""

# put your code here
number = int(input())
list_numbers = []

while number != 55:
    list_numbers.append(number)
    number = int(input())

sum_numbers = 0
count = 0
for number in list_numbers:
    sum_numbers = list_numbers[count] + sum_numbers
    count = count + 1

print(count)
print(sum_numbers)
print(round(sum_numbers / count))
