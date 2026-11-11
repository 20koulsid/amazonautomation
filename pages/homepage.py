from base.base_driver import BasePage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def search_input(self,tv_search):
        search_placeholder = self.wait_until_element_is_clickable("xpath","//input[@id='twotabsearchtextbox']")
        search_placeholder.click()
        print(f"search placeholder was clicked")
        search_placeholder.send_keys(tv_search)
    def search_submit_button(self):
        search_submit_button = self.wait_until_element_is_clickable("xpath","//input[@id='nav-search-submit-button']")
        search_submit_button.click()