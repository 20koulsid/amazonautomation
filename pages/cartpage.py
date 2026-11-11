from base.base_driver import BasePage


class CartPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
    def proceed_product_buying(self):
        proceed_button = self.wait_until_element_is_clickable("xpath","/html[1]/body[1]/div[1]/div[1]/div[4]/div[6]/div[1]/div[1]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]/span[1]/span[1]/span[1]/input[1]")
        proceed_button.click()
        print(f"Proceed button is clicked")
        print(f"the product is ready to be purchased")
