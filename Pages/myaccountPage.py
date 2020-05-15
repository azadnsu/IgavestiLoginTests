from Locators.locators import Locators

class MyaccountPage(): # My Account class

    def __init__(self,driver):

        self.driver = driver
        self.customer_logout_link_id = Locators.customer_logout_link_id
        self.section_header_title_class_name = Locators.section_header_title_class_name

    def click_on_logout(self):# Method to click on logout
        self.driver.find_element_by_id(self.customer_logout_link_id).click()

    def get_section_header_text(self): # Method to get text of section header
        self.driver.find_element_by_class_name(self.section_header_title_class_name).text()
