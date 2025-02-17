# table = [[x * y for x in range(13)] for y in range(13)]

# for row in table:
#     print("\t".join(str(cell).rjust(4) for cell in row))

# Generate multiplication table (0-12)
table = [[x * y for x in range(13)] for y in range(13)]

# Print header row
print("    ", end="")  # Space for alignment
for x in range(1, 13):  # Start from 1 to remove leading zeros
    print(f"{x:4}", end="")  
print("\n" + "-" * 50)  # Separator line

# Print table with row headers
for i, row in enumerate(table[1:], start=1):  # Skip row 0
    print(f"{i:2} |", end="")  # Row header with separator
    for cell in row[1:]:  # Skip first column (leading zeros)
        print(f"{cell:4}", end="")  # Print cell values
    print()  # New line after each row
