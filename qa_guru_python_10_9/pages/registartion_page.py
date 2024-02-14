import os

from selene import browser, have, by, be

from qa_guru_python_10_9.data.users import Users


class RegistrationPage:
    def open(self):
        browser.open('/')
        browser.driver.execute_script("document.querySelector('#fixedban').remove();")
        browser.driver.execute_script("document.querySelector('footer').remove();")
        return self

    def fill_first_name(self, value):
        browser.element('#firstName').type(value)
        return self

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)
        return self

    def fill_email(self, value):
        browser.element('#userEmail').type('example@gmail.com')
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

    def set_hobbie(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()
        return self

    def set_photo(self, name):
        browser.element('#uploadPicture.form-control-file').send_keys(
            os.path.abspath(f'resources/{name}'))
        return self

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def set_state(self, value):
        browser.element("#state").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()
        return self

    def set_city(self, value):
        browser.element("#city").should(be.clickable).click()
        browser.element(by.text(value)).should(be.clickable).click()
        return self

    def submit(self):
        browser.element('#submit').should(be.clickable).click()
        return self

    def should_have_registered(self, user: Users):
        browser.element(".table").all("td:nth-child(2)").should(
            have.exact_texts(
                f"{user.first_name} {user.last_name}",
                user.email,
                user.gender,
                user.mobile_number,
                f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
                user.subject,
                user.hobbie,
                user.photo_name,
                user.current_address,
                f'{user.state} {user.city}',
            )
        )

    def register(self, user: Users):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.set_gender(user.gender)
        self.fill_mobile_number(user.mobile_number)
        self.set_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.fill_subject(user.subject)
        self.set_hobbie(user.hobbie)
        self.set_photo(user.photo_name)
        self.fill_current_address(user.current_address)
        self.set_state(user.state)
        self.set_city(user.city)
        self.submit()
