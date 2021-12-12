from telnetlib import EC

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import logging

from selenium.webdriver.support.wait import WebDriverWait

PATH_TO_CHROME_DRIVER = './webdrivers/chromedriver.exe'
PATH_TO_GECKO_DRIVER = './webdrivers/geckodriver.exe'

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600


def pepper_test(is_chrome):
    if is_chrome:
        driver = webdriver.Chrome(service=Service(PATH_TO_CHROME_DRIVER), options=webdriver.ChromeOptions())
    else:
        driver = webdriver.Firefox(service=Service(PATH_TO_GECKO_DRIVER), options=webdriver.FirefoxOptions())

    driver.set_window_position(0, 0)
    driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    logging.info(f'Loading page: https://www.pepper.pl')
    driver.get('https://www.pepper.pl')

    time.sleep(1)

    cookies_login = driver.find_element(By.CSS_SELECTOR, 'span[class="btn btn--mode-primary overflow--wrap-on"]')
    cookies_login.click()

    time.sleep(4)

    logging.info(f'Searching for account button')
    account_button = driver.find_element(By.CSS_SELECTOR, 'button[class=" btn btn--mode-header btn--toW5-square space--ml-2"]')
    account_button.click()

    time.sleep(1)

    logging.info(f'Searching for login input')
    login_input = driver.find_element(By.ID, 'loginModalForm-identity')
    login_input.send_keys("some_login")

    logging.info(f'Searching for password input')
    password_input = driver.find_element(By.ID, 'loginModalForm-password')
    password_input.send_keys("some_password")

    logging.info(f'Searching for remember user checkbox')
    remember_user_checkbox = driver.find_element(By.CSS_SELECTOR, 'span[class="checkbox-box flex--inline boxAlign-jc--all-c boxAlign-ai--all-c"]')
    remember_user_checkbox.click()

    logging.info(f'Searching for login button')
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[class="btn cept-login-submit btn width--all-12"]')
    login_button.click()

    time.sleep(1)

    logging.info(f'Searching for wrong credentials message')
    wrong_credentials_message = driver.find_element(By.CSS_SELECTOR, 'p[class="formList-info formList-info--error"]')

    logging.info(f'Wrong credentials message: {wrong_credentials_message.text}')
    expected_message = "Nieprawidłowe hasło Wygląda na to że wpisałeś złe hasło. Spróbuj ponownie."
    logging.info(f'Expected wrong credentials message: {expected_message}')

    if wrong_credentials_message.text.strip() == expected_message.strip():
        logging.info(f'Wrong credentials message match, test passed')
    else:
        logging.error(f'Wrong credentials message mismatch, test failed')

    driver.quit()


def xkom_test(is_chrome):
    if is_chrome:
        driver = webdriver.Chrome(service=Service(PATH_TO_CHROME_DRIVER), options=webdriver.ChromeOptions())
    else:
        driver = webdriver.Firefox(service=Service(PATH_TO_GECKO_DRIVER), options=webdriver.FirefoxOptions())

    driver.set_window_position(0, 0)
    driver.set_window_size(WINDOW_WIDTH, WINDOW_HEIGHT)

    logging.info(f'Loading page: https://www.x-kom.pl/p/689598-procesory-intel-core-i5-intel-core-i5-12600k.html')
    driver.get('https://www.x-kom.pl/p/689598-procesory-intel-core-i5-intel-core-i5-12600k.html')

    logging.info(f'Searching for div elements with class="sc-13p5mv-3 gATTUl"')
    processor_series = driver.find_elements(By.CSS_SELECTOR, 'div[class="sc-13p5mv-3 gATTUl"]')
    logging.info(f'Found processor series: {processor_series[1].text}')
    expected_series = 'i5-12600K'
    logging.info(f'Expected processor series: {expected_series}')

    if processor_series[1].text.strip() == expected_series.strip():
        logging.info(f'Processor series match, test passed')
    else:
        logging.error(f'Processor series mismatch, test failed')

    driver.quit()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

    logging.info(f'Performing x-kom test on chrome webdriver')
    xkom_test(True)

    logging.info(f'Performing x-kom test on gecko webdriver')
    xkom_test(False)

    logging.info(f'Performing pepper test on chrome webdriver')
    pepper_test(True)

    logging.info(f'Performing pepper test on gecko webdriver')
    pepper_test(False)
