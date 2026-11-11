from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def scroll_to_element(self, element):

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )

        print("Scrolled to the element successfully")

    def wait_until_element_is_clickable(self,locator_type,locator):
        element = self.wait.until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        return element
    def wait_until_element_is_present(self,locator_type,locator):
        element = self.wait.until(
            EC.presence_of_element_located((locator_type, locator))

        )
        return element
    def wait_until_element_is_visible(self,locator_type,locator):
        element = self.wait.until(
            EC.visibility_of_element_located((locator_type, locator))
        )
        return element
    def wait_until_all_elements_is_visible(self,locator_type,locator):
        element = self.wait.until(
            EC.visibility_of_all_elements_located((locator_type, locator))
        )
        return element