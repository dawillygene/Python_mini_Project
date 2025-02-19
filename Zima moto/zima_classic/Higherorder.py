
"""
    Higher-order function that computes the sum and product of a list of numbers
    using the passed-in function.

    :param operation: A function to perform a reduction operation.
    :param numbers: A list of numbers.
    :return: A tuple (sum_result, product_result).
"""


def apply_function(sum_func,product_func,numbers):
    return sum_func(numbers),product_func(numbers)

def add(lst):
    result = 0
    for value in lst:
        result += value
    return result


def multiply(lst):
    result = 1
    for value in lst:
        result *= value
    return result

numbers = [1,2,3,4,5,6,7,8,9,10]

#sum_result,product_result = apply_function(add,multiply,numbers)

print(apply_function(add,multiply,numbers))



"""Write a function that accepts a list of numbers and a divisar. 
The function should divide each number in the list by the divisor, 
but with custom exception handling, if a division by zero occurs, 
the function should raise a custom exception that outputs a 
message like "Cannot divide by zero!" and continues with the next number. 
The function should also keep track of how many successful and failed divisions occurred."""

class DivisionByZeroError(Exception):

    pass



def divide_numbers(numbers,divisor):
    success_division = 0
    failed_division = 0

    for number in numbers:
        try:
            result = number/divisor
            print(f"Result of {number} / {divisor} = {result} ")
            success_division += 1
        except DivisionByZeroError as e:
            print(e)
            failed_division +=1
        except Exception as e:
            print(f"An unexpected error occured: {e}")
            failed_division += 1
    
    print(f" Summary : Successful division : {success_division} , Failed division : {failed_division}")
        

numbers = [10, 20, 30, 40, 50,100]
divisor = 0
divide_numbers(numbers, divisor)



def ListDivision(lst,target):
    index = 0
    for value in lst:
        if value % target == 0 :
            return index
        index += 1
    return -1
        

numbers = [10, 20, 30, 40, 50]
target = 101
print(ListDivision(numbers,target))


def find_divisible_index(numbers,target):
    for index,number in enumerate(numbers):
        if number % target == 0:
            return index
    return -1

numbers = [10, 21, 30, 42, 50]
target = 7
result = find_divisible_index(numbers, target)
print(f"Index of the first number divisible by {target}: {result}")




"""Write a Python function that generates a multiplication 
table of size n x n using nested loops and returns the 
result as a list of lists (ie, a 20 matrix). 
Then, write a list comprehension that transforms 
this table into a flattened list (ID), where each element is the result of the 
multiplication at the corresponding row and column"""


def multiplication_table():
    table = [[0 for _ in range(12)] for _ in range(12)]
    for column in range(1,13):
        for row in range(1,13):
            table[column-1][row-1] = row * column
    return table 

def flatten_table(table):
    return [item for row in table  for item in row]


table = multiplication_table()

res = flatten_table(table)

print(res)

# for row in table:
#     print(row)

# print(multiplication_table())




