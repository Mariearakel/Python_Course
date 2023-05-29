"""  1 Write a function that takes a string name and a number num (either 0 or 1) and return 
"Hello" + name if num is 1, otherwise return "Bye" + name."""

# def say_hella_bye(a:str,b:int):
#    if b==1:
#       return f"Hello {a.capitalize()}"
#    elif b==0:
#       return f"Bye {a.capitalize()}"
#    else:
#       return("wrong number")
   
# print(say_hella_bye("tomy",1))
# print(say_hella_bye("Alan",0))
# print(say_hella_bye("mary",1))




"""  2  Create a function that takes a list (slot machine outcome) and returns True if all 
elements in the list are identical, and False otherwise. The list will contain 4 elements.

Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False"""


def test_jackpot(a:str,b:str,c:str,d:str):
    if a==b==c==d:
        return True
    else:
        return False
print(test_jackpot("@", "@", "@", "@"))
print(test_jackpot("abc", "abc", "abc", "abc"))
print(test_jackpot("SS", "SS", "SS", "SS"))
print(test_jackpot("&&", "&", "&&&", "&&&&"))
print(test_jackpot("SS", "SS", "SS", "Ss"))



# x=["&&", "&", "&&&", "&&&&"]
# while x[0]==x[1]==x[2]==x[3] and len(x)==4:
#   print("True")
# else:
#   print("False")

""" 3  Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False"""


# def hurdle_jump(a:list,b:int):
#     if b>=max(a):
#         return("true")
#     else:
#         return("false")
    
# print(hurdle_jump([1, 2,  4, ], 1))





# x=[1, 2, 1]
# y=1
# while  y>=max(x):
#     print("True")
#     break
# if y<max(x):
#     print("False")


"""  4  Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]"""

x=4
y=list(range(1,x+1))
for i in y:
    if x%i==0:
        print(i)

""" 5 Create a function that converts Celsius to Fahrenheit and vice versa"""

""""convert("35*C") ➞ "95*F"
convert("19*F") ➞ "-7*C"
convert("33") ➞ "Error"""

# convert = "145*F"
# for i in convert:
#     if len(convert)==4 and convert[2:]=="*C":
#        print(str(int(convert[0:2])* 1.8 + 32),"*F")
#     elif  len(convert)==4 and convert[2:]=="*F":
#         print(str(int(convert[0:2])-32/1.8), "*C")

# else:
#     print("eror")



"""6  Create a function that returns the number of palindrome numbers in a specified range (inclusive).
For example, between 8 and 34, there are 5 palindromes: 8, 9, 11, 22 and 33. Between 1550 and 1552 there is exactly one palindrome: 1551.
Examples
count_palindromes(1, 10) ➞ 9
count_palindromes(555, 556) ➞ 1
count_palindromes(878, 898) ➞ 3
Notes
A palindrome number is a number which remains the same when its digits are reversed. For example, 2552 reversed is still 2552. The reflectional symmetry of this number makes it a palindromic number.
Single-digit numbers are trivially palindrome numbers."""

"""Create a function that takes an integer and returns it as an ordinal number. An Ordinal Number is a number that tells the position of something in a list, such as 1st, 2nd, 3rd, 4th, 5th, etc."""

n=20
if 4 <= n <= 20:
      print(str(n) + "th")
elif n == 1 or (n % 10) == 1:
      print(str(n) + "st")
elif n == 2 or (n % 10) == 2:
    print(str(n) + "nd")
elif n == 3 or (n % 10) == 3:
      print(str(n) + "rd")




# def my_function(*kids):
#   print("The youngest child is " + kids[0])

# my_function("Emil", "Tobias", "Linus")
# def my_function(child3, child2, child1):
  
#   print("The youngest child is " + child2)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)




elements in the list are identical, and False otherwise. The list will contain 4 elements.

Examples
test_jackpot(["@", "@", "@", "@"]) ➞ True
test_jackpot(["abc", "abc", "abc", "abc"]) ➞ True
test_jackpot(["SS", "SS", "SS", "SS"]) ➞ True
test_jackpot(["&&", "&", "&&&", "&&&&"]) ➞ False
test_jackpot(["SS", "SS", "SS", "Ss"]) ➞ False"""


# def test_jackpot(a:str,b:str,c:str,d:str):
#     if a==b==c==d:
#         return True
#     else:
#         return False
# print(test_jackpot("@", "@", "@", "@"))
# print(test_jackpot("abc", "abc", "abc", "abc"))
# print(test_jackpot("SS", "SS", "SS", "SS"))
# print(test_jackpot("&&", "&", "&&&", "&&&&"))
# print(test_jackpot("SS", "SS", "SS", "Ss"))


""" 3  Create a function that takes an array of hurdle heights and a jumper's jump height, and determine whether or not the hurdler can clear all the hurdles.
A hurdler can clear a hurdle if their jump height is greater than or equal to the hurdle height.
hurdle_jump([1, 2, 3, 4, 5], 5) ➞ True
hurdle_jump([5, 5, 3, 4, 5], 3) ➞ False
hurdle_jump([5, 4, 5, 6], 10) ➞ True
hurdle_jump([1, 2, 1], 1) ➞ False"""


# def hurdle_jump(a:list,b:int):
#     if b>=max(a):
#         return("true")
#     else:
#         return("false")
    
# print(hurdle_jump([1, 2,  4, ], 1))

# 2-rd lucum 

# def hurdle_jump(hurdle_heights, jump_heights):
#     for i in hurdle_heights:
#         if i>=jump_heights:
#             return False
#         else:
#             return True
        
# print(hurdle_jump([1, 2, 3, 4, 5], 5))
# print(hurdle_jump([5, 5, 3, 4, 5], 3))
# print(hurdle_jump([5, 4, 5, 6], 10))
# print(hurdle_jump([1, 2, 1], 1))

"""  4  Create a function that takes a number as its argument and returns a list of all its factors.
Examples
factorize(12) ➞ [1, 2, 3, 4, 6, 12]
factorize(4) ➞ [1, 2, 4]
factorize(17) ➞ [1, 17]"""

# def factorize(a:list):
#     for i in list(range(1,a+1)):
#         if i%a==0:
#           i=[]
#           return list.append(i)
# print(factorize(12))       
