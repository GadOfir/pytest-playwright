import pytest
from playwright.sync_api import sync_playwright

class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def browser(self):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=False, slow_mo=500, args=["--start-maximized"])
            yield browser
            browser.close()

    @pytest.fixture(autouse=True)
    def setup(self, browser, request):
        self.browser = browser
        self.page = self.browser.new_page(no_viewport=True)
        yield  # This allows the test function to run

        # Add a hook to capture test outcomes
        outcome = request.node.rep_call.failed if hasattr(request.node, "rep_call") and request.node.rep_call.failed else None

        # Take a screenshot if the test fails
        if outcome:
            screenshot_path = f"screenshots/{request.node.name}.png"
            self.page.screenshot(path=screenshot_path)
            print(f"Screenshot saved: {screenshot_path}")

        self.page.close()  # Close the page after the test function finishes

    @pytest.fixture(scope="session")
    def _html_report_path(self, request):
        # Get the path to save the HTML report
        return request.config.option.htmlpath

    @classmethod
    def pytest_addoption(cls, parser):
        # Add a command-line option to specify the path for HTML report
        parser.addoption("--html-report", action="store", default="report.html", help="Path to save HTML report.")

    @classmethod
    def pytest_configure(cls, config):
        # Configure metadata for HTML report
        config._metadata['Project Name'] = 'Your Project Name'
        config._metadata['Tester'] = 'Your Name'

    @classmethod
    def pytest_sessionfinish(cls, session, exitstatus):
        if hasattr(session, 'browser'):
            session.browser.close()
