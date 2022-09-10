from selene.support.shared import browser

def test_find_google():
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('mvideo').press_enter()
    browser.element('[class="iUh30 tjvcx"]').press_enter()
        # should(have.text('Selene - User-oriented Web UI browser tests in Python'))