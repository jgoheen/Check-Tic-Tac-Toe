import random
from random import randint


listlena = randint(15,20)
listlenb = randint(15,20)
print('list length a:', listlena)
print('list length b:', listlenb)

#a = []
#for i in range(1, listlena):
#    a.append(randint(0,100))
#print('list a:', a)
a=[]
b=[]
a = random.sample(range(1,30), listlena)
b = random.sample(range(1,30), listlenb)
print('list a:', a)
print('list b:', b)


#b = []
#for i in range(1, listlenb):
#    b.append(randint(0,100))
#print('list b:', b)

c = [value for value in a if value in b]
print('list c:', c)




