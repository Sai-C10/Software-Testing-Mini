from user import User
from time import sleep

with open('account.txt') as f:
    email = f.readline().strip()
    password = f.readline().strip()

user = User(email, password, 'https://discord.com/login')

# Log in and wait for the page to load
user.login()
print("Waiting for the page to load...")
sleep(25)  # Adjust this if needed

user.driver.quit()