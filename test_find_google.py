from selene.support.shared import browser
from selene import have, be
def test_find_google():
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('mvideo').press_enter()
    browser.find.test('М.Видео - интернет-магазин цифровой и')
        # should(have.text('Selene - User-oriented Web UI browser tests in Python'))