
def get_integer():
    return int(input("Enter an integer: "))

def check_if_prime(num):
    count=0
    for i in range(1, int(num)+1):
        if ((a % i) == 0):
            count = count + 1
    if count == 2:
        return "prime"


a = get_integer()
status = check_if_prime(a)
if status == "prime":
    print("Prime number")
else:
    print("Not a prime number")

    
    



