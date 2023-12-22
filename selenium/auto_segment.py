import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


def login(driver, username, password):
    # Open the website
    driver.get("https://dev.synergi.ai/")
    driver.maximize_window()

    # Enter username
    driver.find_element("id", "email").send_keys(username)

    # Enter password
    driver.find_element("id", "password").send_keys(password)

    # Click on the login button
    driver.find_element(By.CSS_SELECTOR, ".MuiButton-containedSecondary").click()
    time.sleep(6)


def navigate_to_segments(driver):
    # Navigate to a Segment section
    driver.find_element(By.XPATH, "//span[normalize-space()='Segments']").click()
    time.sleep(6)


def create_segment(driver):
    # Create Segment
    driver.find_element(By.XPATH, "//button[normalize-space()='create Segment']").click()
    time.sleep(6)


def edit_segment(driver, segment_name):
    # Select Edit
    driver.find_element(By.XPATH, "//button[normalize-space()='Edit']").click()
    time.sleep(4)

    # Enter segment name
    driver.find_element("id", "segmentName").send_keys(segment_name)
    time.sleep(2)

    # Review
    driver.find_element(By.XPATH, "//button[normalize-space()='Review']").click()
    time.sleep(12)

    # Save Segment
    driver.find_element(By.XPATH, "//button[normalize-space()='Save Segment']").click()
    time.sleep(10)

    # Manage Segment
    driver.find_element(By.CSS_SELECTOR, "button[class='MuiButton-root']").click()
    time.sleep(10)


def conservative(driver):
    create_segment(driver)

    # Enter segment name for editing
    segment_name = " 10101"

    # Create Conservative Carla
    driver.find_element(By.XPATH, "//div[4]/button[1]").click()
    time.sleep(9)

    edit_segment(driver, segment_name)


def invester(driver):
    create_segment(driver)

    # Enter segment name for editing
    segment_name = " 10101"

    # Create Investor Ian
    driver.find_element(By.XPATH, "//div[2]/div/button").click()
    time.sleep(9)

    edit_segment(driver, segment_name)


def downsizer(driver):
    create_segment(driver)

    # Enter segment name for editing
    segment_name = " 10101"

    # Create Downsizer Dave
    driver.find_element(By.CSS_SELECTOR, "div:nth-child(3) div:nth-child(4) button:nth-child(1)").click()
    time.sleep(9)

    edit_segment(driver, segment_name)


def first_time_freddy(driver):
    create_segment(driver)

    # Enter segment name for editing
    segment_name = " 10101"

    # Create Investor Ian
    driver.find_element(By.XPATH, "//button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[4]//div[4]//button[1]").click()
    time.sleep(9)

    edit_segment(driver, segment_name)


def prepayers(driver):
    create_segment(driver)

    # Enter segment name for editing
    segment_name = " 10101"

    # Create Investor Ian
    driver.find_element(By.XPATH, "//button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[5]//div[4]//button[1]").click()
    time.sleep(9)

    edit_segment(driver, segment_name)


def segment():
    try:
        # Create a webdriver instance
        driver = webdriver.Chrome()

        # login credentials
        username = "ketulpadariya79@gmail.com"
        password = "Ketul@123"

        login(driver, username, password)
        navigate_to_segments(driver)
        conservative(driver)
        invester(driver)
        downsizer(driver)
        prepayers(driver)

    except Exception as e:
        print(e)

    finally:
        driver.quit()


# Call the function
segment()
