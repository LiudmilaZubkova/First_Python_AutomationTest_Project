

import pytest
from selenium.webdriver.common.by import By


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()
        # Verify Row 2 input field is displayed
        row2_locator = driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")
        assert row2_locator.is_displayed(), "Row 2 input should be displayed, but it is not."
