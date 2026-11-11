import pytest

import configfiles
from pages.cartpage import CartPage
from pages.loginpage import LoginPage
from pages.searchresultpage import SearchResultPage
from pages.launchpage import LaunchPage
from pages.homepage import HomePage
from utilities import Utils


@pytest.mark.usefixtures("setUp")
class TestMainFile:

    def test_main_file(self):
        # Launch Page
        launch_page = LaunchPage(self.driver)
        utils = Utils()
        utils.assert_title(configfiles.actual_title, configfiles.expected_title)
        launch_page.login_section()

        # Login
        login_page = LoginPage(self.driver)
        login_page.username(configfiles.email)
        login_page.submit_username()
        login_page.email_proceed()
        login_page.password_input(configfiles.password)
        login_page.password_submit()

        # Home Page - Search TV
        home_page = HomePage(self.driver)
        home_page.search_input(configfiles.tv_search)
        home_page.search_submit_button()

        # Search Results Page
        product_page = SearchResultPage(self.driver)
        product_page.search_result_page()
        product_page.add_to_cart()
        product_page.cart()

        # carts page - proceed the product to buy
        carts_page = CartPage(self.driver)
        carts_page.proceed_product_buying()






