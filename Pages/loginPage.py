from Locators.locators import Locators

class LoginPage():

    def __init__(self, driver):
        self.driver = driver
        self.customer_email_id = Locators.customer_email_id
        self.customer_password_id = Locators.customer_password_id
        self.sign_in_button_xpath = Locators.sign_in_button_xpath


    def enter_email(self, customer_email): # Method for entering email
        self.driver.find_element_by_id(self.customer_email_id).send_keys(customer_email)  # Enter the email

    def enter_password(self, customer_password): # Method for entering password
        self.driver.find_element_by_id(self.customer_password_id).send_keys(customer_password)  # Enter the password

    def click_on_sign_in_button(self):
        self.driver.find_element_by_xpath(self.sign_in_button_xpath).click()  # Click on submit button