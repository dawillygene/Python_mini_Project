from datetime import datetime
xmas = datetime(2025,12,25)
today = datetime.now()
print(f"🎄 {(xmas - today).days} days until Christmas!")