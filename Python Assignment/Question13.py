import random

symbols = ["🍒", "🍋", "🍉", "🔔", "⭐"]

def spin_reels():
  
    return [random.choice(symbols) for _ in range(3)]

def calculate_payout(spin_result, bet_amount):

    if spin_result[0] == spin_result[1] == spin_result[2]:
        return bet_amount * 10  
    elif spin_result[0] == spin_result[1]:
        return bet_amount * 3  
    else:
        return 0  

def play_slot_machine():
    print("\n🎰 Welcome to the Slot Machine! 🎰")
    
    balance = float(input("Enter your starting balance: $"))

    while balance > 0:
        print(f"\nYour current balance: ${balance:.2f}")
        bet = float(input("Enter your bet amount: $"))

        if bet > balance:
            print("❌ Not enough balance. Please enter a smaller bet.")
            continue
        
   
        spin_result = spin_reels()
        print(f"🎰 {spin_result[0]} | {spin_result[1]} | {spin_result[2]} 🎰")

 
        winnings = calculate_payout(spin_result, bet)
        if winnings > 0:
            print(f"🎉 You won ${winnings:.2f}! 🎉")
        else:
            print("💔 You lost this round.")

    
        balance -= bet
        balance += winnings

     
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("\n💸 Game Over! Thank you for playing. 💸")


play_slot_machine()
