 
  
# Generate multiplication table (1-12)

table = [[x * y for x in range(1,13)] for y in range(1,13)]

#@dawilly_gene

print()
print()
print()
print()

for row in table:
     print("\t".join(str(cell).rjust(4) for cell in row))

print()
print()
print()
print()