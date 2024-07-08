from selene import browser, have
import os



class Registration_form:
    def open(self,url):
        browser.open(f'/{url}')

    def first_name(self, name):
        browser.element('#firstName').type(name)

    def last_name(self, second_name):
        browser.element('#lastName').type(second_name)

    def user_email(self,email):
        browser.element('#userEmail').type(email)

    def gender_radio(self):
        browser.element('[for="gender-radio-3"]').click()

    def user_number(self,number):
        browser.element('#userNumber').type(number)

    def date_of_birth(self):
        browser.element('.react-datepicker__input-container').click()
        browser.element('.react-datepicker__month-select').element('[value="5"]').click()
        browser.element('.react-datepicker__year-select').element('[value="2007"]').click()
        browser.element('.react-datepicker__month').element('[aria-label="Choose Saturday, June 16th, 2007"]').click()

    def subjects(self,sub):
        browser.element('#subjectsInput').type(sub).press_enter()

    def hobbies(self):
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

    def upload_picture(self):
        browser.element('#uploadPicture').send_keys(os.path.abspath('../resources/pic.jpg'))

    def current_address(self,address):
        browser.element("#currentAddress").type(address)

    def state(self,state):
        browser.element("#react-select-3-input").type(state).press_enter()

    def city(self,city):
        browser.element("#react-select-4-input").type(city).press_enter()

    def sumbit_button(self):
        browser.element("#submit").click()

    def check_text_after_submit_button(self):
        browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))

    def check_table(self):
        browser.element('.table').all('td').even.should(
            have.exact_texts('Ivan Ivanov', 'Vasya_the_terrible_2005@mail.ru', 'Other', '1987198719', '16 June,2007', 'Chemistry',
                             'Sports, Music', 'pic.jpg', 'Kyoto, Pushkin Street, 16', 'Haryana Karnal'))