from selene.support.shared import browser
from selene import have
import pytest

def test_search_text_in_google(seting_window_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('selene python').press_enter()
    browser.element('[class=v7W49e]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_2_search_text_in_google(seting_window_browser):
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('selene python').press_enter()
    browser.element('[class=v7W49e]').should(have.no.text('C++'))
