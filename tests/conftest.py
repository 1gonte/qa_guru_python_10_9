import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():

    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.config.timeout = 6.0
    browser.config.window_height = 1000
    browser.config.window_width = 1500

    yield

    browser.quit()
