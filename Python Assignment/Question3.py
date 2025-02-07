def email_slicer(email):
    try:
        username, domain = email.split("@")
        return username, domain
    except ValueError:
        return None, None

# Get user input
email = input("Enter your email address: ").strip()

# Process email
username, domain = email_slicer(email)

# Display output
if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email format. Please enter a valid email.")
