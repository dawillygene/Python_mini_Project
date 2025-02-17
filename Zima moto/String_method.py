""" STRING METHODS IN PYTHON """

name = "Dawilly,gene"

print("Hello".lower())
print(name.upper())

print("Hello world".capitalize())

print("  Hello  ".strip())  # removes the extra spaces at the beggining and at the end of the string

print(name.strip())

title = "mabala the farmer"

print(title.title()) 


print(name.endswith("gene")) 
print(name.startswith("Dawilly"))

numbers  = "one , three";
print(numbers.replace("one","two"))


name = "Dawilly,gene"
print(name.split(","))

mylist = ["a","b","c"]
print("_".join(mylist))

print(name.find("willy"))

print(name.index("w"))

new_word = "jieleze sasa"
print(new_word.count("e"))


number = "123456789a"
print(number.isnumeric())

myword = "  a"



print(number.isalpha())
print(myword.isalpha())

text = "   "  
print(text.isspace())



"""swapcase and format"""

text = "Hello WoRLd!"
print(text.swapcase())  

formatted_text = "Hello, my name is {name} and I love {hobby}.".format(name="Dawilly", hobby="coding")
print(formatted_text)



x = str(10) + str(3.14)
print(x)

x = list("hello")
print(x)

x = set([1, 2, 2, 3])
print(x)

x = bool("")
y = bool("Python")
print(x, y)



number = 12
number2 = "24"

print(number + int(number2))


jina = "my name is dawilly gene"

print(len(jina))

print("name" in jina)
print("name" not in jina)

haroon = "HAROON"
print(haroon[0:5])
print(haroon[1:])


print("my name is {} and my age is {}".format("haroon","23"))






"""Adding elements in a list"""

names = ["DAWILLY","VENLIT","Esther","EddyJr","baraka"]

names.append("Neema")
print(names)

names.insert(0,"Eddy")  #add to a specific index
print(names)


names.extend(["Haroon","Ramadhan"])
print(names)

names.remove("Haroon")
print(names)

names.pop()
print(names)


# names.clear()
# print(names)



""" List Slicing """

my_list = [1,2,3,4,5,6,7,8,9]
sliced_list = my_list[0:5]
print(sliced_list)

""" List Operations """

conc_list  = my_list + names
print(conc_list)

repeted_list = conc_list * 2
print(repeted_list)


print("DAWILLY" in repeted_list)

print(len(repeted_list))


"""LIST METHODS"""

list1 = [3,1,4,5,8,6,0,11,10,7]
list1.sort()
print(list1)


list1.reverse()
print(list1)


"""List Comprehesion"""

# new_list = [expression for item in iterable if condition]

numbers = [x for x in range(5) if x>2]
print(numbers)

nono = []




for x in range(5):
    if(x>2):
        nono.append(x)
print(nono)


num_list = [x**2 for x in range(1,6) if x>1]
print(num_list)


even_number = [x for x in range(10) if x%2 == 0]
print(even_number)


words =["hello","dawilly","america"]

wordsupper = [word.upper() for word in words]
print(wordsupper)


name = "elia william mariki"
myname =list(name)
big =[x.upper() for x in myname]
realname = str(big)
print(realname)


name = "elia william mariki"
myname = list(name) 
big = [x.upper() for x in myname] 
realname = "".join(big)  
print(realname)



even_number = [x if x%2 == 0 else "odd" for x in range(10)]
print(even_number)



# table = [[x * y for x in range(13)] for y in range(13)]


# for row in table:
#     print("\t".join(str(cell).rjust(4) for cell in row))



"""Dictionary"""

person = {
 "name" : "DAWILLY BRODAH GENE",
 "age" : 24,
 "Nationality":"Tanzania",
 "description" : "Black chocolate nigga like me can't keep a bitch"

}

print(person)
print(person["name"])
print(person["description"])

print(person.get("name"))
print(person.get("name","Not available"))
print(person.get("gender","Not available"))


person["name"] = "Heavenlight Mariki"
person["age"] = 5
person['description'] = "Dad's daughter"


del person["age"]

name = person.pop("name")

print(name)
print(person)



for key in person:
    print(key)


for value in person.values():
    print(value)

for x in person.values():
    print(x)


for key,value in person.items():
    print(f"{key} : {value}")


print(person.keys())  # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 31])
print(person.items())  # dict_items([('name', 'Alice'), ('age', 31)])
