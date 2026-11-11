from base.base_driver import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def username(self, email):
        email_input = self.wait_until_element_is_clickable("xpath","//input[@id='ap_email_login']")
        email_input.click()
        print(f"sign in section was clicked")
        email_input.send_keys(email)
    def submit_username(self):
        submit_button = self.wait_until_element_is_clickable("xpath","//input[@type='submit']")
        submit_button.click()
    def email_proceed(self):
        username_proceed = self.wait_until_element_is_clickable("xpath","//span[@id='auth-signin-button']")
        username_proceed.click()
    def password_input(self,password):
        password_input = self.wait_until_element_is_clickable("xpath","//input[@id='ap_password']")
        password_input.click()
        print(f"Password input was clicked")
        password_input.send_keys(password)
    def password_submit(self):
        password_submit = self.wait_until_element_is_clickable("xpath","//input[@id='signInSubmit']")
        password_submit.click()
        print(f"password submit button was clicked")
        print(f"The user is successfully logged in")
