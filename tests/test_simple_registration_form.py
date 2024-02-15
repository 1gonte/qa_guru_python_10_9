from qa_guru_python_10_9.data.users import george
from qa_guru_python_10_9.pages.simple_registration_page import SimpleRegistrationPage


def test_fill_simple_registration_form():

    registration_page = SimpleRegistrationPage()
    registration_page.open()

    registration_page.register(george)

    registration_page.should_have_registered_user_with(george)

