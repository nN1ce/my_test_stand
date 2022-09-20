from selene.support.shared import browser  # импорт browser из selene
from selene import have  # импорт have (проверки)

# hold_browser_open - оставить браузер открытым после теста
browser.config.hold_browser_open = True

# Открыть браузер (ncr - поиск без привязки к стране)
browser.open('https://google.com/ncr')
# element - выбор элемента, type - напечатать, press_enter - нажать Enter
browser.element('[name=q]').type('selene python').press_enter()
# element - выбор элемента, should - должен, have - иметь, text - текс
browser.element('[class=v7W49e]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
