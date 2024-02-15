from qa_guru_python_10_9.application import app
from qa_guru_python_10_9.data.users import george


def test_fill_simple_registration_form():

    app.left_panel.open_simple_registration()

    app.simple_user_registration_form.register(george)

    app.simple_user_registration_form.should_have_registered_user(george)
