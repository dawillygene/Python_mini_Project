import random

def get_valid_input(prompt):
  
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def roll_dice(num_dice, num_sides):
   
    rolls = [random.randint(1, num_sides) for _ in range(num_dice)]
    total = sum(rolls)
    return rolls, total

def main():
    print("Welcome to Dice Roller!")
    while True:
    
        num_dice = get_valid_input("\nHow many dice would you like to roll? ")
        num_sides = get_valid_input("How many sides should each die have? ")
        
       
        rolls, total = roll_dice(num_dice, num_sides)
        
       
        print(f"\nRolling {num_dice} {'die' if num_dice == 1 else 'dice'} with {num_sides} sides:")
        for i, roll in enumerate(rolls, 1):
            print(f"  Die {i}: {roll}")
        print(f"Total sum: {total}\n")
        
      
        repeat = input("Roll again? (y/n): ").lower()
        if repeat != 'y':
            print("Thanks for rolling!")
            break

if __name__ == "__main__":
    main()
