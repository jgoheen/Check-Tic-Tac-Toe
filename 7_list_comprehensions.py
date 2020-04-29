import random
from random import randint


listlena = randint(15,20)
print('list length a:', listlena)

a = []
for i in range(1, listlena):
    a.append(randint(0,100))
print('list a:', a)

even = [i for i in a if i % 2 == 0]
print(even)




