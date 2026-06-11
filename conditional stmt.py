pwd_correct = True #assigning a boolean value to the variable pwd_correct, which is used to check whether the password is correct or not.
#pwd_correct = False
n = 30


# if pwd_correct:
#     print("Logged in")
#     print("Thank you for logging in!")
# else:
#     print("Incorrect password")
#     print("Try again")

# print(n % 10)  # here this represents whether the n is divisible by 10 or not.

# if n % 10 == 0:
#     print(str(n) + " is a multiple of 10")
# else:
#     print(str(n) + " is not a multiple of 10")

# elif ladder - is a control structure used to check multiple conditions one after another.
# score = 350

# #in this ladder, if  condition is true, then the remaining conditions that are in upcoming lines will not be runned;
# # only if the statement is false, then the next condition will be executed;
# if score >=350:
#     print("India will win")
# elif score >=250:
#     print("India might win")
# elif score >=150:
#     print("Aus might win")
# else:
#     print("Aus will win")

#nested if
#check if the given number is a 3 digit even number
#logical operators - and,or,not

num = int(input("Enter a num: "))
if 99 < num < 1000:
    if num % 2 == 0:
        print(str(num) + " is a 3 digit even number")
else:
    print(str(num) + " is not a 3 digit even number")

name = "Satya"
if name[4] == 'A' or name[4] == 'a':
    print("The name ends with a")


 