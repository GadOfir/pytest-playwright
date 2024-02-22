import pytest
from tests.BaseTest import BaseTest
from pages.HomePage import HomePage
from pages.AddRemoveElementsPage import AddRemoveElementsPage
from pages.ABTestingPage import ABTestingPage  # Add this import

class TestHomePage(BaseTest):
    @pytest.mark.smoke
    def test_ab_testing_page_navigation(self):
        home_page = HomePage(self.page)
        home_page.goto_home_page()

        # Step annotation
        self.step("Navigated to the home page")

        home_page.click_link_by_text(home_page.AB_TESTING_LINK_TEXT)

        ab_testing_page = ABTestingPage(self.page)
        # Perform assertions to verify the A/B Testing page
        assert ab_testing_page.is_page_loaded(), "A/B Testing page did not load successfully"

    def test_add_remove_elements_page_interaction(self):
        home_page = HomePage(self.page)
        home_page.goto_home_page()

        # Step annotation
        self.step("Navigated to the home page")

        home_page.click_link_by_text(home_page.ADD_REMOVE_ELEMENTS_LINK_TEXT)

        add_remove_elements_page = AddRemoveElementsPage(self.page)
        # Perform actions on the Add/Remove Elements page

        # Check if the 'Add Element' button is displayed
        assert add_remove_elements_page.is_add_element_button_displayed(), "'Add Element' button is not displayed"

    def step(self, description):
        """Annotates a step in the test."""
        if not hasattr(self, "_steps"):
            self._steps = []
        self._steps.append(description)
