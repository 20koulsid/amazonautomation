from base.base_driver import BasePage


class LaunchPage(BasePage):
    def login_section(self):
        signin = self.wait_until_element_is_clickable("xpath","//div[@id='nav-link-accountList']//a[1]")
        signin.click()
        print(f"sign in button was clicked on landing page")

    def get_page_title(self):
        return self.driver.title

