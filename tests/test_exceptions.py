import time

from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.exceptions_page import ExceptionsPage


class TestExceptions:
    @pytest.mark.exceptions

    def test_no_such_element_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it is not."


    @pytest.mark.exceptions
    def test_element_not_interactable_exception(self, driver):
        # Open page
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("Sushi")
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message isn't expected"

    @pytest.mark.exceptions

    def test_invalid_element_state_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.clear_row_1()
        exception_page.add_first_food("Bread")
        assert exception_page.get_attribute_row1("value") == "Bread", "Text row 1 is not expected."

    @pytest.mark.exceptions
    def test_stale_element_reference_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert not exception_page.are_instruction_displayed(), "Text instruction is displayed."

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        assert exception_page.is_row2_displayed(), "Row 2 input should be displayed, but it is not."
