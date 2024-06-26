from selene import browser, have
import os


def test_student_registration_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').set_value('Ivan')
    browser.element('#firstName').should(have.value('Ivan'))
    browser.element('#lastName').set_value('Ivanov')
    browser.element('#lastName').should(have.value('Ivanov'))
    browser.element('#userEmail').set_value('IvanIvanov@test.com')
    browser.element('#userEmail').should(have.value('IvanIvanov@test.com'))
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').set_value('1616161616')
    browser.element('#userNumber').should(have.value('1616161616'))
    browser.element('[class="react-datepicker__input-container"]').click()
    browser.element('[class="react-datepicker__month-select"]').element('[value="5"]').click()
    browser.element('[class="react-datepicker__year-select"]').element('[value="2007"]').click()
    browser.element('.react-datepicker__month').element('[aria-label="Choose Saturday, June 16th, 2007"]').click()
    browser.element('#subjectsInput').type('Che').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pic.jpg'))
    browser.element("#currentAddress").type("Kyoto, Pushkin Street, 16")
    browser.element("#react-select-3-input").type("Haryana").press_enter()
    browser.element("#react-select-4-input").type("Karnal").press_enter()
    browser.element("#submit").click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(
        have.exact_texts('Ivan Ivanov', 'IvanIvanov@test.com', 'Other', '1616161616', '16 June,2007', 'Chemistry',
                         'Sports, Music', 'pic.jpg', 'Kyoto, Pushkin Street, 16', 'Haryana Karnal'))
