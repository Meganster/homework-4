# coding=utf-8

from tests.send_tests.base_send import BaseSend


# Выбрать документ --> Получение сообщения с документом c возможностью просмотра из сообщения
class SendTest_document(BaseSend):
    TEST_FILE_XLSX = BaseSend.TEST_FILE_DIR + 'АДАМОВА!.xlsx'

    def test(self):
        BaseSend.test(self)
        # вложение документа из компьютера
        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_XLSX, 1)
        self.file_sending_form.set_destionation_email()
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)

        self.file_sending_form.closeMessageSent()


# Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику
class AttachTest_Media(BaseSend):
    TEST_FILE_MEDIA = BaseSend.TEST_FILE_DIR + 'Track01.mp3'

    def test(self):
        BaseSend.test(self)

        # вложение медиафайла
        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_MEDIA)
        self.file_sending_form.set_destionation_email()
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)


# Выбрать исполняемый файл --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно появиться
# предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах, можно комбинировать форматы
class AttachTest_Executable(BaseSend):
    TEST_FILE_EXECUTABLE = BaseSend.TEST_FILE_DIR + 'hack.sh'

    def test(self):
        BaseSend.test(self)

        # вложение исполняемого файла
        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_EXECUTABLE)
        self.file_sending_form.set_destionation_email()
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)


# Тест под вопросом, нужно ли делать # вложение 99 изображений
class AttachTest99Photos(BaseSend):
    TEST_FILE_IMG = BaseSend.TEST_FILE_DIR + 'IMG__1.JPG'

    def test(self):
        BaseSend.test(self)

        # вложение 99 изображений
        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        for _ in range(1, 99):
            self.file_sending_form.send_keys_to_input(self.TEST_FILE_IMG, time_to_wait=1)
        self.file_sending_form.set_destionation_email()
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)


# Выбрать файл размером (1.99 Гб) ---> Файл должен быть прикреплен и успешно отправлен
class AttachTestAlmostTwoGigFile(BaseSend):
    TEST_FILE_ALMOST_2_GIGS = BaseSend.TEST_FILE_DIR + '1_99_GIG_FILE.txt'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_ALMOST_2_GIGS)
        self.file_sending_form.set_destionation_email()
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)


# Выбрать файл размером (25 Мб) --> Файл должен быть прикреплен и успешно отправлен (через облако)
class AttachTest25MbAndMoreThroughCloud(BaseSend):
    TEST_FILE_MORE_25_MB = BaseSend.TEST_FILE_DIR + 'More_25_mb.png'

    def test(self):
        BaseSend.test(self)

        # вложение файла размером больше 25 Мб (должен загрузиться через облако)
        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_MORE_25_MB)

        self.assertEqual(self.file_sending_form.check_loaded_through_cloud() is not None, True)


class SendTestEmailToMe(BaseSend):
    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_LESS_25MB, 2)

        self.file_sending_form.add_destionation_email('park.test.testovich@mail.ru\n')
        self.file_sending_form.click_send_button()

        self.assertEqual(self.file_sending_form.checkMessageSent(), True)

        #self.file_sending_form.closeMessageSent()