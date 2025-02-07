# Function to calculate compound interest
def calculate_compound_interest(P, r, n, t):
   
    A = P * (1 + r / n) ** (n * t)
    
    # Calculate the compound interest
    CI = A - P
    
    return CI, A

# Input values
P = float(input("Enter the principal amount (P): "))
r = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
n = int(input("Enter the number of times interest is compounded per year (n): "))
t = float(input("Enter the time the money is invested for in years (t): "))

# Calculate compound interest and total amount
compound_interest, total_amount = calculate_compound_interest(P, r, n, t)

# Output the results
print(f"Compound Interest: {compound_interest:.2f}")
print(f"Total Amount: {total_amount:.2f}")