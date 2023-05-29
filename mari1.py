# """ 1. Create a function which returns the number of true values there are in an array.
# Examples
# countTrue([true, false, false, true, false]) ➞ 2
# countTrue([false, false, false, false]) ➞ 0
# countTrue([]) ➞ 0
# Notes
# Return 0 if given an empty array.
# All array items are of the type bool (true or false).
# # """
# # def countTrue(a):
# #         for i in countTrue:
# #          if type(i)==bool: 
# #             return(sum(i))
# # print(countTrue([True, False, False, True, False]))


# """2. Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
# Examples
# intWithinBounds(3, 1, 9) ➞ true
# intWithinBounds(6, 1, 6) ➞ false
# intWithinBounds(4.5, 3, 8) ➞ false
# Notes
# The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
# Bounds will be always given as integers."""

# # def longest_time(hour,minute,second):
# #      if 3600*hour>minute*60 and 3600*hour>second:
# #       return hour
# #      if 3600*hour<minute*60 and minute*60>second:
# #           return minute
# #      else:
# #           return second
# # print(longest_time(1,59,3598))    
# # print(longest_time(2, 300, 15000))
# # print(longest_time(15, 955, 59400))

# '''Create a function that takes a string and censors words over four characters with *.
# Examples
# censor("The code is fourty") ➞ "The code is ******"
# censor("Two plus three is five") ➞ "Two plus ***** is five"
# censor("aaaa aaaaa 1234 12345") ➞ "aaaa ***** 1234 *****"
# Notes
# Don't censor words with exactly four characters.
# If all words have four characters or less, return the original string.
# The amount of * is the same as the length of the word'''

# # def censor(s):
# # 	lst = []
# # 	for i in s.split(" "):
# # 		if len(i)>4:
# # 			lst.append("*"* len(i))
# # 		else:
# # 			lst.append(i)
# # 	return " ".join(lst)     

# # print(censor("The code is fourty"))
    
# '''Create a function that validates whether a number n is within the bounds of lower and upper. Return false if n is not an integer.
# Examples
# intWithinBounds(3, 1, 9) ➞ true
# intWithinBounds(6, 1, 6) ➞ false
# intWithinBounds(4.5, 3, 8) ➞ false
# Notes
# The term "within bounds" means a number is considered equal or greater than a lower bound and lesser (but not equal) to an upper bound, (see example #2).
# Bounds will be always given as integers.'''

# # def intWithinBounds(a,b,c,):
# #         if a>=b and a<c and type(a)==int:
# #             return True
# #         else:
# #             return False
# # print(intWithinBounds(3, 1, 9))
# # print(intWithinBounds(6, 1, 6))
# # print(intWithinBounds(4.5, 3, 8))

# '''4. Create a function that takes the month and year (as integers) and returns the number of days in that month.
# Examples
# days(2, 2018) ➞ 28
# days(4, 654) ➞ 30
# days(2, 200) ➞ 28
# days(2, 1000) ➞ 28
# Notes
# Don't forget about leap years!'''

# # def month_year(month,year):
# #      if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
# #           return "31"
# #      elif month==2 and year%400==0 or year%4==0 and year%100!=0:
# #           return "29"
# #      elif month==2:
# #           return "28"
# #      else:
# #           return "30"
# # print(month_year(2,2018))
# # print(month_year(4,654))
# # print(month_year(2,200)) 
# # print(month_year(2,1000))

# ''''6. Given a sentence, create a function that replaces every "a" as an article with "an absolute". It should return the same string without any change if it doesn't have any "a".
# Examples
# absolute("I am a champion!!!") ➞ "I am an absolute champion!!!"
# absolute("Such an amazing bowler.") ➞ "Such an amazing bowler."
# absolute("A man with no haters.") ➞ "An absolute man with no haters."
# Notes
# Watch for uppercase letters as shown in example #3.
# '''

# # def absolute(s):
# # 	lst = []
# # 	for i in s.split(" "):
# # 		if "a" or "A" in s:
# # 			s.replace("a", "an absolute")
# # 			lst.append
# # 		else:
# # 			lst.append(i)
  
# # print(absolute("i am a champion"))
# '''Return an Array of Subarrays
# Write a function that takes three arguments (x, y, z) and returns an array containing x subarrays (e.g. [[], [], []]), each containing y number of item z.
# x Number of subarrays contained within the main array.
# y Number of items contained within each subarray.
# z Item contained within each subarray.
# Examples
# matrix(3, 2, 3) ➞ [[3, 3], [3, 3], [3, 3]]
# matrix(2, 1, "edabit") ➞ [["edabit"], ["edabit"]]
# matrix(3, 2, 0) ➞ [[0, 0], [0, 0], [0, 0]]
# Notes
# The first two arguments will always be integers.
# The third argument is either a string or an integer.'''

# ''' Given a string of numbers separated by a comma and space, return the product of the numbers.
# Examples
# multiplyNums("2, 3") ➞ 6
# multiplyNums("1, 2, 3, 4") ➞ 24
# multiplyNums("54, 75, 453, 0") ➞ 0
# multiplyNums("10, -2") ➞ -20
# # Notes
# Bonus: Try to complete this challenge in one line!'''''

# # def find_missing_number(arr):
# #     n = len(arr) + 1
# #     hash_set = set(arr)
 
# #     for i in range(1, n):
# #         if i not in hash_set:
# #             return i
 
# #     return n
 
# # arr = [1, 2, 4, 6, 3, 7, 8]
# # # missing_number = find_missing_number(arr)
# # # print("Missing number is:", missing_number)


# # def solution(param1, param2):
# #     return param1+param2
    

# # print(solution(2,5))


# # def solution(year):
# #     if year<=0:
# #        return "write a namber >=0"
# #     elif year<=100:
# #        return "1" 
# #     elif year%100==0:
# #        return year//100 
# #     else:
# #         return year//100+1
        
# # print(solution(5))


# # def solution(inputString):
# #  if inputString[::-1]==inputString:
# # #      return True
# # #  else:
# # #      return False
 
# # # print(solution("114"))


# # # def adjacentElementsProduct(inputArray):
# # #     for i in range(0, len(inputArray)-1):
# # #         lis=(inputArray[i]*inputArray[i+1])
# # #         return(lis)
# # # print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))

# # def solution(statues):
# #     statues.sort()
# #     statuesNeeded = 0
# #     for i in range(0, len(statues)-1):
# #         if(statues[i + 1] - statues[i]) > 1:
# #             statuesNeeded = statuesNeeded + statues[i + 1] - statues[i] - 1
# #     # print(f'Status needed {statuesNeeded}')
# #     return statuesNeeded
# # print(solution([2,6,5,8]))


# # def solution(sequence):
# #     error = 0
# #     second_error=0
# #     for index ,i in enumerate(sequence[:-1]):
# #             if sequence[index+1]<=i:
# #              error+=1
             
# #             if index<len(sequence)-2 and sequence[index+2]<=i:
# # #                second_error+=1
# # #     if error<=1 and second_error<=1:
# # #             return True
# # #     return False   
        


# # # def solution(matrix):
# # #     total=0
# # #     j_colums = set()
# # #     for index, i in enumerate(matrix):
# # #         for jindex,j in enumerate(i):
# # #              if j==0:
# # #                  j_colums.add(jindex)
# # #                  continue
# # #              if  index>0 and jindex in j_colums:
# # #                  continue
         
# # #              total+=j
# # #     return total       


# # def allLongestStrings(inputArray):
# #     m=[]
# #     for i in inputArray:
# #         m.append(len(i))
# #         count=max(m)
# #     l=[]
# #     for i in inputArray:
# #        if(len(i)==count):
# #           l.append(i)
# #     return l


# # def allLongestStrings(inputArray):
# #     m = max(len(s) for s in inputArray)
# #     r = [s for s in inputArray if len(s) == m]
# #     return r
# # print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))



# # def allLongestStrings(inputArray):
# #     result = list()
# #     max_str_len = 0
# #     for i in inputArray:
# #         if max_str_len < len(i):
# #             max_str_len = len(i)

# #     for j in inputArray:
# #         if len(j) == max_str_len:
# #             result.append(j)

# #     return result

# # print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))

# # def solution(s1,s2):
# #  return sum(min(s1.count(x),s2.count(x)) for x in set(s1))
# # print(solution("aaa","aab"))

# def isLucky(n):
#     n = [int(i) for i in str(n)]
#     n_slice = len(n) // 2


#     if sum(n[:n_slice]) == sum(n[n_slice : ]):
#         return True
#     else:
#         return False
# print (isLucky(120303))




 
# # def solution(a):

# #     l = sorted([i for i in a if i > 0])
# #     for n,i in enumerate(a):
# #         if i == -1:
# #             l.insert(n,i)
# #     return l


# # def solution(a):
# #     b=[]
# #     c=[]
# #     for i in a:
# #         i[::2]
# #         b.append(i)
# #     for i in a:
# #         i[1: 2]
# #         c.append(i)
# #         return sum(b,c)
# # print(solution([50, 60, 60, 45, 70]))
        



# # def solution(picture):
# #     v_border=["*"*(len(picture[0])+2)]
# #     return v_border
    
# #     with_border=["*"+x+"*" for x in picture]
    
# #     return v_border+with_border+v_border

# # print(solution(["abc"]))



# '''Using .sort() method, create a lambda function that sorts the list in descending order. Refrain from using the reverse parameter.
# (Hint: lambda will be passed to sort method's key parameter as argument)
# Please check out Hint 0 below to be informed about a glitch regarding this exercise.
# lst=[100, 10, 10000, 1, 9, 999, 99]'''

# lst=[100, 10, 10000, 1, 9, 999, 99]
# print(sorted(lst, key=lambda x:x , reverse=True))

# """Using sorted() function, reverse parameter and lambda sort the tuples in the list based on the last character of the second items in reverse order.
# lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]
# """
# list=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

# # print(sorted(list, key=lambda x: x [1][-1],reverse=True))

# def solution(inputArray):
#     moves = 0
#     for i in range(1,len(inputArray)):
#         if inputArray[i] <= inputArray[i-1]:

#             moves += inputArray[i-1] - inputArray[i] + 1
           
#             inputArray[i] = inputArray[i-1] + 1
#     return moves
# print(solution([2,1,10,1]))

        

# def solution(inputString):
#     for i in inputString:
#      if i[::]==i [::-1]:
#       return True



# x=5
# y=10
# z=5
# c=10
# a=y+x==c+z

# def solution(inputString):

#   p = inputString.split('.')
#   return len(p) == 4 and all(n.isdigit() and 0 <= int(n) < 256 for n in p)

# """1 You need to create two functions to substitute str() and int(). A function called int_to_str() 
# that converts integers into strings and a function called str_to_int() that 
# converts strings into integers."""
  
# def int_str(num):
#         if num==str(num):
#           return int(num)
#         else:
#             return str(num)
# print(type(int_str(5)))
# print(type(int_str("5")))
        
# # """Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

# # # # Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:
# # # # """"

# # pet="timmy"
# # items = {"tv": 30,"timmy": 20,"stereo": 50,} 
# # if pet in items:
# #       print(pet.capitalize(),"is a gone")
# # else:
# #        print( pet.capitalize(), "is not here")



# # def find_it(items, name):
# #     if name in items:
# # 	    return name.capitalize(), "is a gone"
# #     else:
# # 	    return name.capitalize(), "is a here"
    
# # print (find_it({"tv": 30,"stereo": 50,} ,"timmy"))

# # # """Create a function that takes a country's name and its area as arguments 
# # # and returns the area of the country's proportion of the total world's landmass."""

# name_countriy="Germany"
# area_country=3485600
# area_world=48940000
# c=area_country/area_world*100
# print(name_countriy,"is", int(c)," % of the total world's landmass")


# """For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.

# Write a template string according to the following example. Notice that the template will be formatted twice:

# Example
# a = "John"
# b = "Joe"
# template = "yourtemplatestringhere"

# template.format(1).format(a, b) ➞ "My best friend is Joe."""

# txt1="my best friend is {str:}"
# print(txt1.format(str="jon"))

'''Given a lottery ticket (ticket), represented by a list of 2-value lists, create a function to find out if you've won the jackpot.

To do this, you must first count the "mini-wins" on your ticket. Each sublist has both a string and a number within it. If the character code of any of the characters in the string matches the number, you get a mini-win. Note you can only have one mini-win per sublist.

Once you have counted all of your mini-wins, compare that number to the other input provided (win). If your number of mini-wins is more than or equal to win, return Winner!. Else, return Loser!.

'''


def check_lottery(ticket, win):
    mini_wins = 0
    for i in ticket:
        string = i[0]
        number = i[1]
        for j in string:
            if ord(j) == number:
                mini_wins += 1
                break 
    if mini_wins >= win:
        return "Winner!"
    else:
        return "Loser!"

print(check_lottery([["YYW", 70], ["WXK", 65], ["RPDI", 88]], 2))



"""Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

"""

def arithmetic_operation(s):
    number1, operator, number2 = s.split()

    number1 = int(number1)
    number2 = int(number2)
    
    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "//":
        if number2 == 0:
            return -1
        else:
            return number1 // number2
        
print(arithmetic_operation("12 + 12"))

print(arithmetic_operation("12 - 12"))

print(arithmetic_operation("12 * 12"))

print(arithmetic_operation("12 // 0"))

"""A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.

Create a function that determines whether a number is a Disarium or not."""
    
def is_disarium(n):
    digits = [int(d) for d in str(n)]
    s = sum(d**i for i, d in enumerate(digits, 1))
    return s == n
print(is_disarium(135))

"""Write a function that takes a list of lists and returns the value of all of the symbols in it, where each symbol adds or takes something from the total score. Symbol values:

# = 5
O = 3
X = 1
! = -1
!! = -3
!!! = -5
A list of lists containing 2 #s, a O, and a !!! would equal (0 + 5 + 5 + 3 - 5) 8.

If the final score is negative, return 0 (e.g. 3 #s, 3 !!s, 2 !!!s and a X would be (0 + 5 + 5 + 5 - 3 - 3 - 3 - 5 - 5 + 1) -3, so return 0.

"""

def sum_symbols(lst):
    sums = 0
    for i in lst:
        for j in i:
            if j == '#':
                sums += 5
            elif j == 'O':
                sums += 3
            elif j== 'X':
                sums += 1
            elif j == '!':
                sums -= 1
            elif j == '!!':
                sums -= 3
            elif j== '!!!':
                sums -= 5
    if sums < 0:
        return 0
    else:
        return sums
    
print(sum_symbols([
  ["#", "O", "#", "!!", "X", "!!", "#", "O", "O", "!!", "#", "X", "#", "O"],
  ["!!!", "!!!", "!!", "!!", "!", "!", "X", "!", "!!!", "O", "!", "!!!", "X", "#"],
  ["#", "X", "#", "!!!", "!", "!!", "#", "#", "!!", "X", "!!", "!!!", "X", "O"],
  ["!!", "X", "!!", "!!", "!!!", "#", "O", "O", "!!!", "#", "O", "O", "#", "!!"],
  ["O", "X", "#", "!", "!", "X", "!!!", "O", "!!!", "!!", "O", "!", "O", "X"],
  ["!!", "!!!", "X", "!!!", "!!", "!!", "!!!", "X", "O", "!", "#", "!!", "!!", "!!!"],
  ["!!", "!!", "#", "O", "!", "!!", "!", "!!!", "#", "O", "#", "!", "#", "!!"],
  ["X", "X", "O", "X", "!!!", "#", "!!!", "!!!", "X", "X", "X", "!", "#", "!!"],
  ["O", "!!!", "!", "O", "#", "!", "!", "#", "X", "X", "#", "O", "!!", "!"],
  ["X", "!", "!!", "#", "#", "X", "!!", "O", "!!", "X", "X", "!!", "#", "X"],
  ["!", "!!", "!!", "O", "!!", "!!", "#", "#", "!", "!!!", "O", "!", "#", "#"],
  ["!", "!!!", "!!", "X", "!!", "!!", "#", "!!!", "O", "!!", "!!!", "!", "!", "!"],
  ["!!!", "!!!", "!!", "O", "!", "!", "!!!", "!!!", "!!", "!!", "X", "!", "#", "#"],
  ["O", "O", "#", "O", "#", "!", "!!!", "X", "X", "O", "!", "!!!", "X", "O"]
]))

"""Create a function that takes a string's characters as ASCII and returns each character's hexadecimal value as a string."""




def convert_to_hex(txt):
    str1 = ""
    for i in txt:
        str1+= hex(ord(i))[2:]
    return str1
print(convert_to_hex("hello word"))


"""Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.

Given a censored string and a string of the censored vowels, return the original uncensored string.

"""

def uncensor(txt, vowels):
   
    uncensored = ''
    for char in txt:
        if char == '*':
            uncensored += vowels[0+1]   
        else:
            uncensored += char
    return uncensored          
print(uncensor("*PP*RC*S*", "UEAE"))

 
def tidy_link(url, name, hover_text=None):
       if hover_text:
        return f"[{name}]({url} \"{hover_text}\")"
       else:
        return f"[{name}]({url})"

print(tidy_link("https://edabit.com/challenges", "this", "Go to the challenges!"))

print (tidy_link("https://www.google.com", "Google", "Google Search"))

print("Line 1\nLine 2\nLine 3")

def pluralize(words):
    # create an empty set to hold the pluralized words
    plural_words = set()
    # create a dictionary to keep track of the count of each word
    word_counts = {}
    # iterate through each word in the list
    for word in words:
        # if the word is not already in the dictionary, add it with a count of 1
        if word not in word_counts:
            word_counts[word] = 1
        # if the word is already in the dictionary, increment its count
        else:
            word_counts[word] += 1
            # if the count is 2 or more, add the plural form of the word to the set of pluralized words
            if word_counts[word] == 2:
                plural_words.add(word + 's')
    # return the set of pluralized words
    return plural_words

def remove_letters(letters, word):  
    lst=[]
    for i in letters:
        if  i not in word:
           lst.append(i)
    return  lst
        



# def censor_string(txt,lst, char="*"):
#     y=txt.split()
#     lst=[]
#     for i in y:
#      if i in lst:
#       word=char*len(i)
#       lst.append(word)
#      else:
#          lst.append(i)
#          z=" ".join(lst)
#     return z
# print(censor_string("Today is a Wednesday!", ["Today", "a"]))

# def parse_code(txt):
#   parts = txt.split('000')
#   return {
#         "first_name": parts[0],
#         "last_name": parts[1],
#         "id": parts[2]
#     }
# print(parse_code("John000Doe000123"))

# def interview(lst, tot):
#         lst2=[5, 5, 10, 10, 15, 15, 20, 20]
#         if lst[0] and lst[1]<=5 and lst[2] and lst[3]<=10 and lst[4] and lst[5]<=15 and lst[6] and lst [7]<=20 and tot==120:
#             return "qualified"
#         elif len(lst)!=len(lst2):
#             return "disqualified"

#         else:
#             return "disqualified"
# print(interview([5, 8, 10, 10, 15, 15], 120))
      


# # def string(a=str):
# #     a.split( )
# #     for i in list(a):
# #         if i=="+":
# #             return i[0] + i[2]:
# # print(string("24 + 24"))

# def basic_arithmetic(s):
#     num1, op, num2 = s.split()
#     num1, num2 = int(num1), int(num2)
#     if op == "+":
#         return num1 + num2
#     elif op == "-":
#         return num1 - num2
#     elif op == "*":
#         return num1 * num2
#     elif op == "//":
#         if num2 == 0:
#             return -1
#         else:
#             return num1 // num2
#     else:
#         return None




def solution(arr1, arr2):

    combined = arr1 + arr2
  
    combined.sort()
    for i in range(len(combined) - 1):
        if combined[i+1] - combined[i] == 1:
            return True
    return False
     
print(solution([7, 4, 5, 1], [2, 3, 6]))

print(solution([1, 4, 6, 5], [2, 7, 8, 9]))

print(solution([1, 4, 5, 6], [2, 3, 7, 8, 10]))

print(solution([44, 46], [45]))



# def solution(snock):
#     x={}
#     for i in snock:
#       count_scnock=snock.count(i)
#       if count_scnock>2:
#               x.append(i)
 
#     return x
# print(solution([10, 20, 20, 10, 10, 30, 50, 10, 20]))



# def remove_letters(letters, word):
#     lst = []
#     for i in letters:
#         if i not in word:
#             lst.append(i)
#     return lst
# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))     

# print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))

# print(remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))

# print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))


def mec(tar):
    for i in tar:
        if tar.count(i)>len(tar)//2:
            return i 
        continue
    else:
             return "None"
        
print(mec(["A", "B","B"]))

print(mec(["A", "A", "B","B","B"])) 

print(mec(["A", "A", "A", "B", "C", "A"]))

print(mec(["A", "B", "B", "A", "C", "C"]))



# def pluralize(words):
#     # create an empty set to hold the pluralized words
#     plural_words = set()
#     # create a dictionary to keep track of the count of each word
#     word_counts = {}
#     # iterate through each word in the list
#     for word in words:
#         # if the word is not already in the dictionary, add it with a count of 1
#         if word not in word_counts:
#             word_counts[word] = 1
#         # if the word is already in the dictionary, increment its count
#         else:
#             word_counts[word] += 1
#             # if the count is 2 or more, add the plural form of the word to the set of pluralized words
#             if word_counts[word]==2:
#                 plural_words.add(word + 's')  
          
#     return (plural_words)


def pluralize(lst):
    
    words = set()
    
    word = {}
    
    for i in lst:
        
        if i not in word:
            word[i] = 1
        
        else:
            word[i] += 1
           
            if word[i] == 2:
                words.add*(i + 's')  
          
    return words

def pluralize(lst):
   return set(i + 's'*(lst.count(i)>1) for i in lst)
print(pluralize(["cow", "pig", "cow", "cow"]))



def secret(string):
    tag, *classes = string.split(".")
    class_str = " ".join(classes)
    return f"<{tag} class='{class_str}'></{tag}>"


# def pluralize(lst):
#    return set(i + 's'*(lst.count(i)>1) for i in lst)
# print(pluralize(["cow", "pig", "cow", "cow"]))

def pluralize(lst):
    x=set()
    for i in lst:
        if (lst.count(i)>1):
            x.add(i+"s")
        else:
            x.add(i)
    return x
print(pluralize(["cow", "pig", "cow", "cow"]))   



def count_datatypes(*args):
    types = [0, 0, 0, 0, 0, 0]  # counts for [int, str, bool, list, tuple, dictionary]
    for arg in args:
        if type(arg) == int:
            types[0] += 1
        elif type(arg) == str:
            types[1] += 1
        elif type(arg) == bool:
            types[2] += 1
        elif type(arg) == list:
            types[3] += 1
        elif type(arg) == tuple:
            types[4] += 1
        elif type(arg) == dict:
            types[5] += 1
    return types
print (count_datatypes(1, 45, "Hi", False) )

print (count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1) )
print(count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23) )
print(count_datatypes())
 


# def unique_styles(albums):
#     albums.split(,)


def unique_styles(albums):
    return len(set(",".join(albums).split(",")))


print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]))


x="mari,ani"
y=",".join(x)
print(y)

for i in range(8):
    print(i)