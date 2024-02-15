from selene import browser, have

from qa_guru_python_10_9.data.users import SimpleUsers


class SimpleRegistrationPage:

    def open(self):
        browser.open('/text-box')
        return self

    def fill_full_name(self, value):
        browser.element('#userName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress-wrapper #currentAddress').type(value)
        return self

    def fill_permanent_address(self, value):
        browser.element('#permanentAddress-wrapper #permanentAddress').type(value)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_registered_user(self, user: SimpleUsers):
        browser.element('.border').all('p').should(have.exact_texts(
            f'Name:{user.full_name}',
            f'Email:{user.email}',
            f'Current Address :{user.current_address}',
            f'Permananet Address :{user.permanent_address}',
        )
        )
        return self

    def register(self, user: SimpleUsers):
        self.fill_full_name(user.full_name)
        self.fill_email(user.email)
        self.fill_current_address(user.current_address)
        self.fill_permanent_address(user.permanent_address)
        self.submit()
