# -------------------------------indexing and slicing in string-----------------------------------------

# indexing  - to access a particular character in a string
# indexing is of two types - positive and negative indexing
# positive indexing - to access a particular character in a string
# negative indexing - to access a particular character in a string from the end

x = "peacock is standing"

# print(x[2]) #positive indexing
# print(x[-2]) #negative indexing

"""print(x[0:7])  # slicing - to access a range of characters in a string,where the first number is the starting index and the second number is the ending index (not included)
print(x[:7])
print(x[7:])
print(x[2:19:2]) # slicing with step - to access a range of characters in a string with a specific step, where the first number is the starting index, the second number is the ending index, and the third number is the step (not included)
"""

# print(x[-5:-9])   # str(start : end : step), here the default step is 1, so it will print the characters from index -5 to index -9 with a step of 1, but since the starting index is greater than the ending index, it will return an empty string.so in order to get the desired output we need to change the step to -1, so it will print the characters from index -5 to index -9 with a step of -1, so it will print the characters in reverse order.
# print(x[-5:-9:-1])



