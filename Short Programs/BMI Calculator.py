weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
bmi = weight / (height ** 2)
print(f"Your BMI is {bmi:.2f}")