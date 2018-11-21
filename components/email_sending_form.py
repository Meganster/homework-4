# coding=utf-8
import re
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from components.base_form import BaseForm


class EmailSendingForm(BaseForm):
    SEND_EMAIL = '//span[@data-id="contact-to-{}"]'
    MY_EMAIL = 'park.test.testovich@mail.ru'
    CORRECT_EMAILS = ['adam404pet@gmail.com', 'headmonster3@yandex.ru']
    WRONG_EMAILS = ['sdvskdvnskldv@mail', 'sdv238y2jkdvn']

    def set_correct_recipients(self):
        CORRECT_EMAILS = ['adam404pet@gmail.com', 'headmonster3@yandex.ru']
        emailsStr = ""
        for i in range(len(self.CORRECT_EMAILS)):
            emailsStr += CORRECT_EMAILS[i] + "\n"
        self.add_destionation_email(emailsStr)

    def check_correct_recipients(self):
        CORRECT_EMAILS = ['adam404pet@gmail.com', 'headmonster3@yandex.ru']
        for i in range(len(self.CORRECT_EMAILS)):
            span = WebDriverWait(self.driver, 2) \
                .until(lambda driver: driver.find_element_by_xpath(self.SEND_EMAIL.format(i)))
            clean_email_from_ui = re.sub('\s+', '', span.get_attribute('innerHTML'))
            clean_email_from_ui = re.sub(',', '', clean_email_from_ui)
            if clean_email_from_ui != CORRECT_EMAILS[i]:
                return False
        return True

    def add_recipient(self, email_for_add):
        self.add_destionation_email(email_for_add)

    def set_subject_email(self, subject):
        self.click_on_subject_field()
        self.write_some_text(subject)

    def set_message_email(self, message):
        self.click_on_message_field()
        self.write_some_text(message)

