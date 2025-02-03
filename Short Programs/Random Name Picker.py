import random
names = input("Enter names (comma-separated): ").split(",")
print(f"🎉 The winner is... {random.choice(names).strip()}!")