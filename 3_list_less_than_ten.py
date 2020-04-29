from random import random
from random import seed
from random import randint

a = []
for i in range(1, 49):
    a.append(randint(0,100))
print(a)

for n in range(len(a)):
    if a[n] < 10:
        print(a[n])



