fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']

colors = ['red', 'green', 'blue', 'yellow', 'orange']

print(colors[1:4])

alphabet = 'abcdefghijklmnopqrstuvwxyz'
print(alphabet[1::3])


coordinates = (4, 3, 2, 1, 0)
print(coordinates[1:4])


fruits = ['apple', 'banana', 'cherry', 'date']

fruits[1] = 'blackberry'

print(fruits)


text = "Python is awesome!"
print(text[7:9])

numbers = [1, 2, 3, 4, 5]
print(numbers[0:5])

months = ['January', 'February', 'March', 'April', 'May', 'June']
print(months[-3::])

values = [10, 20, 30, 40, 50]
sliced = values[1:]
print(sliced[-2::])


matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]

print(matrix[1])

text = "abcdefghijklmnopqrstuvwxyz"
print(text[2::4])


data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 10], [11, 12]]]
print(data[1:3])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:None:2])


letters = ['a', 'b', 'c', 'd', 'e']
reversed_list = [letters[x] for x in range(len(letters) - 1, -1, -1)]
print(reversed_list)


nested = [[1, 2, [3, 4]], [5, 6, [7, 8]]]
print(nested[1][2][0])


phrase = "Hello world, welcome to Python!"
print(phrase[6:11])


data = [10, 20, 30]
print(data[-4:])



import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)

last_column =[row[-1] for row in arr]
print(last_column)


matrix = [[10, 20], [30, 40], [50, 60]]
matrix[1][1] = 99
print(matrix)


