#------------------------------------------Data structures-----------------------------------------------

# A data structure is a way of organizing and storing data in a computer so that it can be accessed and modified efficiently. There are many different types of data structures,each with its own advantages and disadvantages. Some common data structures include lists, tuples, sets, dictionaries, stacks, queues, linked lists, trees, and graphs.
# Tuple - is a collection of ordered, immutable, and heterogenous elements. It is defined using parentheses () and the elements are separated by commas. Tuples are similar to lists, but they cannot be modified after they are created. They are often used to group related data together, such as a person's name, age, and address.
# list - is a collection of ordered, mutable, and heterogenous elements. It is defined using square brackets [] and the elements are separated by commas. Lists are similar to tuples, but they can be modified after they are created. They are often used to store a collection of items, such as a list of names or a list of numbers.
# dictionary - is a collection of unordered, mutable, and heterogenous key-value pairs. It is defined using curly braces {} and the key-value pairs are separated by commas. Dictionaries are often used to store data that can be accessed using a unique key, such as a person's name or a product's ID.

#DICTIONARY
# Creating a dictionary
car = {
    "brand": "Tesla",
    "model": "Model S",
    "year": 2024
}

# Accessing values
print(car["brand"])   # Output: Tesla
print(car["year"])    # Output: 2024

# Adding a new key-value pair
car["color"] = "red"

# Updating a value
car["year"] = 2025

# Removing a key-value pair
del car["model"]

print(car)
# Output: {'brand': 'Tesla', 'year': 2025, 'color': 'red'}

#--------------------------------------------------------------------------------------------------------------
#LIST
# Creating a list
cars = ["Tesla", "BMW", "Audi"]

# Accessing values
print(cars[0])   # Output: Tesla
print(cars[2])   # Output: Audi

# Adding new elements
cars.append("Mercedes")        # Add at the end
cars.insert(1, "Toyota")       # Insert at index 1

# Updating values
cars[2] = "Ford"               # Change "BMW" to "Ford"

# Removing elements
cars.remove("Tesla")           # Remove by value
del cars[0]                    # Remove by index
popped_car = cars.pop()        # Remove last element

# Printing final list
print(cars)
# Example Output: ['Toyota', 'Ford']

#----------------------------------------------------------------------------------------------------------------------

#TUPLE
# Creating a tuple
fruits = ("apple", "banana", "cherry")

# Accessing values
print(fruits[0])   # Output: apple
print(fruits[2])   # Output: cherry

# Tuples are immutable, so you cannot directly add/update/remove.
# But you can convert to a list, modify, then convert back.

# Converting to list to modify
fruits_list = list(fruits)

# Adding new elements
fruits_list.append("orange")

# Updating values
fruits_list[1] = "mango"

# Removing elements
fruits_list.remove("apple")

# Converting back to tuple
fruits = tuple(fruits_list)

# Printing final tuple
print(fruits)
# Example Output: ('mango', 'cherry', 'orange')
