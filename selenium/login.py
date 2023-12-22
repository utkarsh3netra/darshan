import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(20)
driver.get("https://dev.synergi.ai/")

username = "ketulpadariya79@gmail.com"
password = "Ketul@123"
#username password type

driver.find_element("id", "email").send_keys(username)

driver.find_element("id", "password").send_keys(password)

#login button
#driver.find_element(By.XPATH, "//div/button/button[1]").click()
driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()

#select segment
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > a:nth-child(4) > div:nth-child(1) > div:nth-child(1)").click()

#Create Segment
driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-zu44x").click()

#crete Conservative Carla
driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiButton-root.MuiButton-text.MuiButton-textPrimary.MuiButton-sizeMedium.MuiButton-textSizeMedium.css-dvwafp").click()

# Select Edit
driver.find_element(By.CSS_SELECTOR,"button.css-cz5i37").click()

#segment name type
segment_name = " 1111"
driver.find_element("id", "segmentName").send_keys(segment_name)

#Review
driver.find_element(By.XPATH,'//*[@id="root"]/div[1]/div[2]/div/div[2]/div[2]/div/div[2]/div[3]/form/div/div[12]/button[2]').click()

#Save Sagment
driver.find_element(By.CSS_SELECTOR,"button.MuiButtonBase-root.MuiButton-root.MuiButton-contained.MuiButton-containedPrimary.MuiButton-sizeMedium.MuiButton-containedSizeMedium.css-1hw9j7s").click()

driver.find_element(By.CSS_SELECTOR,"button[type='submit'][variant='contained'].MuiButton-root").click()
