from selenium import webdriver # Import webdriver from Selenium
import unittest # Import unittest
from Pages.homePage import HomePage # Home page imported to access the class
from Pages.loginPage import LoginPage # Login page imported to access the class
from Pages.myaccountPage import MyaccountPage

class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox() # Invoke chrome driver just at the begining of test execution
        cls.driver.get("https://igavesti-ou.myshopify.com/")  # Open the URL at the beginning of test


    def test_01_valid_login(self):
        driver = self.driver # Setup driver variable to self.driver so no need to type self.driver each time
        home = HomePage(driver) # A variable for home, driver instance passed because this argument added to constructor of HomePage
        login = LoginPage(driver) # A variable for login, driver instance passed because this argument added to constructor of LoginPage
        my_account = MyaccountPage(driver) # A variable for my account, driver instance passed because this argument added to constructor of MyaccountPage

        home.click_customer_login_link() # Click on Login link
        login.enter_email('azadtestlio@gmail.com')  # Enter the email
        login.enter_password('Tester1234')  # Enter the password
        login.click_on_sign_in_button()  # Click on submit button
        self.assertEqual(my_account.get_section_header_text(), "My Account") # Verify header of the page is My Account
        my_account.click_on_logout()  # Need to sign out after this test for the next one


    def test_02_invalid_login(self):
        driver = self.driver # Setup driver variable to self.driver so no need to type self.driver each time
        home = HomePage(driver)  # A variable for home, driver instance passed because this argument added to construction of LoginPage
        login = LoginPage(driver)  # A variable for login, driver instance passed because this argument added to construction of LoginPage

        home.click_customer_login_link()  # Click on Login link
        login.enter_email('azadtestlio@gmail.com')  # Enter the email
        login.enter_password('Tester1234')  # Enter the password
        login.click_on_sign_in_button()  # Click on submit button
        assert 'Incorrect email or password.' in driver.page_source # Verify error is shown

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() # Quit the browser

if __name__ == '__main__':
    unittest.main()