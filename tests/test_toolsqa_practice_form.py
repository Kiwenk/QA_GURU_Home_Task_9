from modules.registration_from import Registration_form


def test_student_registration_form():
    form_action = Registration_form()
    form_action.open('automation-practice-form')
    form_action.first_name('Ivan')
    form_action.last_name('Ivanov')
    form_action.user_email('Vasya_the_terrible_2005@mail.ru')
    form_action.gender_radio()
    form_action.user_number('1987198719')
    form_action.date_of_birth()
    form_action.subjects('Che')
    form_action.hobbies()
    form_action.upload_picture()
    form_action.current_address("Kyoto, Pushkin Street, 16")
    form_action.state('Haryana')
    form_action.city('Karnal')
    form_action.sumbit_button()
    form_action.check_text_after_submit_button()
    form_action.check_table()
