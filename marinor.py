""" 1  Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.



The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.

Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview."""


def interview(lst, tot):
        if len(lst)!=8:
             return "disqualified"
        #  lstmax=[5, 5, 10, 10, 15, 15, 20, 20]
        if lst[0] and lst[1]<=5 and lst[2] and lst[3]<=10 and lst[4] and lst[5]<=15 and lst[6] and lst [7]<=20 and sum(lst) >= tot- 20 :
            return "qualified"

        else:
            return "disqualified"

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20], 120))
print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))



'''2  In abstract set theory, a construction due to von Neumann represents the natural numbers by sets, as follows:

0 = [ ] is the empty set
1 = 0 ∪ [ 0 ] = [ 0 ] = [ [ ] ]
2 = 1 ∪ [ 1 ] = [ 0, 1 ] = [ [ ], [ [ ] ] ]
n = n−1 ∪ [ n−1 ] = ...
Write a function that receives an integer n and produces the representing set.

Examples
rep_set(0) ➞ []

rep_set(1) ➞ [[]]

rep_set(2) ➞ [[], [[]]]

rep_set(3) ➞ [[], [[]], [[], [[ ]]]]
Notes
Make sure to use list brackets [,].
Technically we should use set brackets {,} instead, but Python doesn't approve.
A neat feature of this representation is that n < m precisely if the set representing n is contained in the set representing m.'''

'''3 Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number (e.g. "12 + 24" or "23 - 21" or "12 // 12" or "12 * 21").

Here, we have 1 followed by a space, operator followed by another space and 2. For the challenge, we are going to have only two numbers between 1 valid operator. The return value should be a number.

eval() is not allowed. In case of division, whenever the second number equals "0" return -1.

For example:

"15 // 0"  ➞ -1
Examples
arithmetic_operation("12 + 12") ➞ 24 // 12 + 12 = 24

arithmetic_operation("12 - 12") ➞ 24 // 12 - 12 = 0

arithmetic_operation("12 * 12") ➞ 144 // 12 * 12 = 144

arithmetic_operation("12 // 0") ➞ -1 // 12 / 0 = -1'''


def arithmetic_operation(n):
     num1, op, num2=n.split( )
     num1=int(num1)
     num2=int(num2)
     if op=="+":
          return num1+num2
     elif op=="-":
          return num1-num2
     elif op=="*":
          return num1* num2
     elif op=="//":
          if num2==0:
               return -1 
          else:
              return num1//num2
     else:
          return None


print(arithmetic_operation("12 + 12"))
print(arithmetic_operation("12 - 12"))
print(arithmetic_operation("12 * 12"))
print(arithmetic_operation("12 // 12"))
print(arithmetic_operation("12 // 0"))


'''4 Create a function that takes a string as an argument and returns the Morse code equivalent.

Examples
encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."

encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"
This dictionary can be used for coding:

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
}'''


morse_code = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'}
def  encode_morse(message):
 morse_txt=""
 for i in message.upper():
    if i in morse_code:
        morse_txt+=morse_code[i]+ " "
    elif i== " ":
         morse_txt+=" "
    else:
         morse_txt+=i
 return  morse_txt    
print(encode_morse("EDABBIT CHALLENGE"))

'''5  Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:

"rank suit"
Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of Mandarin Chinese (for numbers see table below).

Number	Character	Pinyin
1	一	yi
2	二	er
3	三	san
4	四	si
5	五	wu
6	六	liu
7	七	qi
8	八	ba
9	九	jiu
Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):

One of tong is called bing gan (饼干, cookie)
Two of tong is called yan jing (眼镜, glasses)
One of tiao is called ji (鸡, chicken)
Examples of tiles
Five of tong ➞ "wu tong"

Seven of wan ➞ "qi wan"

One of tiao ➞ "ji"

Three of tiao ➞ "san tiao"'''


'''6 Write a function that returns True if two arrays, when combined, form a consecutive sequence. A consecutive sequence is a sequence without any gaps in the integers, e.g. 1, 2, 3, 4, 5 is a consecutive sequence, but 1, 2, 4, 5 is not.'''

def solution(arr1, arr2):

    combined = arr1 + arr2
  
    combined.sort()
    for i in range(len(combined) - 1):
        if combined[i+1] - combined[i] != 1:
            return False
    return True
     
print(solution([7, 4, 5, 1], [2, 3, 6]))

print(solution([1, 4, 6, 5], [2, 7, 8, 9]))

print(solution([1, 4, 5, 6], [2, 3, 7, 8, 10]))

print(solution([44, 46], [45]))


'''7A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]
Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
'''
'''8 Given a list of integers representing the color of each sock, determine how many pairs of socks with matching colors there are. For example, there are 7 socks with colors [1, 2, 1, 2, 1, 3, 2]. There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.

Create a function that returns an integer representing the number of matching pairs of socks that are available.

Examples
sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]) ➞ 3

sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]) ➞ 4

sock_merchant([]) ➞ 0'''

def sock_merchant(lst):
    
    sock =[]
    
    count_sock = {}
    
    for i in lst:
        
        if i not in count_sock:
            count_sock[i] = 1
        
        else:
            count_sock[i] += 1
           
            if count_sock[i]% 2==0:
                sock.append(i)
          
    return len(sock)
print(sock_merchant([10, 20, 20, 10, 10, 30, 50, 10, 20]))
print(sock_merchant([50, 20, 30, 90, 30, 20, 50, 20, 90]))
print(sock_merchant([]))


'''9 Create a function that takes a list and string. The function should remove the letters in the string from the list, and return the list.

Examples
remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string") ➞ ["w"]

remove_letters(["b", "b", "l", "l", "g", "n", "o", "a", "w"], "balloon") ➞ ["b", "g", "w"]

remove_letters(["d", "b", "t", "e", "a", "i"], "edabit") ➞ []'''

def remove_letters(letters, word):
   
    for i in word:
        if i in letters:
            letters.remove(i)
    return letters
print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))     

print(remove_letters(["s", "t", "r", "i", "n", "g", "w"], "string"))

print(remove_letters([" b","b", "l", "l", "g", "n", "o", "a", "w"], "balloon"))

print(remove_letters(["d", "b", "t", "e", "a", "i"], "edabit"))

'''10Create a function that returns the majority vote in a list. A majority vote is an element that occurs > N/2 times in a list (where N is the length of the list).

Examples
majority_vote(["A", "A", "B"]) ➞ "A"

majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A"

majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None '''

def majority_vote(lst):
    for i in lst:
        if lst.count(i)>len(lst)//2:
            return i 
        continue
    else:
             return "None"
        
print(majority_vote(["A", "B","B"]))

print(majority_vote(["A", "A", "B","B","B"])) 

print(majority_vote(["A", "A", "A", "B", "C", "A"]))

print(majority_vote(["A", "B", "B", "A", "C", "C"]))


'''11 Given a list of words in the singular form, return a set of those words in the plural form if they appear more than once in the list.

Examples
pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }

pluralize(["table", "table", "table"]) ➞ { "tables" }

pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }'''

def pluralize(lst):
    x=set()
    for i in lst:
        if (lst.count(i)>1):
            x.add(i+"s")
        else:
            x.add(i)
    return x
print(pluralize(["cow", "pig", "cow", "cow"]))   
print(pluralize(["table", "table", "table"]))
print(pluralize(["chair", "pencil", "arm"]))

'''12  Create a function based on the input and output. Look at the examples, there is a pattern.

Examples
secret("p.one.two.three") ➞ "<p class='one two three'></p>"

secret("p.one") ➞ "<p class='one'></p>"

secret("p.four.five") ➞ "<p class='four five'></p>"'''

def secret(string):
    tag, *classes = string.split(".")
    class_str = " ".join(classes)
    return f"<{tag} class='{class_str}'></{tag}>"



'''13 Write a function that takes the coordinates of three points in the form of a 2d array and returns the perimeter of the triangle. The given points are the vertices of a triangle on a two-dimensional plane.

Examples
perimeter([[15, 7], [5, 22], [11, 1]]) ➞ 47.08

perimeter([[0, 0], [0, 1], [1, 0]]) ➞ 3.41

perimeter([[-10, -10], [10, 10 ], [-10, 10]]) ➞ 68.28
Notes
The given points always create a triangle.
The numbers in the argument array can be positive or negative.
Output should have 2 decimal places
This challenge is easier than it looks.'''


""" 14  Given a function that accepts unlimited arguments, check and count how many data types are in those arguments. Finally return the total in a list.

List order is:

[int, str, bool, list, tuple, dictionary]"""

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
 

"""15There are many different styles of music and many albums exhibit multiple styles. Create a function that takes a list of musical styles from albums and returns how many styles are unique.

Examples
unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]) ➞ 9

unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]) ➞ 7"""

def unique_styles(albums):
    return len(set(",".join(albums).split(",")))


print(unique_styles([
  "Dub,Dancehall",
  "Industrial,Heavy Metal",
  "Techno,Dubstep",
  "Synth-pop,Euro-Disco",
  "Industrial,Techno,Minimal"
]))
print(unique_styles([
  "Soul",
  "House,Folk",
  "Trance,Downtempo,Big Beat,House",
  "Deep House",
  "Soul"
]))