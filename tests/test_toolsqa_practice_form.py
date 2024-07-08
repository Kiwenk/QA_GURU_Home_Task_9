from modules.registration_from import Registration_form
from modules.users import User


def test_student_registration_form():
    form_action = Registration_form()
    human_being = User(first_name='Ivan',
                       last_name='Ivanov',
                       email='Vasya_the_terrible_2005@mail.ru',
                       phone='1987198719',
                       subject='Computer Science',
                       hobbies='Sports',
                       address='Kyoto, Pushkin Street, 16',
                       state='Haryana',
                       city='Karnal')
    form_action.open('automation-practice-form')
    form_action.register(human_being)
    form_action.table_check(human_being)
