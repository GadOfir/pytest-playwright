from pages.basePage import BasePage


class AddRemoveElementsPage(BasePage):
    ADD_ELEMENT_BUTTON_CSS_SELECTOR = 'button'

    def __init__(self, page):
        super().__init__(page)

    def is_add_element_button_displayed(self):
        """
        Checks if the 'Add Element' button is displayed on the page.
        """
        # Find all buttons on the page
        buttons = self.page.query_selector_all(self.ADD_ELEMENT_BUTTON_CSS_SELECTOR)

        # Check if any button contains the text 'Add Element'
        for button in buttons:
            if button.inner_text() == 'Add Element':
                return True
        return False