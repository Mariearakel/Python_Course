# """1 Create methods for the Calculator class that can do the following:

# Add two numbers.
# Subtract two numbers.
# Multiply two numbers.
# Divide two numbers."""

# class Calculator:
#     def add(self, a, b):
#         return a+b
#     def subtract(self, a, b):
#         return a-b
#     def multiply(self, a, b):
#         return a*b 
#     def divide(self, a, b):
#         return a//b
    
# calculator = Calculator()

# print(calculator.add(10, 5))

# print(calculator.subtract(10, 5))

# print(calculator.multiply(10, 5))

# print(calculator.divide(10, 5))

# """2 Given an int, figure out how many ones, threes and nines you could fit into the number. You must create a class. You will make variables (self.ones, self.threes, self.nines) to do this.

# """

# class Ones_threes_nines:
#     def nines(self, a):
#         if a<9:
#             return 0
#         else:
#             return a%9
#     def ones(self,a):
#         if a<1:
#             return 0
#         else : 
#            return a//1
#     def threes(self, a):
#         if a<3:
#             return 0
#         else:
#             return a//3
 

# n1 = Ones_threes_nines()

# print(n1.nines(5))

# print(n1.ones(5))

# print(n1.threes(5))


# """ 3 Create a class that takes the following four arguments for a particular football player:

# name
# age
# height
# weight
# Also, create three functions for the class that returns the following strings:

# get_age() returns "name is age age"
# get_height() returns "name is heightcm"
# get_weight() returns "name weighs weightkg"
# """
# class Player:
#     def __init__(self, name:str="Davit Jones", age:int=25, height:int=175, weight:int=75):
 
#        self.name=name 
#        self.age=age
#        self.height=height
#        self.weight=weight
#     def get_age(self):
#        return f"{self.name} is age {self.age}"
#     def get_height(self):
#          return f"{self.name} is {self.height}cm"
#     def get_weight(self):
#         return f"{self.name} weighs {self.weight}kg"


# p1 = Player()

# print(p1.get_age())             
# print(p1.get_height())        
# print(p1.get_weight())            


# """" 4 reate the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase."""

# class Employee:
#     def __init__(self, name ,surname ):
#         self.name=name
#         self.surname=surname 
#     def fullname(self):
#         return f"{self.name} {self.surname}"
#     def email(self):
#        return f"{self.name.lower()}.{self.surname.lower()}@compny.com"
#     def firstname(self):
#         return self.name
    
# emp_1 = Employee("John", "Smith")
# emp_2 = Employee("Mary",  "Sue")
# emp_3 = Employee("Antony", "Walker")
# print(emp_1.fullname())

# print(emp_2.email())

# print(emp_3.firstname())


# """ 5 Create a class named User and create a way to check the number of users (number of instances) that were created, so that the value can be accessed as a class attribute.

# """



# class User:
#     user_count = 0

#     def __init__(self, username):
#         self.username = username
#         User.user_count += 1


# u1 = User("johnsmith10")
# print(User.user_count)  # Output: 1
# print(u1.username)  # Output: "johnsmith10"

# u2 = User("marysue1989")
# print(User.user_count)  # Output: 2
# print(u2.username)  # Output: "marysue1989"

# u3 = User("milan_rodrick")
# print(User.user_count)  # Output: 3
# print(u3.username)  # Output: "milan_rodrick"

# u4= User("gggg")
# print(User.user_count)
# print(u4.username)

# """ 6 Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

# An attribute called fullname which returns the first and last names.
# An attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
# Remember to allow the attributes fname and lname to be accessed individually as well.

# """
# class Name:
#     def __init__(self,name1,name2):
#         self.name1=name1
#         self.name2=name2
#     def fname(self):
#         return f"{self.name1.capitalize()}"
#     def lname(self):
#         return f"{self.name2.capitalize()}"
#     def fullname(self):
#         return f"{self.name1.capitalize()}  {self.name2.capitalize()}"
#     def initials(self):
#         return f"{self.name1.capitalize()[0]}.{self.name2.capitalize()[0]}"

# a1 = Name("john", "SMITH")
# print(a1.fname())

# print(a1.lname())

# print(a1.fullname())

# print(a1.initials())

# """ 7 Write a Composer class that has three instance variables:

# name
# dob
# country
# Add an additional class variable .count which counts the total number of instances created.
#    user_count = 0

#     def __init__(self, username):
#         self.username = username
#         User.user_count += 1

# """
# class Composer:
#     count=0
#     def __init__(self, name, dob, country):
    
#        self.name=name
#        self.dob=dob
#        self.country=country
#        Composer.count+=1


# print(Composer.count)

# c1 = Composer("Ludvig van Beethoven", 1770, "Germany")
# print(Composer.count)  

# c2 = Composer("Wolfgang Amadeus Mozart", 1756, "Austria")
# c3 = Composer("Johannes Brahms", 1833, "Germany")
# print(Composer.count)

# """ 8 Create a Book class that has two attributes:

# .title
# .author
# and two methods:

# A method named .get_title() that returns: "Title: " + the instance title.
# A method named .get_author() that returns: "Author: " + the instance author.
# and instantiate this class by creating 3 new books:

# Pride and Prejudice - Jane Austen (PP)
# Hamlet - William Shakespeare (H)
# War and Peace - Leo Tolstoy (WP)
# The name of the new instances should be PP, H, and WP, respectively.

# For instance, if I instantiated the following book using this Book class:

# Harry Potter - J.K. Rowling (HP)
# I would get the following attributes and methods:

# """
# class Book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     def get_title(self):
#         return f"Title:{self.title}"
#     def get_author(self):
#         return f"Autor:{self.author}"
    
# HP=Book("Harry Potter","J.K. Rowling")
# PP=Book("Pride and Prejudice","Jane Austen")
# H=Book("Hamlet","William Shakespeare")
# WP=("War and Peace","Leo Tolstoy")

# print(HP.title )
# print(HP.author)
# print(HP.get_title())
# print(HP.get_author()) 

# """9 Create a Person class which will have three properties:

# Name
# List of foods they like
# List of foods they hate
# In this class, create the method taste():

# It will take in a food name as a string.
# Return {person_name} eats the {food_name}.
# If the food is in the person's like list, add 'and loves it!' to the end.
# If it is in the person's hate list, add 'and hates it!' to the end.
# If it is in neither list, simply add an exclamation mark to the end."""

# class Person:
#     def __init__(self, name, likes, hates):
#         self.name = name
#         self.likes = likes
#         self.hates = hates

#     def taste(self,food_name):
#         if food_name in self.likes:
#             return f"{self.name} eats the {food_name} and loves it!"
#         elif food_name in self.hates:
#             return f"{self.name} eats the {food_name} and hates it!"
#         else:
#             return f"{self.name} eats the {food_name}!"

# p1 = Person("Sam", ["ice cream"], ["carrot"])


# print(p1.taste("ice cream"))

# print(p1.taste("carrot")) 

# print(p1.taste("apple"))

# """10  A country can be said as being big if it is:

# Big in terms of population.
# Big in terms of area.
# Add to the Country class so that it contains the attribute is_big. Set it to True if either criterea are met:

# Population is greater than 250 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:"""

# class Country:
#     def __init__(self, name, population, area):
#         self.name = name
#         self.population = population
#         self.area = area
#         self.is_big = self.population > 250000000 or self.area > 3000000
    
#     def compare_pd(self, other_country):
#         if self.population / self.area > other_country.population / other_country.area:
#             return f"{self.name} has a larger population density than {other_country.name}."
#         elif self.population / self.area < other_country.population / other_country.area:
#             return f"{self.name} has a smaller population density than {other_country.name}."
#         else:
#             return f"{self.name} has the same population density as {other_country.name}."


# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)

# print(australia.is_big)  # Output: True
# print(andorra.is_big)  # Output: False

# print(andorra.compare_pd(australia)) 

# HARD 
'''Create a class with a few functions like these examples.

magic.replace("string", 'char', char') is a function that replaces all of the specified characters with different specified characters.
magic.str_length("string") is a function that returns the length of the string.
magic.trim(" string ") is a function that returns a string with truncated spaces at both the beginning and end.
magic.list_slice(list, tuple) is a function that returns the items in the list that are between the specified indexes. If the length of the new list is 0, return -1.'''

class Magic:
  
    def replace(string, old_char, new_char):
        return string.replace(old_char,new_char)
    
    def str_length(string):
        return len(string)
    
    def trim(string):
        return string.strip()
    
    def list_slice(lst, indexes):
        start, end = indexes
        new_list = lst[start:end]
        if len(new_list) == 0:
            return -1
        return new_list

print(Magic.replace("AzErty-QwErty", "E", "e"))  # Output: "Azerty-Qwerty"

print(Magic.str_length("hello world"))  # Output: 11

print(Magic.trim("      python is awesome      "))  # Output: "python is awesome"

print(Magic.list_slice([1, 2, 3, 4,5], (1, 4)))  # Output: [2, 3, 4]
 

"""Given an integer between 0 and 26, make a variable (self.answer). That variable would be assigned to a string in this format:

"nines:your answer, threes:your answer, ones:your answer"
You need to find out how many ones, threes, and nines it would at least take for the number of each to add up to the given integer when multiplied by one, three or nine (depends)."""
def calculate_counts(n):
    # Calculate the number of nines
    num_nines = n // 9

    # Calculate the remaining value after subtracting the nines
    remaining_value = n % 9

    # Calculate the number of threes
    num_threes = remaining_value // 3

    # Calculate the number of ones
    num_ones = remaining_value % 3

    # Construct the result string
    result = f"nines:{num_nines}, threes:{num_threes}, ones:{num_ones}"

    return result

# Example usage:
given_integer = 17
answer = calculate_counts(given_integer)
print(answer)

"""   Employee Parsing
In the class Employee, implement the instance attributes as firstname, lastname and salary.

Create the method from_string() which parses a string containing these attributes and assigns them to the correct properties. Properties will be separated by a dash."""           

class Employee:
    def __init__(self,firstname, lastname,salary):
        self.firstname=firstname
        self.lastname=lastname
        self.salary=salary

    @classmethod
    def from_string(cls, employee_string):
        firstname, lastname, salary = employee_string.split("-")
        return cls(firstname, lastname, int(salary))


emp1 = Employee("Mary", "Sue", 60000)
emp2 = Employee.from_string("John-Smith-55000")

print(emp1.firstname)

print(emp1.salary)
print(emp2.firstname)
print(emp2.salary)


class Memory:
    def __init__(self):
        self.memories = {}

    def add(self, **kwargs):
        self.memories.update(kwargs)

    def remember(self, key):
        return self.memories.get(key, False)


memories = Memory()

memories.add(name="Shane", gender="M", catch_phrase="bazinga")
memories.add(work="None", love_life=0)
memories.add(address="car")

print(memories.remember("love_life"))  # Output: None
print(memories.remember("address"))  # Output: M
print(memories.remember("lover"))  # Output: False

class Employee:
    def __init__(self,name, lastname, **kwargs ):
        self.name=name
        self.lastname=lastname
        self.kwargs=kwargs


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")

print(john.name)
# print(mary.lastname)
# print(richard.height)
# print(giancarlo.nationality)