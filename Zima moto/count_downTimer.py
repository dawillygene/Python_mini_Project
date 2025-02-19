

def count_downTimer(second):
    while second > 0:
        mins,sec = divmod(second,60)
        print(f"min{mins:02} : {sec:02}", end="\r")
        time.sleep(1)
        second -= 1
