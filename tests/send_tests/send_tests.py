# coding=utf-8

from tests.send_tests.base_send import BaseSend

class SendTestEmailToMe(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.email_sending_form.open_writing_letter()

        self.email_sending_form.set_correct_recipients()
        self.email_sending_form.set_subject_email(self.SUBJECT)
        self.email_sending_form.set_message_email(self.TEXT)
        self.email_sending_form.click_send_button()

        #self.assertEqual(self.email_sending_form.checkMessageSent(), True)
        self.assertEqual(self.email_sending_form.check_correct_recipients(), True)

        #self.email_sending_form.closeMessageSent()