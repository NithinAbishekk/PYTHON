# diamond pattern generation using loop
n = 5
# for i in range(1, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))
# for i in range(n - 1, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# for i in range(1,10):
#     print("*" * i)
# for i in range(10,1,-1):
#     print("*" * i)

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n-1,0,-1):
    print(" " * (n - i) + "*" * (2 * i - 1))

for i in range(1,6): #rows 1 to 5
    for j in range(1,i+1): #columns 1 to i+1
        print(j, end = '') #end='' is used to print the numbers in the same line without adding a new line after each print statement, so that the numbers will be printed in a pattern of increasing numbers in each row.
    print()# this is used to print a new line after each row of numbers, so that the next row of numbers will be printed on a new line.
