from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ExceptionsPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-exceptions/"
    __add_button = (By.XPATH, "//button[@id='add_btn']")
    __row_1_input_element = (By.XPATH, "//div[@id='row1']/input")
    __row_2_input_element = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")
    __row_1_save_button = (By.XPATH, "/html//button[@id='save_btn']")
    __row_2_save_button = (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']")
    __confirmation_element = (By.ID, "confirmation")
    __edit_button = (By.XPATH, "/html//button[@id='edit_btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)
    def add_second_row(self):
        super()._click(self.__add_button)
        super()._wait_until_element_is_visible(self.__row_2_input_element)

    def is_row2_displayed(self) -> bool:
        return super()._is_displayed(self.__row_2_input_element)

    def add_second_food(self, food: str):
        super()._type(self.__row_2_input_element, food)
        super()._click(self.__row_2_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)

    def add_first_food(self, food: str):
        super()._type(self.__row_1_input_element, food)
        super()._click(self.__row_1_save_button)
        super()._wait_until_element_is_visible(self.__confirmation_element)
    def get_confirmation_message(self) -> str:
        return super()._get_text(self.__confirmation_element, time = 3)

    def clear_row_1(self):
        super()._click(self.__edit_button, time = 3)
        super()._wait_until_element_is_clickable(self.__row_1_input_element)
        super()._clear(self.__row_1_input_element)

    def get_attribute_row1(self, attribute: str) -> str:
        return super()._get_attribute(self.__row_1_input_element, attribute)
