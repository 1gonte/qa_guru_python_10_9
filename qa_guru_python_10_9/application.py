from qa_guru_python_10_9.components.left_panel import LeftPanel
from qa_guru_python_10_9.pages.simple_registration_page import SimpleRegistrationPage


class ApplicationManager:
    def __init__(self):
        self.simple_user_registration_form = SimpleRegistrationPage()
        self.left_panel = LeftPanel()


app = ApplicationManager()
