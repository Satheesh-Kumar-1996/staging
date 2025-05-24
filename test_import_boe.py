import pytest
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Src.login import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import subprocess

def upload_file_linux(driver, input_locator, file_path, timeout=20):
    # Wait for the file-input to be in the DOM
    file_input = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(input_locator)
    )
    # Un-hide it (if styled hidden by the dropzone)
    driver.execute_script(
        """
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.height = '1px';
        arguments[0].style.width = '1px';
        """,
        file_input
    )
    # Send the absolute path
    file_input.send_keys(file_path)
    return file_input

# Fixture to initialize WebDriver
@pytest.fixture()
def driver():
    # Initialize ChromeOptions
    options = Options()

    # Setting preferences to disable password manager, notifications, etc.
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    # Remove "Chrome is being controlled by automated test software" banner
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # Disable the "Chrome Automation Extension"
    options.add_experimental_option('useAutomationExtension', False)
    # Hide the Selenium detection
    options.add_argument("--disable-blink-features=AutomationControlled")
    # Initialize the driver with options
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    # Open the login page
    driver.get("https://staging.bharathexim.com/login")

    # Maximize the browser window
    driver.maximize_window()

    # Yield the driver to use it in the test
    yield driver

    # Quit the driver after the test is done
    driver.quit()


# Login function (assuming you have these methods defined)
def login(driver):
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)


def wait_for_loader_to_disappear(driver, timeout=60):
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.CLASS_NAME, "loading-main"))
    )

def test_commercial_pass(driver):
        login(driver)
        radiobutton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='checkbox']")))
        wait_for_loader_to_disappear(driver)
        radiobutton.click()
        documents = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Documents']")))
        wait_for_loader_to_disappear(driver)
        documents.click()
    #PIPO
        wait_for_loader_to_disappear(driver)
        WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//h6[normalize-space()='PI / PO / Order Copy']"))).click()
    #Add new
        wait_for_loader_to_disappear(driver)
        WebDriverWait(driver, timeout=30).until(EC.presence_of_element_located((By.XPATH, "//button[@class='upload-button btn btn-success ng-star-inserted']"))).click()
    #check box
        wait_for_loader_to_disappear(driver)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='checkbox'])[1]"))).click()
        wait_for_loader_to_disappear(driver)
        file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
        upload_file_linux(driver, file_input_locator, "/home/sathish/Desktop/Aug.pdf")
        wait_for_loader_to_disappear(driver)
        #boe Date
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='date'])[3]"))).send_keys("12/05/2025")
        #boe number
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@type='text'])[3]"))).send_keys("test")
        #boe currency
        #WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "//label[@class='form-label-control ng-star-inserted']")))
        #boe_amount
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[5]"))).send_keys("4000")
        #port code
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[6]"))).send_keys("20")
        #awbno
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[7]"))).send_keys("a12344567")
        #origin
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[8]"))).send_keys("test")
        #portofloading
        WebDriverWait(driver,timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[9]"))).send_keys("chennai")
        #adcode
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[10]"))).send_keys("122345")
        #FREIGHT VALUE
        WebDriverWait(driver, timeout=20).until((EC.element_to_be_clickable((By.XPATH, "//input[@class='form-control ng-pristine ng-valid ng-touched']")))).send_keys("1234567")
        #MISCELLANEOUS AMOUNT
        WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "")))
