from dotenv import load_dotenv
from selenium import webdriver
from undetected_chromedriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import os
import time

# Solving Captchas



# Grammarly Login
load_dotenv()
grammar_email = str(os.getenv("GRAMMARLY_EMAIL"))
grammar_pass = str(os.getenv("GRAMMARLY_PASSWORD"))

# Setting options for our chrome instance
options = webdriver.ChromeOptions()
# Use chrome profile to keep logged in to services (not working, cannot figure out why)
# options.add_argument("--user-data-dir=C:\\Users\\kyleb\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
# Keeps the window open after task is completed
options.add_experimental_option("detach", True)
# Adding fake useragent into the session

# Selecting our webdriver for selenium to use
driver = webdriver.Chrome(options = options)

# Function for checking which page we are on based on the title
def condition_check(title: str):
    # Grammarly titles:
    # Login page = "Login | Grammarly"
    # Home page = "My - Grammarly"
    # Doc open = " - Grammarly"
    title_check = driver.title
    if title_check == title:
        return True
    else:
        return False

# Function for logging into grammarly
def grammarly_login(driver, email, password):
    # Go to Grammarly
    driver.get("https://grammarly.com/signin")
    
    WebDriverWait(driver, timeout = 10).until(ec.title_is("Login | Grammarly"))
    # Signing into grammarly email field (TEMP UNTIL PROFILE WORKS)
    # Check for email button to verify its existance
    WebDriverWait(driver, timeout = 7).until(ec.element_to_be_clickable((By.ID, "email")))
    assert "email" in driver.page_source
    # Find email input
    email_field = driver.find_element(by=By.ID, value = "email")
    # Clears whatever is in email field (just in case)
    email_field.clear()
    # Type in email for Grammarly account. Get email from .env
    email_field.send_keys(email)

    # Confirming continue button
    assert "base_basic__8rArQ" in driver.page_source
    # Finding continue button, and clicking it
    continue_button = driver.find_element(by = By.CLASS_NAME, value = "base_basic__8rArQ")
    continue_button.click()

    # Confirming password field
    WebDriverWait(driver, timeout = 7).until(ec.element_to_be_clickable((By.ID, "password")))
    assert "password" in driver.page_source
    # Finding password field
    pass_field = driver.find_element(by = By.ID, value = "password")
    # Inserting password into field
    pass_field.send_keys(password)

    # Confirming signin button
    assert "base_text__vPnqO" in driver.page_source
    # Finding the signin button and signing in
    signin = driver.find_element(by = By.CLASS_NAME, value = "base_text__vPnqO")
    signin.click()

grammarly_login(driver, grammar_email,grammar_pass)
# Uses WebDriverWait and Expected_Conditions to wait until a condition is met.
# In this case, until there is an object, which is clickable, which has the class name "_54ecb82a-document-item-add"
WebDriverWait(driver, timeout = 7).until(ec.element_to_be_clickable((By.CLASS_NAME, "_54ecb82a-document-item-add")))

# Creating a new document
# Find the new document button and click
create_doc = driver.find_element(by=By.CLASS_NAME, value = "_54ecb82a-document-item-add")
create_doc.click()