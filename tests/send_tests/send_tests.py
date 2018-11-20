# coding=utf-8

from tests.send_tests.base_send import BaseSend

class SendTestEmailToMe(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.add_destionation_email('park.test.testovich@mail.ru\n')
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        self.assertEqual(self.email_sending_form.checkMessageSent(), True)

        self.email_sending_form.check_recipients(2)

        #self.email_sending_form.closeMessageSent()