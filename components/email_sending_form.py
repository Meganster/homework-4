# coding=utf-8
import zipfile

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from components.base_form import BaseForm


class EmailSendingForm(BaseForm):
    # file attach elements
    FILE_ATTACH_INPUT = '//input[@data-test-id="attach-file"]'
    FILE_ATTACH_CHECK = '//div[@class="container_progress--2uptg"]'
    FILE_ATTACH_CLOUD_ICON = '//div[@class="container_link--bxJaw"]'
    # FILE_ATTACH_CHECK_NOT_CLOUD = '//div[@class="item--3fh5V"]/div/div'
    FILE_ATTACH_PREVIEW = '//div[@class="item--1ZnwZ"]'

    FILE_ATTACHED = '//div[@data-test-id="attach:{}:loaded]'

    FILE_ATTACH_CLOUD_BTN = '//button[@data-test-id="attach-cloud"]'
    FILE_ATTACH_CLOUD_ELEMENT = '//div[@data-id="/{}"]'
    FILE_ATTACH_CLOUD_ATTACH = '//span[@data-qa-id="attach"]'
    FILE_ATTACH_CHECK_LOADED = '//div[@data-test-id="attach:{}:loaded"]'

    def select_cloud_file(self, filename):
        print self.FILE_ATTACH_CLOUD_ELEMENT.format(filename)
        fileElement = WebDriverWait(self.driver, 2) \
            .until(lambda driver: driver.find_elements_by_xpath(self.FILE_ATTACH_CLOUD_ELEMENT.format(filename))[0])
        fileElement.click()

    def do_cloud_attach(self):
        button = WebDriverWait(self.driver, 1) \
            .until(lambda driver: driver.find_element_by_xpath(self.FILE_ATTACH_CLOUD_ATTACH))
        button.click()

    def add_destionation_email(self, emailAdd):
        self.set_destionation_email()

    def set_subject_email(self, subject):
        self.click_on_subject_field()
        self.write_some_text(subject)

    def set_message_email(self, message):
        self.click_on_message_field()
        self.write_some_text(message)

