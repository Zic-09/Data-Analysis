# Checking for Data Types
int("123")
str(123)
int(10.15)
type(100)
type("you")
type(5.23)
type(True)

# Using the case methods
"hello world".upper()
"hello world".title()
"Hello World".lower()
first_name = "Toluwanimi".upper()
last_name = "Oke".title()
print(f'Full name: {first_name} {last_name}')
word = "Good People".count('o') # Count method
print(word)

# Replace method
"I love yoa".replace('a', 'u')
"Lagos is a Statk".replace('k', 'e')

# Concatenation
message_1 = "Food is good"
message_2 = "and it is required for strength"
print(f' {message_1} {message_2}')

# len function
word = "It is a long way to go"
length = len(word)
print(length)
length_2 = len("Run for your life!")
print(length_2)

# Split method splits a string into a list by a specified delimeter
sentence = "I love to read books often"
print(sentence.split())
print(sentence.split("often"))

# Join method combines a list of strings into a single string
words = ("God", "is", "great")
print(" ".join(words))

# Find method searches for a specified substring within a string and returns the first index of its occurence.
word_1 = "Cleanliness is next to Godliness"
print(word_1.find("is"))
print(word_1.find("go")) # if a substring is not found, it returns -1

# OPERATIONS are are direct actions on data, like getting or modifying parts of it. It doesn’t require a function or method call and works directly with data
# String Operation (indexing) allows you to access an individual character in a string using its respective position. Indexing in Python starts from 0
here = "I love data analysis"
print(here[3])
print(here[-1]) # Negative indexing starts counting from the back

# String Operation (slicing) enables one to get a particular segment of a string, by defining a start index, stop index, and an optional step value
word = "Dubai is one of the most beautiful countries"
print(word[0:5])
print(word[16:34])

# Escape characters are used Escape characters in Python are used to include special characters in strings that would otherwise be difficult to 
# represent, such as quotes, newlines, and backslashes - By using a backslash (\)
new = "I have never been to an Asian continent. I honestly desire strongly to visit an Asian country probably next year by the grace of God.\nWould you like to go with me?"
print(new)
new_1 = "Joy to the world! \tThe Lord is come."
print(new_1)
new_2 = "Joy to the world! \"The Lord is come.\""
print(new_2)

# IN operator is used to check if a specified substring exists in a string. It returns True or False.
lock = "I have been able to read 20 books this year"
print("year" in lock)
print("know" in lock)

# Lists are used to store multiple items in a single variable.
countries = ["United States", "India", "Canada", "Japan", "Botswana"]
print(countries[3]) # list indexing
print(countries[-4]) 
print(countries[1:3]) # list slicing
print(countries[:4]) # slice from beginning to the end
print(countries[3:]) # slice from position 3 to the end

# Adding elements to a list
countries = ["United States", "India", "Canada", "Japan", "Botswana"]
countries.append("Nigeria") # Append method adds another string to the end of the list
print(countries) 
countries.insert(2, "France") # Insert method adds another string to the list by putting it in a specified position
print(countries)

# Joining lists
countries_2 = ["South Africa", "Congo", "Australia", "Dubai"]
print(countries + countries_2) # Using the + sign to join two lists

# Nested list is putting two lists inside another list
nested_list = [countries, countries_2] # It also makes use of square brackets
print(nested_list)

# Removing lists
countries_3 = ["France", "Germany", "Belgium", "Liberia"]
countries_3.remove("Liberia") # remove specifies the exact string you want take out
print(countries_3)
countries.pop(4) # pop takes out a string by using the index
print(countries)
del countries_2[2] # del is also another way to take out a string from a list
print(countries_2)
countries_3.clear() # clear takes out all the strings at once
print(countries_3)

# Sorting lists
numbers = [4, 23, 1, 9, 11, 14, 2, 7, 0, 32, 28]
print("Original number:", numbers)
numbers.sort() # sorts the number in ascending order
print("Sorted numbers(ascending):", numbers)
numbers.sort(reverse=True) # sorts the number in descending order
print("Sorted numbers(descending order):", numbers)

# Updating a list
numbers[2] = 100 # It changes the specified index of the numbers list to 100
print(numbers)

# Copying a list
copied_list = numbers[:] # copies the values in numbers list into copied_list
print(copied_list)
copied_list_2 = numbers.copy() # copying by using the copy method
print(copied_list_2)

# Thank you