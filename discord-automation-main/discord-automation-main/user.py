from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os

class User:
    def __init__(self, email, password, url):
        self.email = email
        self.password = password
        self.url = url
        self.driver = webdriver.Chrome(service=Service(r"C:\Users\saira\Downloads\discord-automation-main\discord-automation-main\chromedriver.exe")) # replace with your chromedriver path
        self.driver.get(self.url)

    def login(self):
        """Login to Discord"""
        try:
            print("Logging in...")
            email_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))
            )
            email_field.send_keys(self.email)

            password_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="password"]'))
            )
            password_field.send_keys(self.password)
            password_field.send_keys(Keys.RETURN)

            # Wait for the user to be logged in
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-list-item-id="channels"]'))
            )
            print("Login successful.")
        except Exception as e:
            print(f"An error occurred during login: {e}")

    def choose(self, friend_name):
        """Choose the chat with a specific friend"""
        try:
            print(f"Searching {friend_name}...")
            search_box = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
            )
            search_box.send_keys(friend_name)
            
            friend_chat = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, f'//div[contains(text(), "{friend_name}")]'))
            )
            friend_chat.click()
            print(f"Selected chat with {friend_name}.")
        except Exception as e:
            print(f"An error occurred while choosing the chat: {e}")

    def send_message(self, msg):
        """Send messages to the selected chat"""
        try:
            print("Sending message...")
            msg_field = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="textbox"]'))
            )
            msg_field.click()  # Ensure the field is focused
            msg_field.send_keys(msg)
            msg_field.send_keys(Keys.RETURN)
            self.log(msg)
            print("Message sent.")
        except Exception as e:
            print(f"An error occurred while sending the message: {e}")

    def send_image_js(self, file_path):
        """Send an image file to the chat using JavaScript"""
        try:
            if not os.path.isfile(file_path):
                raise FileNotFoundError(f"The file {file_path} does not exist.")
            
            print(f"Sending image from {file_path}...")
            
            # Locate the file input element
            upload_button = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="file"]'))
            )
            
            # Use JavaScript to set the value of the file input
            self.driver.execute_script(f"arguments[0].style.display = 'block';", upload_button)
            self.driver.execute_script(f"arguments[0].setAttribute('value', '{file_path}');", upload_button)
            
            # Click the upload button
            upload_button.send_keys(file_path)
            
            # Wait for the file to be processed and sent
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'img[src*="data:image"]'))
            )
            print("Image sent.")
        except Exception as e:
            print(f"An error occurred while sending the image: {e}")

    def logout(self):
        """Logout from Discord"""
        try:
            print("Logging out...")
            user_settings = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-list-item-id="settings"]'))
            )
            user_settings.click()
            
            logout_button = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Log Out")]'))
            )
            logout_button.click()
            
            WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))
            )
            print("Logout successful.")
        except Exception as e:
            print(f"An error occurred during logout: {e}")

    def log(self, msg):
        """Message log"""
        t = datetime.now().strftime('%H:%M:%S')
        print(f'[{t}] MESSAGE: {msg}')