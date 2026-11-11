from base.base_driver import BasePage


class SearchResultPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def search_result_page(self):
        select_tv = self.wait_until_element_is_clickable("xpath","/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/a[1]")
        self.scroll_to_element(select_tv)
        print("TV selected:", select_tv.text.strip())
        self.scroll_to_element(select_tv)
    def add_to_cart(self):
        product_to_cart = self.wait_until_element_is_clickable("xpath","/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/div[1]/div[5]/div[1]/div[1]/span[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/div[1]/div[1]/span[1]/div[1]/div[1]/span[1]/span[1]")
        product_to_cart.click()
        print(f"Product was added to cart: {product_to_cart.text}")
    def cart(self):
        carts_section = self.wait_until_element_is_clickable("id","nav-cart")
        carts_section.click()
        print(f"carts section was selected")
