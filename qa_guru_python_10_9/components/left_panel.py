from selene import browser, have


class LeftPanel:
    def __init__(self):
        self.container = browser.element('.category-cards')
        self.menu = browser.element('.menu-list')

    def open(self, category, section):
        browser.open('/')
        self.container.all('.card-body').element_by(have.exact_text(category)).click()
        self.menu.all('#item-0').element_by(have.exact_text(section)).click()

    def open_simple_registration(self):
        self.open('Elements', 'Text Box')