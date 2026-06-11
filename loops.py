# loops - repeat a block of code multiple times
# for loop - is a control structure used to repeat a block of code a specific number of times.
# while loop - is a control structure used to repeat a block of code as long as a specific condition is true.


#for loop
#print the numbers from 1 to 10 using for-loop
for i in range(1, 11):
    print(i)
else:
     print("Loop is over") # the else block will be executed when the loop is over, which means that the loop has iterated through all the numbers in the range and the condition of the for loop is no longer true.


## while loop
##print the numbers from 1 to 10 using while loop
# print("\n")
i = 1
while i <= 10:
    print(i)
    i += 1  # this is the same as i = i + 1, which is used to increment the value of i by 1 in each iteration of the loop, so that the loop will eventually terminate when i become greater than 10.
else:
    print(
        "Loop is over"
    )  # the else block will be executed when the loop is over, which means that the condition of the while loop is no longer true.


# to print the square numbers from list of numbers using for loop
numbers = [1,2,3,4,5]
for x in numbers:
     print(x**2) #x*x can also be used to calculat the square of x, but using x**2 is more concise and easier to read.

# to print the cubes of numbers from list of numbers using for loop
even_nos = [2,4,6,8,10]
for i in even_nos:
    #print(i*i*i)
    print(i**3)


# #guess the number game using while loop
import random
number = random.randint(1,10)
guess = int(input("Guess the number between 1 and 10:"))

while guess != number:
    if guess < number:
        print("Your guess is too low, try again.")
        guess = int(input("Guess again: "))

    else:
        print("Your guess is too high, try again.")
        guess = int(input("Guess again: "))

print("Congratulations! You guessed the number " + str(number) + " correctly!")


# pattern generation using loop
n  = 5 # no. of rows
for i in range(1, n+1):
  print("*" * i) # this will print the pattern of stars, where the number of stars in each row is equal to the row number, so in the first row it will print 1 star, in the second row it will print 2 stars, and so on until it reaches n rows.

for i in range(10,1,-1):
   print("@" * i)

# #nested loops - a loop inside another loop
for i in range(1,4):
    for j in range(1,6):
        print(j, end="")
    print("")

# get a list of numbers from user and update as list
print("Enter list of numbers,Enter z to exit. ")
number = []
while True:
    inp = input()
    if inp == 'z':
        break
    else:
        number.append(int(inp))

print("The list of numbers you entered is: ",number)


# remove comma from a string
text = "A,B,C,D,E"
text2 = "" 
for i in text:  #seperate each character in the string and check if it is a comma or not, if it is a comma then skip it and if it is not a comma then add it to the new string text2.
    if i == ",":
        pass
    else:
        text2 = text2 + i
print(text2)
