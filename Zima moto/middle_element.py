"""Extract Middle Element from List: Write a 
Python function that takes a list of oddlength 
and returns the middle element. If the list has an even length, 
returnthetwomiddle elements."""



def middle_element(lst):
    if len(lst) % 2 == 0:
        return lst[len(lst) // 2 - 1], lst[len(lst) // 2]
    else:
        return lst[len(lst) // 2]


my_list = [12,3,45,33,51,223,21,4]
print(middle_element(my_list))



"""Reversing a String Without Built-in Functions:
 Write a Python function that takesastring and 
 returns it in reverse order using slicing 
(do not use the reversed() function)."""


def reverse_string(input_string):
    string_list = list(input_string)
    _reverse_string = string_list[::-1]
    result = "".join(_reverse_string)
    return result

name ="ELIA"
print(reverse_string(name))



"""Remove Duplicates Using Slicing: Write a Python 
function that takes a list andreturns a new list 
with duplicates removed, 
keeping the original order of elements"""


names =["ELIA","HAROON","MAKUKA","RAMADHAN","JESTONE","MAKUKA","HAROON"]

def remove_duplicates(lst):
    non_duplicate = []
    for value in lst:
        if value not in non_duplicate:
            non_duplicate.append(value)
    return non_duplicate

print(remove_duplicates(names))



"""Extract Every N-th Element from a List: Write a 
Python function that takes a list and an integer n, 
and returns a new list 
containing every n-th element from the original list."""

def n_term_list(lst,n):
    return lst[::n] 

table =[0,1,2,3,4,5,6,7,8,9,10,11,12]
print(n_term_list(table,2))


def extract_nth_elements(lst, n):
    return lst[n-1::n] 

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n = 3
result = extract_nth_elements(my_list, n)
print(result)


"""Check if a String is a Palindrome: Write a Python 
function that takes a stringandreturns True 
if the string is a palindrome 
(reads the same forward and backward), using slicing"""



def is_Palindrome(input_string):
    return input_string == input_string[::-1]

print(is_Palindrome("civic"))




"""6. Extract a Sublist Between Two Indices:
 Write a Python function that takes a list andtwo 
 indices (start and end) and returns a sublist containing elements froms tart
index to end index (inclusive)"""

def extract_sublist(lst,start,end):
    return lst[start:end+1]

number = [0,1,2,3,4,5,6,7,8,9,10]
print(extract_sublist(number,1,8))


"""Create a Copy of a List Using Slicing: Write a Python function 
that takes a list andreturns a copy of that list using slicing
"""

def copy_list(lst):
    return lst[::]

print(copy_list(number))


"""Find the Second Largest Element in a List:
Write a Python function that takes a list of numbers 
and returns the second largest element using slicing and indexing."""


number = [1,2,3,4,5,10,6,19]



def Sec_Largest(lst):
    if len(lst) < 2 :
        print("The number should be atleast two")
        exit
    remove_duplicates = list(set(lst))
    sorted_list = sorted(remove_duplicates)
    return sorted_list[-2]

print(Sec_Largest(number))
    


"""Rotate a List Left by N Elements: Write a Python 
function that rotates a list lst to the left by n elements using slicing."""

def rotate_left(lst,n):
    n = n % len(lst)
    return lst[n:] + lst[:n]

numbers = [1, 2, 3, 4, 5, 6]
rotated_list = rotate_left(numbers, 2)
print(rotated_list) 



"""10. Replace Elements in a Range of Indices: Write a Python function that 
takes a list, two indices (start and end),
and a new list of elements. Replace the 
sublist between the two indices with the new list."""

numbers = [1, 2, 3, 4, 5, 6]


def Replaces(lst,new_list,start,end):
    return  lst[:start] + new_list +lst[end:]

print(Replaces(numbers,names,2,4))










