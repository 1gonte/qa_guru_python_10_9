from qa_guru_python_10_9.pages.registartion_page import RegistrationPage


def test_fill_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    (registration_page
     .fill_first_name('Georgii')
     .fill_last_name('Sergeev')
     .fill_email('example@gmail.com')
     .set_gender('Male')
     .fill_mobile_number('0123456789')
     .set_date_of_birth('2001', 'February', '16')
     .fill_subject('Computer Science')
     .set_hobbie('Reading')
     .set_photo('image.png')
     .fill_current_addres('Moscow, Red Square, 1A')
     .set_state('NCR')
     .set_city('Delhi')
     .submit())

    registration_page.should_registered_user_with(
        'Georgii Sergeev',
        'example@gmail.com',
        'Male',
        '0123456789',
        '16 February,2001',
        'Computer Science',
        'Reading',
        'image.png',
        'Moscow, Red Square, 1A',
        'NCR Delhi')
