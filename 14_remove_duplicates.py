import random
from random import randint

def remove_duplicates(a):
    new_set = set(a)
    return new_set

listlena = 10

a=[]
for i in range(1,listlena):
    a.append(random.randint(1, 9))
print('list a:', a)

new_list = remove_duplicates(a)
new_list = list(new_list)
print("new list: ", new_list)