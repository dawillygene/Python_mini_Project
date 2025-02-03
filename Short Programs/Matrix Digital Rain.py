import os, time
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("".join([str(randint(0,1)) for _ in range(50)]))
    time.sleep(0.1)