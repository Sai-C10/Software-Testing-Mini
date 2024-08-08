# test_send_message.py
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

# Choose the chat with the specific friend
friend_name = 'Vice_Cpt'  # Replace with the actual friend’s name
print(f"Choosing chat with {friend_name}...")
user.choose(friend_name)

# Send a message to the selected friend
message = 'Hello, this is a automated test !'
print(f"Sending message: {message}")
user.send_message(message)

user.driver.quit()