'''Given a list, rotate the values clockwise by one (the last value is sent to the first position).
'Examples
[1, 2, 3, 4, 5] ➞ [5, 1, 2, 3, 4]
[6, 5, 8, 9, 7] ➞ [7, 6, 5, 8, 9]
[20, 15, 26, 8, 4] ➞ [4, 20, 15, 26, 8]'''

# x=[6, 5, 8, 9, 7]
# y=x.pop(-1)
# x.insert(0,y)
# print(x)

# ''''''Create a function that inverts the rgb values of a given tuple.
# Examples
# color_invert((255, 255, 255)) ➞ (0, 0, 0)'''''''

# x,y,z=((165, 221, 70))
# n= abs(x-255), abs (y-255), abs(z-255)
# print(n)

# Write a function that searches a list of names (unsorted) for the name "Bob" and returns the location in the list. If Bob is not in the list, return -1.

# names=(["Leyla", "Anna",])
# name=names.index("Bob",) + "Bob" not in name*(-1)
# print(name)

# .6 Create a function that takes a dictionary of student names and returns a list of student names in alphabetical order.
# Examples
# {
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# } ➞ ["Becky", "John", "Steve"]

# names={
#   "Student 1" : "Steve",
#   "Student 2" : "Becky",
#   "Student 3" : "John"
# }

# y=list(names.values())
# y.sort()
# print(y)

# 7 Create a function that returns a list of strings sorted by length in ascending order.
# Examples
# sort_by_length(["a", "ccc", "dddd", "bb"]) ➞ ["a", "bb", "ccc", "dddd"]
# sort_by_length(["apple", "pie", "shortcake"]) ➞ ["pie", "apple", "shortcake"]
# sort_by_length(["may", "april", "september", "august"]) ➞ ["may", "april", "august", "september"]
# sort_by_length([]) ➞ []
# Notes
# Strings will have unique lengths, so don't worry about comparing two strings with identical length.
# Return an empty array if the input array is empty


# sort_by_length=(["a", "ccc", "dddd", "bb"])
# sort_by_length.sort(key=len)
# print(sort_by_length)


# Dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(Dict)



# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"
# }

# sample_dict['location'] = sample_dict.pop('city')
# print(sample_dict)


'''EXTRA Knowledge
4. Given a list of numbers, write a function that returns a list that...
Has all duplicate elements removed.
Is sorted from least to greatest value.
Examples
unique_sort([1, 2, 4, 3]) ➞ [1, 2, 3, 4]
unique_sort([1, 4, 4, 4, 4, 4, 3, 2, 1, 2]) ➞ [1, 2, 3, 4]
unique_sort([6, 7, 3, 2, 1]) ➞ [1, 2, 3, 6, 7]'''


y=([6, 7, 3, 2, 1])
x=(list(set(y)))
# x.sort()
print(x)
