# coding=utf-8
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

    def check_recipients(self, emails):
        span = WebDriverWait(self.driver, 2) \
            .until(lambda driver: driver.find_element_by_xpath(self.SEND_EMAIL.format(0)))
        print span.get_attribute('innerHTML')

    def add_recipient(self, email_for_add):
        self.add_destionation_email(email_for_add)

    def set_subject_email(self, subject):
        self.click_on_subject_field()
        self.write_some_text(subject)

    def set_message_email(self, message):
        self.click_on_message_field()
        self.write_some_text(message)

