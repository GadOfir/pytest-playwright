class BasePage:
    def __init__(self, page):
        self.page = page

    def verify_title(self, title):
        assert self.page.title() == title

    def click_link_by_text(self, link_text):
        self.page.click(f'text="{link_text}"')
