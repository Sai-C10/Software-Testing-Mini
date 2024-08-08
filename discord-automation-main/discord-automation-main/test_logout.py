from user import User
from time import sleep

# Read email and password from the file
with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()

# Create a User object with email, password, and login URL
user = User(email, password, 'https://discord.com/login')

# Log in and wait for the page to load
user.login()
print("Waiting for the page to load...")
sleep(25)  # Adjust this if needed

# Log out
user.logout()

# Print a message indicating successful logout
print("Successfully logged out")

# Quit the driver
user.driver.quit()
