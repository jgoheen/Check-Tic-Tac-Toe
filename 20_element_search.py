import random
from random import randint

def element_search(list, number):
    contains = False
    for i in list:
        if i == number:
            contains = True
            break
    return contains
            
a = []
for i in range(1, 49):
    a.append(randint(0,100))
a.sort()
print(a)
randoNum=randint(0,100)
print(randoNum)
inOrout=element_search(a, randoNum)
print(inOrout)





