from selene.support.shared import browser
from selene import have, be

def test_submit_user_details():
    browser.config.timeout = 3
    browser.config.base_url = 'https://demoqa.com'

    browser.open('https://demoqa.com/text-box')
    browser.should(have.title('ToolsQA'))
    browser.element('.main-header').should(have.text('Text Box'))
    browser.all('#userFrom input, #userForm textarea').should(have.size(2))

    browser.element('#userName').type('Evgen')
    browser.element('#submit').press_enter()
    browser.close()

