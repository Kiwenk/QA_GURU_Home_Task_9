from selene import browser, have
from pathlib import Path


class RegistrationForm:
    def open(self, url):
        browser.open(f'/{url}')

    def first_name(self, name):
        browser.element('#firstName').type(name)

    def last_name(self, second_name):
        browser.element('#lastName').type(second_name)

    def user_email(self, email):
        browser.element('#userEmail').type(email)

    def gender_radio(self):
        browser.element('[for="gender-radio-3"]').click()

    def user_number(self, number):
        browser.element('#userNumber').type(number)

    def date_of_birth(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('June')
        browser.element('.react-datepicker__year-select').type('2007')
        browser.element(
            f'.react-datepicker__day--0{16}:not(.react-datepicker__day--outside-month)'
        ).click()  # одолжил у коллег

    def subjects(self, sub):
        browser.element('#subjectsInput').type(sub).press_enter()

    def hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self, photo):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(f'resources/{photo}')))

    def current_address(self, address):
        browser.element("#currentAddress").type(address)

    def state(self, state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def city(self, city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def sumbit_button(self):
        browser.element("#submit").click()

    def check_text_after_submit_button(self, text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(text))

    def check_table(self, name, email, gender, phone, birthday, hobbies, hobbies2, photo, address, state):
        browser.element('.table').all('td').even.should(
            have.exact_texts(name, email, gender, phone,
                             birthday, hobbies, hobbies2, photo, address, state))
