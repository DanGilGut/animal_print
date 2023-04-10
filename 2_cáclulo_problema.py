"""

N squirrels found K nuts and decided to divide them equally.
Determine how many nuts each squirrel will get and print the result.
Input data format:
    There are two positive numbers N and K, each of them is not greater than 10000.

"""
print("Introduce el número de ardillas presentes: ")
N = int(input())
print("...ok, a continuación introduce el número de cacauetes disponibles: ")
K = int(input())

print("...entonces a cada ardilla de tocan {} cacauetes.".format(int(K/N)))
