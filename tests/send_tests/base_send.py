from pages import email_sending_page
from pages.email_sending_page import EmailSendingPage
from tests.base_test import BaseTest


class BaseSend(BaseTest):
    TEST_FILE_DIR = './test_files/'

    def test(self):
        BaseTest.test(self)
        self.email_sending_page = EmailSendingPage(self.driver)
        self.file_sending_form = self.email_sending_page.form
        self.email_sending_page.redirectQA()
