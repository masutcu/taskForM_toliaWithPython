
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import unittest

class Task14(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.service = Service('path/to/chromedriver')
        cls.service.start()
        cls.driver = webdriver.Remote(cls.service.service_url)
        cls.driver.maximize_window()
        cls.driver.get("http://automationexercise.com")

    def test_1_home_page_visibility(self):
        home_page = self.driver.find_element(By.TAG_NAME, "html")
        self.assertTrue(home_page.is_displayed())

    def test_2_add_to_cart_and_proceed_to_checkout(self):
        # Add products to cart
        # Assuming the products are added automatically in the page load, if not, you need to add the relevant code here

        # Click 'Cart' button
        cart_button = self.driver.find_element(By.XPATH, "//a[text()=' Cart']")
        cart_button.click()

        # Verify that cart page is displayed
        shopping_cart_page = self.driver.find_element(By.XPATH, "//*[text()='Shopping Cart']")
        self.assertTrue(shopping_cart_page.is_displayed())

        # Click Proceed To Checkout
        proceed_to_checkout_button = self.driver.find_element(By.XPATH, "//*[text()='Proceed To Checkout']")
        proceed_to_checkout_button.click()

    def test_3_create_account_and_verify_logged_in(self):
        # Click 'Register / Login' button
        self.driver.find_element(By.XPATH, "//u[text()='Register / Login']").click()
        sing_up_button = self.driver.find_element(By.XPATH, "//a[@href='/login']")
        sing_up_button.click()
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@data-qa='signup-name']").send_keys("Mehmet")
        self.driver.find_element(By.XPATH, "//input[@data-qa='signup-email']").send_keys("password19@gmail.com")
        time.sleep(1)
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.PAGE_DOWN).perform()

        sign_up = self.driver.find_element(By.XPATH, "//*[@data-qa='signup-button']")
        sign_up.submit()
        time.sleep(1)

        self.driver.back()
        self.driver.forward()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//u[text()='Register / Login']").click()
        time.sleep(1)

        # Fill signup form details
        self.driver.find_element(By.ID, "id_gender1").click()
        self.driver.find_element(By.ID, "password").send_keys("password2", Keys.ENTER)

        # Fill additional details
        date = self.driver.find_element(By.ID, "days")
        Select(date).select_by_value("11")

        month = self.driver.find_element(By.ID, "months")
        Select(month).select_by_value("3")

        year = self.driver.find_element(By.ID, "years")
        Select(year).select_by_visible_text("1979")

        # Select checkboxes
        check = self.driver.find_element(By.XPATH, "//label[@for='newsletter']")
        if not check.is_selected():
            check.click()

        check1 = self.driver.find_element(By.XPATH, "//label[@for='optin']")
        if not check1.is_selected():
            check1.click()

        actions.send_keys(Keys.PAGE_DOWN).perform()
        time.sleep(1)

        self.driver.find_element(By.ID, "first_name").send_keys("david")
        self.driver.find_element(By.ID, "last_name").send_keys("gold")
        self.driver.find_element(By.ID, "company").send_keys("milkyCompany")
        self.driver.find_element(By.ID, "address1").send_keys("Manhettan")
        self.driver.find_element(By.ID, "address2").send_keys("NewYorkCity")

        country = self.driver.find_element(By.ID, "country")
        Select(country).select_by_index(1)

        state = self.driver.find_element(By.ID, "state")
        state.send_keys("NYC")

        city = self.driver.find_element(By.ID, "city")
        city.send_keys("NewYork")

        zip = self.driver.find_element(By.ID, "zipcode")
        zip.send_keys("061525")

        

        tel = self.driver.find_element(By.ID, "mobile_number")
        tel.send_keys("5525252321")
        time.sleep(1)

        # Click 'Create Account' button
        create_account_button = self.driver.find_element(By.XPATH, "//button[@data-qa='create-account']")
        create_account_button.click()

        # Verify 'ACCOUNT CREATED!'
        account_created = self.driver.find_element(By.XPATH, "//h2[@data-qa='account-created']")
        self.assertTrue(account_created.is_displayed())

        # Click 'Continue' button
        self.driver.find_element(By.XPATH, "//a[text()='Continue']").click()

        # Verify 'Logged in as username'
        logged_in = self.driver.find_element(By.XPATH, "//a[text()=' Logged in as '] ")
        self.assertTrue(logged_in.is_displayed())

    def test_4_proceed_to_checkout_and_place_order(self):
        # Click 'Cart' button
        self.driver.find_element(By.XPATH, "//a[text()=' Cart']")