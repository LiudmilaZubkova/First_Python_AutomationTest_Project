import pytest

from page_objects.logged_in_successfully import LoggedInSuccessfullyPage
from page_objects.login_page import LoginPage


class TestPositiveScenarios:
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        login_page = LoginPage(driver)
        # Open page
        login_page.open()
        # Type username student into Username field
        # Type password Password123 into Password field
        # Puch Submit button
        login_page.execute_login("student", "Password123")
        logged_in_page = LoggedInSuccessfullyPage(driver)
        # Verify new page URL contains practicetestautomation.com/logged-in-successfully/
        assert logged_in_page.expected_url == logged_in_page.expected_url, "Actual URL is not the same as expected"
        # Verify new page contains expected text ('Congratulations' or 'successfully logged in')
        assert logged_in_page.header == "Logged In Successfully", "Header is not expected"
        # Verify button Log out is displayed on the new page
        assert logged_in_page.is_logout_button_displayed(), "Logout button should be visible"
