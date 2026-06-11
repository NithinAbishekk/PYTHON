#-------------------------------FUNCTIONS----------------------------------------------------......................

#parameter - is a variable listed inside the parentheses of a function's definition
#argument - is the actual value sent to the function when it is called. The number of arguments in a function call should match the number of parameters in the function definition. If there are more or fewer arguments than parameters, it will result in a TypeError.


# def greet(name):  # define a function called greet that takes one parameter, name
#     print("Hello " + name)
#     print("How are you?")
# greet("Alice")  # passing argument
# greet("Bob")  # call the greet function with the argument "Bob"


# def greet(fname,lname):
#     '''takes a string name as input.Says hello  + name ''' #docstring - describes what the function does
#     print("Hello " + fname + ' ' + lname)
#     print("How are you?")
# fname, lname = "Robert" , "Hooke"
# greet(fname, lname)


# def greet(fname,lname):
#     '''takes a string name as input.Says hello  + name ''' #docstring - describes what the function does
#     print("Hello " + fname + ' ' + lname)
#     print("How are you?")
# greet(fname = 'Ram', lname = 'Sharma')
# greet(lname = 'Shetty', fname = 'Lakshman') # keyword arguments - order of the arguments does not matter when you use keyword arguments.


# sum of n natural numbers.
# def sum(n):
#     """find the sum of n natural numbers"""
#     sum_result = n * (n + 1) / 2
#     return sum_result
# result = sum(20)
# print(result)


# --------------------------------------VARIABLE SCOPE-------------------------------------------


# variable scope - the region of the program where a variable is defined and can be accessed
# global variable - a variable that is defined outside of any function and can be accessed anywhere in the program
# local variable - a variable that is defined inside a function and can only be accessed within that function
# In the example below, the variable 'message' is a local variable defined inside the 'welcome' function. It cannot be accessed outside of that function, which is why the last line will raise a NameError.

# def welcome():
#     message = "Hi"
#     print(message)
# welcome()
# #print(message) --> NameError: name 'message' is not defined because messsage is a local variable and cannot be accessed


# num = 10  # global variable
# def welcome(name):  # name - parameter
#     global num
#     num = 20
#     print("Welcome, " + name)
#     print(str(num))
# welcome("Nithin")
# print("The value of num is " + str(num))
# while num <= 100:
#     print(num)
#     num += 10



#-----------------------------------------VARIABLE LENGTH ARGUMENTS---------------------------------------------
#variable length arguments - allows a function to accept an arbitrary number of arguments. There are two types of variable length arguments: *args and *kwargs.
#*args - allows a function to accept any number of positional arguments. The arguments are passed as a tuple to the function.
#*kwargs - allows a function to accept any number of keyword arguments. The arguments are passed as a dictionary to the function.

#sum of numbers
# def total(n1,n2,n3):
#     sum_result =  n1+n2+n3
#     return sum_result

# print(total(4,5,9))



#sum of numbers by variable length argument
# def total(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum
# print(total(1,2,3,4,5,6,7,8,9,0))


# def print_addr(**kwargs):
#     for key,val in kwargs.items():
#         print(val)

# print_addr(door_no = "213",Road_name = 'veppadai road',town = 'pallipalayam',pincode = '638008')


#------------------------------------Default arguments -------------------------------------------------------

#default arguments - allows a function to have default values for parameters. If the caller does not provide a value for a parameter, the default value is used.
# def greet(name = "Guest"):
#     print("Hello " + name)
#     print("How are you?")
# greet()#will use the default value "Guest"
# greet("Alice")#will use the provided value "Alice"


#----------------------------------Passing list -----------------------------------------------------------------

#passing list as an argument to a function


#passing list
# def print_list(items): #here the parameter is items which is a list, we can pass any list to this function and it will print the items in the list. There is no any necessity exact name of the list, thus we can use any name for the parameter, it is just a convention to use items or lst or something similar to indicate that it is a list.
#     for i in items:
#         print(i.title())
# names = ['Nithin','kavi','shanjeev','rohit','aslam']
# print_list(names)



# def print_list(items): 
#     for i in range(0, len(items)):
#         items[i] = items[i].title()
#         print(items[i])

# names = ['Nithin','kavi','shanjeev','rohit','aslam']
# print_list(names[:])
# print(names)


#-----------------------------------------------------Returning dictionary -----------------------------------------------------

#returning dictionary - a function can return a dictionary, which is a collection of key-value pairs. The keys are unique and the values can be of any data type. A dictionary is defined using curly braces {} and the key-value pairs are separated by commas.    

