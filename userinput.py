#---------------------------------------------taking user input in python--------------------------------------------------

# input() - to take input from the user, it always returns a string. 


name = input("What is your name? ")
print("Hello, " + name.title() + "!")

height = input("what is your height in cm ? ")
print("Your height is " + height + "cm.")

print("Your height in inches is " + str(float(height) / 2.54) + " inches.")
print("Your height in feet is " + str(float(height)/30.8)+ " feet.") 
      
      

