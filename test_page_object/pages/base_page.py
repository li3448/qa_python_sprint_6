from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element_with_wait(self, locator):
        (WebDriverWait(self.driver, 5).
         until(expected_conditions.visibility_of_element_located(locator)))
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.click()

    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        return element.text

    def add_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        element.send_keys(text)

    def change_modal(self, locator):
        modal = self.find_element_with_wait(locator)
        self.driver.switch_to.frame(modal)

    def switch_to_new_window(self):
        main_window = self.driver.current_window_handle
        new_window = [window for window in self.driver.window_handles if window != main_window][0]
        self.driver.switch_to.window(new_window)
