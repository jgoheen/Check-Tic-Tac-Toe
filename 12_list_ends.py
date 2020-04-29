import random
from random import randint

listlena = randint(15,20)
print('list length a:', listlena)

a=[]
a = random.sample(range(1,30), listlena)
print('list a:', a)

b = [a[0], a[listlena-1]]
print('list b:', b)





