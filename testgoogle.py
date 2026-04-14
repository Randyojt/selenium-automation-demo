from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Start browser
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find search box
search_box = driver.find_element(By.NAME, "q")

# Input keyword
search_box.send_keys("Selenium Python")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait for results
time.sleep(3)

# Validate result
assert "Selenium" in driver.title

print("Test Passed")

# Close browser
driver.quit()
