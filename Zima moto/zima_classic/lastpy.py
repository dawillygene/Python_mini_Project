# name = "ELIA WILLIAM MARIKI"
# number = 12
# state = True
# points = 12.34
# compex_number = 23 + 4j

# print(type(name))
# print(type(number))
# print(type(state))
# print(type(points))
# print(type(compex_number))
# # print(type(name))
# # print(type(name))



# print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))
# print((2 ** 4), (2 * 4.), (2 * 4)) 
# print((2 % -4), (2 % 4), (2 ** 3 ** 2))
# print((5 * ((25 % 13) + 100) / (2 * 13)) // 2)
# print (3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4 + 6)


# print ("Is it greater?", 5 > - 2)
# print ("Is it greater or equal?", 5 >= - 2)


# for ch in "john.smith@pythoninstitute.org": 
#     if ch == "@": 
#         break  # Exit the loop when '@' is found
#     print(ch, end="")  # Print characters on the same line

# print()

# for digit in "0165031806510": 
#     if digit == "0": 
#         print("x", end="")  # Replace '0' with 'x'
#         continue  # Skip the rest of the loop and move to the next iteration
#     print(digit, end="")  # Print other digits normally

# print()


# print("************************************")


# x = 4 
# y = 1 

# a = x & y 
# b = x | y 
# c = ~x # tricky! 
# d = x ^ 5 
# e = x >> 2 
# f = x << 2 
# print(a, b, c, d, e, f)




name = "Dawilly,gene , official"
print(name.split(","))

mylist = ["a","b","c"]
print("".join(mylist))

print("".join(name))

print(name.find("willy"))
print(name.index("w"))


number = "123456789a"
print(number.isnumeric())




print(number.isalpha())

print("my name is {} and my age is {}".format("haroon",23))


print("**************************************")
print("**************************************")
print("**************************************")
print("**************************************")

person = {
    "name":"Elia william mariki",
    "phone":12333433
}


person["accademic"] = "software engineering"
person["Graduate_Year"] = 2056
person["status"] = "single"



print(person)


car = dict(name="Toyota",year="1992",city="Germany")
print(car)