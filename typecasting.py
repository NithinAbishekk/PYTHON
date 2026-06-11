#---------------------------------------------typecasting in python--------------------------------------------------

#typecasting - converting one data type to another data type.
# str() - to convert a data type to a string.
# int() - to convert a data type to an integer.
# float() - to convert a data type to a float.
# type() - to find what type of data a variable is storing.



# otp = 2008
# # print("your otp is " + otp) #this will give an error because we cannot concatenate a string and an integer.
# # so we need to convert the integer otp to a string using the str() function.
# print("your otp is " + str(otp))

# #type method   
# print(type(otp))

# n = 10
# n = str(n)  # we have typecasted the integer number to a string using the str() function.
# print(n)
# print(type(n))


# count = "100"
# print(int(count) + 100)  # we have typecasted the string count to an integer using the int() function and added it to 100.

# x = 5.5
# # print(type(x))  # this will print <class 'float'> because x is a decimal.
# print(int(x) + int("0.5"))

y = '2.3'
print(100+ int(float(y)))

