# '''1. Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.
# Person  Relation
# Darth Vader father
# Leia    sister
# Han brother in law
# R2D2    droid
# Examples
# relation_to_luke("Darth Vader") ➞ "Luke, I am your father."
# relation_to_luke("Leia") ➞ "Luke, I am your sister."
# relation_to_luke("Han") ➞ "Luke, I am your brother in law."'''


# # a=input("write a name >")

# # if a=="Darth Vader":
# #  print("Luke, I am your father.")
# # elif a=="Leia":
# #  print('Luke, I am your sister.')
# # elif a=="Han":
# #  print("Luke, I am your brother in law.")
# # else:
# #  print("droid")


# '''2. Create a function that takes damage and speed (attacks per second) and returns the amount of damage after a given time.
# Examples
# damage(40, 5, "second") ➞ 200
# damage(100, 1, "minute") ➞ 6000
# damage(2, 100, "hour") ➞ 720000
# Notes
# Return "invalid" if damage or speed is negative.'''
# # a,b,c =(2, 100, "hour")

# # if c=="second":
 
# #      print(a*b)

# # elif c=="minute":
# #      print(a*b*60)

# # elif c=="hour":
# #      print(a*b*3600)


# """3. Create a function that takes a list of strings and integers, and filters out the list so that it returns a list of integers only.
# Examples
# filter_list([1, 2, 3, "a", "b", 4]) ➞ [1, 2, 3, 4]
# filter_list(["A", 0, "Edabit", 1729, "Python", "1729"]) ➞ [0, 1729]
# filter_list(["Nothing", "here"]) ➞ []"""

# # lst=([1, 2, 3, "a", "b", 4])
# # lst2=[]
# # for x in lst:
# #     if type(x)==int:
# #      lst2.append(x)
# #      print(lst2)

# """Create a function that takes a number as an argument and returns True or False depending on whether the number is symmetrical or not. A number is symmetrical when it is the same as its reverse.
# Examples
# is_symmetrical(7227) ➞ True
# is_symmetrical(12567) ➞ False
# is_symmetrical(44444444) ➞ True
# is_symmetrical(9939) ➞ False
# is_symmetrical(1112111) ➞ True"""


# #x=str(44)
# # y=x[::-1]
# # if y==x:
# #     print("True")
# # else:
# #     print("False")

# '''5. Create a function that changes all the elements in a list as follows:
# Add 1 to all even integers, nothing to odd integers.
# Concatenates "!" to all strings and make the first letter of the word a capital letter.
# Changes all boolean values to its opposite.
# Examples
# change_types(["a", 12, True]) ➞ ["A!", 13, False]
# change_types([13, "13", "12", "twelve"]) ➞ [13, "13!", "12!", "Twelve!"]
# change_types([False, "False", "true"]) ➞ [True, "False!", "True!"]
# Notes
# There won't be any float values.
# You won't get strings with both numbers and letters in them.
# Although the task may be easy, try keeping your code as clean and as readable as possible!'''

# # x="b"
# # y=x.upper()
# # z=y+ ("!")
# # print(z)


# # x=12
# #  if x%2==0:
# #     print(x+1)
# # else:
# #     print(x)

# # x=False
# # if x==True:
# #   print(False)
# # elif x==False:
# #      print(True)







# '''6. Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.
# See the below examples for a better understanding:
# Examples
# string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]
# string_pairs("edabit") ➞ ["ed", "ab", "it"]
# string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
# Notes
# Return [] if the given string is empty.'''''

# # s=input("input name>")
# # if len(s)%2!=0:
     
# #    s=s+"*"
# #    resalt=(list(s[i:i]+2)  for i in range(0,len(s,2)))

# # print(resalt)


# '''7. Create a function that takes two parameters and, if both parameters are strings, add them as if they were integers or if the two parameters are integers, concatenate them.
# Examples
# stupid_addition(1, 2) ➞ "12"
# -stupid_addition("1", "2") ➞ 3
# stupid_addition("1", 2) ➞ None
# Notes
# If the two parameters are different data types, return None.
# All parameters will either be strings or integers.'''

# # a="1"
# # b=2
# # if type(a)!=type(b):
# #    print("None")
# # elif type(a)==int:
# #      print(str(a)+str(b))
# # elif type(a)==str:
# #      print(int(a)+int(b))



# ''' 9 Check if the given string consists of only letters and spaces and if every letter is in lower case.

# Examples
# letters_only("PYTHON") ➞ False
# letters_only("python") ➞ True
# letters_only("12321313") ➞ False
# letters_only("i have spaces") ➞ True
# letters_only("i have numbers(1-10)") ➞ False
# letters_only("") ➞ False
# Notes
# Empty arguments will always return False.
# Input values will be mixed (symbols, letters, numbers).'''

# # letters_only=("ggggg")
# # for i in letters_only:
# #   if letters_only==(letters_only.isalpha and letters_only.islower ):
# #     print("True")
# # else:
# #     print("False")


# '''10 Write a function that takes a list and determines whether it's strictly increasing, strictly decreasing, or neither.
# Examples
# check([1, 2, 3]) ➞ "increasing"
# check([3, 2, 1]) ➞ "decreasing"
# check([1, 2, 1]) ➞ "neither"
# check([1, 1, 2]) ➞ "neither"
# Notes
# The last example does NOT count as strictly increasing, since 1-indexed 1 is not strictly greater than the 0-indexed 1.
# Input lists have a minimum length of 2.'''


# # x=([1, 1, 2])
# # if x[0]<x[1] and x[1]<x[2]:
# #   print("increasing")
# # elif x[0]>x[1] and x[1]>x[2]:
# #   print("decreasing")
# # else:
# #   print("neither")
