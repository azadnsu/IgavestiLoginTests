from Locators.locators import Locators

class HomePage(): # Homepage class

    def __init__(self, driver): # Constructor

        self.driver = driver
        self.customer_login_link_id = Locators.customer_login_link_id # ID of the customer login link which is in Homepage

    def click_customer_login_link(self): # Method to click on login link
        self.driver.find_element_by_id(self.customer_login_link_id).click()


