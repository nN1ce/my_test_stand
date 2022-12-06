from selene.support.shared import browser
from selene import have, be
def test_find_google():
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('mvideo').press_enter()
    browser.element('[class=BYM4Nd').should(have.text('Официальный сайт сети магазинов бытовой'))

def test_2_find_ya():
    browser.open('https://ya.ru')
    browser.element('#text').type('dns').press_enter()
    browser.element('#"search-result').should(have.no.text('Официальный сайт сети магазинов бытовой'))