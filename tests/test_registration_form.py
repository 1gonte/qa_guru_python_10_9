from qa_guru_python_10_9.data.users import student
from qa_guru_python_10_9.pages.registartion_page import RegistrationPage


def test_fill_registration_form():

    registration_page = RegistrationPage()
    registration_page.open()

    registration_page.register(student)

    registration_page.should_have_registered(student)
