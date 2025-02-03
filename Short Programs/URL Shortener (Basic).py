import hashlib
url = input("Enter URL: ")
short_url = hashlib.md5(url.encode()).hexdigest()[:6]
print(f"Short URL: https://short.url/{short_url}")