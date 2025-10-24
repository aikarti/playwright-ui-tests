from playwright.sync_api import Playwright, expect, Page
from tests.utils.constants import BASE_URL
name = 'Karthick'


# Default handling is to dismiss
def test_dialog_default_handling(page: Page):
    
    page.goto(f'{BASE_URL}')


    input_firstname = page.get_by_label('First name')
    input_firstname.fill(name)
    expect(input_firstname).to_have_value(name)

    input_lastname = page.get_by_label('Last name')
    input_lastname.fill('Amaze')
    expect(input_lastname).to_have_value('Amaze')

    page.get_by_role('button', name='Clear').click()
    expect(input_firstname).to_have_value(name)
    expect(input_lastname).to_have_value('Amaze')

     


def test_dialog_ok_or_dismiss(page: Page):
    page.once('dialog', lambda dialog: dialog.accept())

    page.goto(f'{BASE_URL}')
    input_firstname = page.get_by_label('First name')
    input_firstname.fill(name)

    input_lastname = page.get_by_label('Last name')
    input_lastname.fill('Amaze')

    page.get_by_role('button', name='Clear').click()
    expect(input_firstname).to_have_value('')
    expect(input_lastname).to_have_value('')

    page.pause()