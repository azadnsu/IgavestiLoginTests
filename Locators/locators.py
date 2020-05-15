class Locators():

    # Homepage Locators
    customer_login_link_id = 'customer_login_link'

    # Login page locators
    customer_email_id = 'CustomerEmail'  # id for customer email field
    customer_password_id = 'CustomerPassword'  # id for customer password field
    sign_in_button_xpath = "//form[@id='customer_login']//input[@class='btn']"  # xpath of sign in button

    # My Account page locators
    customer_logout_link_id = 'customer_logout_link'  # logout link id
    section_header_title_class_name = "section-header__title"  # Class name of section header title