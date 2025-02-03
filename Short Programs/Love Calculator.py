name1 = input("Your name: ").lower()
name2 = input("Crush's name: ").lower()
score = sum(ord(c) for c in name1+name2) % 101
print(f"💖 Love Score: {score}% 💖")  # Always gets laughs!