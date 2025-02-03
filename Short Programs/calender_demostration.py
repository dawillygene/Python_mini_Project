import datetime

def create_calendar(year, month):  
    first_day = datetime.date(year, month, 1).weekday()  # 0=Monday, 6=Sunday  

    # Handle December case properly
    if month == 12:
        next_month = datetime.date(year + 1, 1, 1)
    else:
        next_month = datetime.date(year, month + 1, 1)

    days_in_month = (next_month - datetime.date(year, month, 1)).days  

    print("Mo Tu We Th Fr Sa Su")  
    print("   " * first_day, end="")  

    for day in range(1, days_in_month + 1):  
        print(f"{day:2}", end=" ")  
        if (day + first_day) % 7 == 0:  
            print()  
    print()  

# Example usage  
create_calendar(2023, 12)
