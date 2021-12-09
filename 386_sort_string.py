'''
Given a string, sort it in decreasing order based on the frequency of characters. 
If there are multiple possible solutions, return any of them.
For example, given the string tweet, return tteew. eettw would also be acceptable.
'''

userInput = input("Enter a string: ")
sortedSTR = sorted(userInput)
joinedSortedSTR = ''.join(sortedSTR)
reversedSTR = ''.join(reversed(joinedSortedSTR))
print(reversedSTR)






