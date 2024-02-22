from pages.basePage import BasePage

class HomePage(BasePage):
    URL = "https://the-internet.herokuapp.com/"
    AB_TESTING_LINK_TEXT = "A/B Testing"
    ADD_REMOVE_ELEMENTS_LINK_TEXT = "Add/Remove Elements"

    def __init__(self, page):
        super().__init__(page)

    def goto_home_page(self):
        """Navigate to the home page."""
        self.page.goto(self.URL)

    def click_ab_testing_link(self):
        """Click on the A/B Testing link."""
        self.click_link_by_text(self.AB_TESTING_LINK_TEXT)

    def click_add_remove_elements_link(self):
        """Click on the Add/Remove Elements link."""
        self.click_link_by_text(self.ADD_REMOVE_ELEMENTS_LINK_TEXT)
