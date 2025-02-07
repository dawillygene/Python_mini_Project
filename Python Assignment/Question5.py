import time


def countdown_timer(total_time):
    while total_time:
       
        mins, secs = divmod(total_time, 60)
        timer = f"Timmer : {mins:02d}:{secs:02d}"
        print(timer, end="\r")  
        time.sleep(1)  
        total_time -= 1  

    print("Time's up!")


try:
    total_time = int(input("Enter the countdown time in seconds: "))
    countdown_timer(total_time)
except ValueError:
    print("Please enter a valid number of seconds.")