from selenium.webdriver.support import expected_conditions as ec
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestExceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        # Click Add button
        add_button_locator = driver.find_element(By.XPATH, "//button[@id='add_btn']")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located(
            (By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/input[@type='text']")))

        # Verify Row 2 input field is displayed
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed, but it is not."


