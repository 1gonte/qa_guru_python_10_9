import os
from selene import browser, be, have, by


def test_fill_registration_form():

    browser.open('/')
    browser.driver.execute_script("document.querySelector('#fixedban').remove();")
    browser.driver.execute_script("document.querySelector('footer').remove();")

    browser.element('#firstName').type('Georgii')
    browser.element('#lastName').should(be.blank).type('Sergeev')
    browser.element('#userEmail').should(be.blank).type('example@gmail.com')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type('0123456789')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("2001")
    ).click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("February")
    ).click()
    browser.element(".react-datepicker__day--016").click()

    browser.element('#subjectsInput').should(be.blank).type('Computer Science')\
        .press_enter()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()

    browser.element('#uploadPicture.form-control-file').send_keys(
        os.path.abspath('resources/image.png'))

    browser.element('#currentAddress').should(be.blank).type('some random address')

    browser.element("#state").should(be.clickable).click()
    browser.element(by.text('NCR')).should(be.clickable).click()

    browser.element("#city").should(be.clickable).click()
    browser.element(by.text('Delhi')).should(be.clickable).click()

    browser.element('#submit').should(be.clickable).click()

    browser.element('.table').all('td:nth-child(2)').should(
        have.texts('Georgii Sergeev',
                   'example@gmail.com',
                   'Male',
                   '0123456789',
                   '16 February,2001',
                   'Computer Science',
                   'Sports, Reading, Music',
                   'image.png',
                   'some random address',
                   'NCR Delhi'))

