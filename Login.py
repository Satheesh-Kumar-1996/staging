import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from webdriver_manager.chrome import ChromeDriverManager
import pyotp


def start_driver():
    options = Options()
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")

    # Initialize driver using webdriver-manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver


def login(driver):
    """Perform the initial login steps."""
    driver.get("https://staging.bharathexim.com/login")
    time.sleep(2)
    # Handle alert
    alert = driver.switch_to.alert
    alert.accept()
    driver.maximize_window()
    time.sleep(4)


def username(driver):
    """Enter the username."""
    email_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter email id'])[1]")
    email_input.send_keys("Ddttester4@gmail.com")


def password(driver):
    """Enter the password."""
    password_input = driver.find_element(By.XPATH, "(//input[@placeholder='Enter password'])[1]")
    password_input.send_keys("test@1234")


def perform_login(driver):
    """Click the login button."""
    login_button = driver.find_element(By.XPATH, "(//button[normalize-space()='Login'])[1]")
    login_button.click()


def perform_otp(driver):
    # Example secret from QR code (must be base32 encoded, never share it)
    totp_secret = "MZKFUOJYFE2FOQZG"  # Replace with actual secret

    # Generate OTP
    totp = pyotp.TOTP(totp_secret)
    otp = totp.now()
    print("Generated OTP:", otp)
    time.sleep(4)
    if otp == totp.now():
        # Enter the OTP
        autherntication = driver.find_element(By.XPATH, "(//input[@placeholder='Enter 6 digit Google Auth OTP'])[1]")

        autherntication.send_keys(otp)

    else:
        print(otp)
        print("Enter the OTP correctly")
        driver.quit()


# Main function
if __name__ == "__main__":
    driver = start_driver()
    # Execute the steps
    login(driver)
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)
    time.sleep(10)


