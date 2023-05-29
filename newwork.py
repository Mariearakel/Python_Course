"""1.  Write a map function that adds plus 5 to each item in the list."""

def number_plus_five(x):

    return x+5

numbers=[2, 5, 8, 6]

print(list(map(number_plus_five,numbers)))

"""2.  Write a map function that adds "Hello " in front of each item in the list."""

def hello_name(x):
    
    return "Hello,"+" "+ x

names=["Ani", "Mari", "Alvard"]

print(list(map(hello_name,names)))

"""3.  Using filter() function filter the list so that only negative numbers are left."""

def negative_numbers(x):

    return x<0

number_list= [5, -6, 8, -3, 1, -9]

print(list(filter(negative_numbers,number_list)))

"""4.  Using filter function, filter the even numbers so that only odd numbers are passed to the new list"""

def odd_numbers(x):

    return x%2!=0

number_list= [5, 6, 8, 3, 1, 9]

print(list(filter(odd_numbers,number_list)))

"""5.  Using map() and filter() functions add 2000 to the values below 8000."""

def mix_func(x):

    if x>8000:
     
     return x +2000
    
number_list=[2000,9800,15000,7000,666,17000] 

filtr_number=list(filter(mix_func,number_list))   

print(list(map(mix_func,filtr_number)))

"""6.  Return product of integer lists"""

from functools import reduce

def product_numbers(x, y):

    return x*y

lst=[2,8,1,9,10]

print(reduce(product_numbers,lst))

"""with lambda"""
lst=[2,8,1,9,10]

print(reduce(lambda x, y: x*y,lst))

