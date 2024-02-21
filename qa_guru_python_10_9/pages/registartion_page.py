from selene import browser, have, by, be, command

from qa_guru_python_10_9.resource import path


class RegistrationPage:
    def open(self):
        browser.open('/')
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type(value)
        return self

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def fill_mobile_number(self, value):
        browser.element('#userNumber').type(value)
        return self

    def set_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element(".react-datepicker__year-select").click().element(
            by.text(year)
        ).click()
        browser.element(".react-datepicker__month-select").click().element(
            by.text(month)
        ).click()
        browser.element(f".react-datepicker__day--0{day}").click()
        return self

    def fill_subject(self, value):
        browser.element('#subjectsInput').should(be.blank).type(value) \
            .press_enter()
        return self

    def set_hobby(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def set_photo(self, name):
        browser.element('#uploadPicture').send_keys(path(name))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value):
        browser.element("#state").perform(command.js.scroll_into_view).click()
        browser.element(by.text(value)).should(be.clickable).click()
        return self

    def set_city(self, value):
        browser.element("#city").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()
        return self

    def submit(self):
        browser.element('#submit').perform(command.js.scroll_into_view).click()
        return self

    def should_registered_user_with(self, full_name, email, gender, mobile_number, date_of_birth,
                                    subject, hobby, photo_name, current_address, state_and_city):
        browser.element('.table').all('td:nth-child(2)').should(
            have.texts(full_name,
                       email,
                       gender,
                       mobile_number,
                       date_of_birth,
                       subject,
                       hobby,
                       photo_name,
                       current_address,
                       state_and_city))
        return self
