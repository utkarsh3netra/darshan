import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a webdriver instance
driver = webdriver.Chrome()

# Open the website
driver.get("https://dev.synergi.ai/")
driver.maximize_window()

# login credentials
username = "ketulpadariya79@gmail.com"
password = "Ketul@123"

# Enter username
driver.find_element("id", "email").send_keys(username)

# Enter password
driver.find_element("id", "password").send_keys(password)

# Click on the login button
driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()
time.sleep(6)

# Navigate to a Segment section
driver.find_element(By.XPATH, "//span[normalize-space()='Segments']").click()
time.sleep(6)

# Create Segment
driver.find_element(By.XPATH, "//button[normalize-space()='create Segment'] ").click()
time.sleep(6)

# Create Conservative Carla
driver.find_element(By.XPATH, "//div[@id='root']//div[@class='MuiBox-root css-3bcwuz']/div//div/div/div/button").click()
time.sleep(6)

# Select Edit
driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()
time.sleep(4)

# Enter segment name
segment_name = " 1129"
driver.find_element("id", "segmentName").send_keys(segment_name)
time.sleep(2)

# Review
driver.find_element(By.XPATH, "//button[normalize-space()='Review']").click()
time.sleep(6)

# Save Segment
driver.find_element(By.XPATH, "//button[normalize-space()='Save Segment']").click()
time.sleep(6)

# Manage Segment
driver.find_element(By.CSS_SELECTOR, "button[class='MuiButton-root']").click()
time.sleep(6)

# Close the browser
driver.quit()
