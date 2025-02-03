import time
seconds = int(input("Enter seconds: "))
for i in range(seconds, 0, -1):
    print(f"⏳ {i} seconds remaining...")
    time.sleep(1)
print("🎉 Time's up!")