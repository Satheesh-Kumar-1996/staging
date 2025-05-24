import time

import pytest
from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support import wait
from Src.login import *

def wait_for_loader_to_disappear(driver, timeout=40):
    try:
        WebDriverWait(driver, timeout).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "loading-main"))
        )
    except TimeoutException:
        print("Loader did not disappear within the timeout.")

def login(driver):
    username(driver)
    password(driver)
    perform_login(driver)
    perform_otp(driver)
    perform_login(driver)

def upload_file_linux(driver, input_locator, file_path, timeout=20):
    file_input = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located(input_locator)
    )
    driver.execute_script(
        """
        arguments[0].style.display = 'block';
        arguments[0].style.visibility = 'visible';
        arguments[0].style.height = '1px';
        arguments[0].style.width = '1px';
        """,
        file_input
    )
    file_input.send_keys(file_path)
    return file_input

@pytest.fixture()
def driver():
    options = Options()
    prefs = {
        "profile.password_manager_enabled": False,
        "credentials_enable_service": False,
        "profile.default_content_setting_values.notifications": 2
    }
    options.add_experimental_option("prefs", prefs)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://staging.bharathexim.com/login")
    driver.maximize_window()
    yield driver
    driver.quit()

def test_import_pipo(driver):
    login(driver)
    radiobutton = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@for='checkbox']")))
    radiobutton.click()
    wait_for_loader_to_disappear(driver)
    documents = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Documents']"))
    )
    documents.click()

    wait_for_loader_to_disappear(driver)

    pipo = WebDriverWait(driver, timeout=30).until(
        EC.element_to_be_clickable((By.XPATH, "//h6[normalize-space()='PI/PO Summary']"))
    )
    pipo.click()
    wait_for_loader_to_disappear(driver)
    Add_new = WebDriverWait(driver, timeout=30).until(
         EC.element_to_be_clickable((By.XPATH, "//button[@class='upload-button btn btn-success ng-star-inserted']"))
     )
    wait_for_loader_to_disappear(driver)
    time.sleep(1)
    Add_new.click()
    time.sleep(10)
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    wait_for_loader_to_disappear(driver)
    time.sleep(10)
    upload_file_linux(driver, file_input_locator, "/home/sathish/Satheesh/satz/2025/stagingsample/samplePDFFile.pdf")
    time.sleep(10)
    WebDriverWait(driver, timeout=20).until(
         EC.presence_of_element_located((By.XPATH, "(//input[@class='form-control col-11 pr-4'])[1]"))
     ).send_keys("12345we")
    time.sleep(3)
    WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "(//input[@aria-autocomplete='list'])[1]"))
    ).click()
    options= WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "(//span[@class='ng-option-label ng-star-inserted'])[2]")))
    options.click()
    time.sleep(2)
#types of goods
    Types_Goods = WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Raw Material']//div[@class='checkbox-border']")))
    Types_Goods.click()
    time.sleep(3)
#PIPO number
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='form-group mb-0 ng-star-inserted']//div[@class='form-group mb-0 ng-star-inserted']//input[@type='text']"))).send_keys("test123test")
#PIPO date
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[2]"))).send_keys("12/05/2025")
#Currency
    time.sleep(3)
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "(//div[@class='ng-input'])[2]")))
    WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='INR']"))).click()
    time.sleep(3)
#PI/PO Amount
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-control ng-pristine ng-valid ng-touched']"))).send_keys("20000")
    time.sleep(3)
#Incoterm
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-expanded='true']//input[@type='text']")))
    WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='FCA | Free to Carrier']"))).click()
    time.sleep(3)
#Branch
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-expanded='true']//input[@type='text']")))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//span[@class='ng-option-label ng-star-inserted']"))).click()
    time.sleep(3)
#Mode of Transport
    WebDriverWait(driver,timeout=10).until(EC.presence_of_element_located((By.XPATH, "//label[normalize-space()='Sea']//div[@class='checkbox-border']"))).click()
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located(( By.XPATH, "(//span[@class='mat-checkbox-inner-container'])[1]"))).click()
    time.sleep(3)
#payment
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//div[@aria-expanded='true']//input[@type='text']")))
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "(//span[@class='ng-option-label ng-star-inserted'])[1]"))).click()
    time.sleep(3)
#last date of shipment
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='input-container']//input[@type='date']"))).send_keys("19/05/2025")
    time.sleep(3)
#Amount
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//ng-input-number[@type='textbox']//input[@type='textbox']"))).send_keys("20000")
    time.sleep(3)
#submit
    WebDriverWait(driver, timeout=10).until(EC.presence_of_element_located((By.XPATH, "//button[@id='PIPO_IMPORT']"))).click()
    time.sleep(10)


def view(driver):
    wait_for_loader_to_disappear(driver)
    View_button = WebDriverWait(driver, timeout=20).until(
        EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class, 'PopupOpen') and @title='View'])[1]"))
    )

    try:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", View_button)
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "(//a[contains(@class, 'PopupOpen') and @title='View'])[1]")))
        View_button.click()
    except ElementClickInterceptedException:
        print("Click was intercepted, retrying after short wait...")
        time.sleep(2)
        driver.execute_script("arguments[0].click();", View_button)

    #time.sleep(60)
    overview = WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='header-panel ActiveClass']")))
    wait_for_loader_to_disappear(driver)
    overview.click()
    #time.sleep(60)
    wait_for_loader_to_disappear(driver)
    detail = WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//p[normalize-space()='Details']")))
    detail.click()
    Upload=WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "(//p[normalize-space()='Upload'])[1]")))
    wait_for_loader_to_disappear(driver)
    Upload.click()
    beneficiary = WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "(//input[@id='myDropdown'])[2]")))
    wait_for_loader_to_disappear(driver)
    beneficiary.click()
    beneficiary.send_keys("Tara Exports Ltd")
    wait_for_loader_to_disappear(driver)
    s_date = WebDriverWait(driver, timeout=1).until(EC.presence_of_element_located((By.XPATH, "//div[@class='width-100 show-filter ng-star-inserted']//div[2]//div[21]//input[1]")))
    s_date.send_keys("12/05/2025")
    wait_for_loader_to_disappear(driver)
    e_date = WebDriverWait(driver, timeout=1).until(EC.presence_of_element_located((By.XPATH, "//custom-hover-panel-import//div[3]//div[21]//input[1]")))
    e_date.send_keys("17/05/2025")
    file_input_locator = (By.CSS_SELECTOR, "input[type='file']")
    wait_for_loader_to_disappear(driver)
    upload_file_linux(driver, file_input_locator, "/home/sathish/Satheesh/satz/2025/Testing Notes/Python.pdf")
    time.sleep(20)
    WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "(//input[@class='form-control ng-untouched ng-pristine ng-valid'])[5]"))).send_keys("1223346")
    WebDriverWait(driver, timeout=20).until(EC.presence_of_element_located((By.XPATH, "//input[@class='form-control ng-pristine ng-valid ng-touched']"))).send_keys("5000")
    WebDriverWait(driver, timeout=20).until(EC.element_to_be_clickable((By.XPATH, "//form[@class='col-12 division-panel ng-invalid ng-touched ng-dirty']//input[@type='date']"))).send_keys("17/05/2025")