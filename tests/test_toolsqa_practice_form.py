from selene import browser, have
import os


def test_student_registration_form():
    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('IvanIvanov@test.com')
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('1616161616')
    browser.element('.react-datepicker__input-container').click()
    browser.element('.react-datepicker__month-select').element('[value="5"]').click()
    browser.element('.react-datepicker__year-select').element('[value="2007"]').click()
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
