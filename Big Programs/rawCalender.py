def day_of_week(y, m, d):

    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if m < 3:
        y -= 1
    return (y + y // 4 - y // 100 + y // 400 + t[m - 1] + d) % 7

def days_in_month(m, y):
    if m == 2:
        return 29 if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)) else 28
    return 30 if m in {4, 6, 9, 11} else 31


month, year = 12, 2012
month_names = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]


dow = day_of_week(year, month, 1)
header_index = (dow + 6) % 7  

total_days = days_in_month(month, year)
weeks = []
current_day = 1


week = ['  '] * header_index
days_left_in_week = 7 - header_index
for _ in range(days_left_in_week):
    week.append(f"{current_day:2d}")
    current_day += 1
weeks.append(week)


while current_day <= total_days:
    week = []
    for _ in range(7):
        if current_day > total_days:
            week.append('  ')
        else:
            week.append(f"{current_day:2d}")
            current_day += 1
    weeks.append(week)

print(f"{month_names[month - 1]} {year}")
print("Mo Tu We Th Fr Sa Su")
for week in weeks:
    print(' '.join(week).rstrip())