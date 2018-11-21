from pages import email_sending_page
from pages.email_sending_page import EmailSendingPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
    SUBJECT = 'Test subject'

    def test(self):
        BaseTest.test(self)
        self.email_sending_page = EmailSendingPage(self.driver)
        self.email_sending_form = self.email_sending_page.form
        self.email_sending_page.redirectQA()
