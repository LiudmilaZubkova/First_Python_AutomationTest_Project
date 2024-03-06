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
    @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        exception_page = ExceptionsPage(driver)
        exception_page.open()
        exception_page.add_second_row()
        exception_page.add_second_food("Sushi")
        assert exception_page.get_confirmation_message() == "Row 2 was saved", "Confirmation message isn't expected"

    @pytest.mark.exceptions

    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Clear input field
        edit_button_locator = driver.find_element(By.XPATH, "/html//button[@id='edit_btn']")
        edit_button_locator.click()
        row_1_locator = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_locator))
        row_1_locator.clear()
        # Type text into the input field
        row_1_locator.send_keys("Bread")
        save_button_locator = driver.find_element(
            By.XPATH, "/html//button[@id='save_btn']")
        save_button_locator.click()
        # Verify text changed
        assert row_1_locator.get_attribute("value") == "Bread", "Text row 1 is not expected."

    @pytest.mark.exceptions

    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Find the instructions text element
        instraction_text_element_locator = driver.find_element(By.XPATH, "/html//p[@id='instructions']")
        instraction_text_element_locator._is_displayed(), "Instraction text element is not displayed."
        # Push add button
        add_button_locator = driver.find_element(By.XPATH, "/html//button[@id='add_btn']")
        add_button_locator.click()
        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(instraction_text_element_locator), "Text instraction is displayed.")

    @pytest.mark.exceptions

    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")), "Row 2 is not displayed.")
        # Verify second input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it is not."
