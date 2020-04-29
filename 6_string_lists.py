def reverse(s):
    return s[::-1]

inputstr = input("Enter a string: ")
print(inputstr)

answer = reverse(inputstr)

if (inputstr == answer):
    print('Palindrom')
else:
    print('not a Palindrom')