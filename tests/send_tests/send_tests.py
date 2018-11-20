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


class AttachTestLess25MbWithoutCloud2(BaseSend):
    TEST_FILE_LESS_25MB = BaseSend.TEST_FILE_DIR + './pict.png'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.set_file_attach_input()
        self.file_sending_form.send_keys_to_input(self.TEST_FILE_LESS_25MB, 2)

        self.assertEqual(self.file_sending_form.check_loaded_without_cloud(), True)


# Выбрать документ из облака--> Получение сообщения с документом c возможностью просмотра из сообщения
class AttachCloudDocument(BaseSend):
    TEST_FILE_XLSX = 'some_table.xlsx'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.click_cloud_button()
        self.file_sending_form.select_cloud_file(self.TEST_FILE_XLSX)
        self.file_sending_form.do_cloud_attach()

        assert (self.file_sending_form.check_loaded(filename=self.TEST_FILE_XLSX))


# Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику
class AttachCloudMedia(BaseSend):
    TEST_FILE_MEDIA = 'Track01.mp3'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.click_cloud_button()
        self.file_sending_form.select_cloud_file(self.TEST_FILE_MEDIA)
        self.file_sending_form.do_cloud_attach()

        assert (self.file_sending_form.check_loaded(filename=self.TEST_FILE_MEDIA))


# Выбрать исполняемый файл из облака --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно
# появиться предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах,
# можно комбинировать форматы
class AttachCloudExecutable(BaseSend):
    TEST_FILE_EXECUTABLE = 'hack.sh'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.click_cloud_button()
        self.file_sending_form.select_cloud_file(self.TEST_FILE_EXECUTABLE)
        self.file_sending_form.do_cloud_attach()

        assert (self.file_sending_form.check_loaded(filename=self.TEST_FILE_EXECUTABLE))


# Выбрать файл размером (1.99 Гб) из облака ---> Файл должен быть прикреплен и успешно отправлен
class AttachCloudAlmost2GigFile(BaseSend):
    TEST_FILE_ALMOST_2_GIGS = '1_99_GIG_FILE.txt'

    def test(self):
        BaseSend.test(self)

        self.file_sending_form.open_writing_letter()
        self.file_sending_form.click_cloud_button()
        self.file_sending_form.select_cloud_file(filename=self.TEST_FILE_ALMOST_2_GIGS)
        self.file_sending_form.do_cloud_attach()

        assert (self.file_sending_form.check_loaded(self.TEST_FILE_ALMOST_2_GIGS))

        # class AttachTestDragDropIMGasFile(BaseSend):
        #     TEST_FILE_IMG = BaseSend.TEST_FILE_DIR + 'pict.png'
        #
        #     # JS_DROP_FILE = """
        #     #     var target = arguments[0],
        #     #         offsetX = arguments[1],
        #     #         offsetY = arguments[2],
        #     #         document = target.ownerDocument || document,
        #     #         window = document.defaultView || window;
        #     #
        #     #     var input = document.createElement('INPUT');
        #     #     input.type = 'file';
        #     #     input.onchange = function () {
        #     #       var rect = target.getBoundingClientRect(),
        #     #           x = rect.left + (offsetX || (rect.width >> 1)),
        #     #           y = rect.top + (offsetY || (rect.height >> 1)),
        #     #           dataTransfer = { files: this.files };
        #     #
        #     #       ['dragenter', 'dragover', 'drop'].forEach(function (name) {
        #     #         var evt = document.createEvent('MouseEvent');
        #     #         evt.initMouseEvent(name, !0, !0, window, 0, 0, 0, x, y, !1, !1, !1, !1, 0, null);
        #     #         evt.dataTransfer = dataTransfer;
        #     #         target.dispatchEvent(evt);
        #     #       });
        #     #
        #     #       setTimeout(function () { document.body.removeChild(input); }, 25);
        #     #     };
        #     #     target.appendChild(input);
        #     #     return input;
        #     # """
        #
        #     # JS_DROP_FILE = """
        #     #     let container = arguments[0];
        #     #     let img = document.createElement('img');
        #     #     img.src = 'http://qaru.site/img/logo-dark.svg'
        #     #     container.appendChild(img)
        #     #     return img
        #     # """
        #     #
        #     # def test(self):
        #     #     BaseSend.test(self)
        #     #     self.file_sending_form.open_writing_letter()
        #     #
        #     #     target = self.driver.find_element_by_xpath('//div[@class="scrollview--1Ltx2 scrollview_main--12OVu"]')
        #     #
        #     #     # driver = target.parent
        #     #
        #     #     file_input = self.driver.execute_script(self.JS_DROP_FILE, target, 0, 0)
        #     #     # file_input.send_keys(self.TEST_FILE_IMG)
        #     #
        #     #     ActionChains(self.driver).drag_and_drop(file_input, target).perform()
        #
        #     def test(self):
        #         BaseSend.test(self)
        #
        #         self.file_sending_form.open_writing_letter()
        #         target = self.driver.find_element_by_xpath('//div[@class="scrollview--1Ltx2 scrollview_main--12OVu"]')
        #         drag_file(self.TEST_FILE_IMG, to=target)
        #
        #         print 'yeah!'

        # ––––––––––––––––––––
        # –––––––––––––––––––––

        #
        # Прикрепление файла из компьютера:
        # Выбрать документ --> Получение сообщения с документом c возможностью просмотра из сообщения – \/

        # Выбрать медиафайл --> Получение сообщения с медиафайлом с возможностью воспроизведения по клику – \/

        # Выбрать исполняемый файл --> Получение сообщения с исполняемым файлом. При попытке скачать файл должно появиться – \/
        # предупреждение о потенциальной вредоносности файла. Если речь идет о нескольких файлах, можно комбинировать форматы

        # Выбрать файл размером (1.99 Гб) ---> Файл должен быть прикреплен и успешно отправлен – \/

        # Выбрать файл размером (25 Мб) --> Файл должен быть прикреплен и успешно отправлен (через облако) – \/

        # Выбрать файл размером (24.99 Мб) --> Файл должен быть прикреплен и успешно отправлен (напрямую без облака) – \/

        # ––––––––––––––––––––
        # ––––––––––––––––––––


        # Выбрать исполняемый файл и отправить на gmail почту --> Со стороны отправителя: получение сообщения от
        # mailer-daemon@corp.mail.ru об ошибке | Со стороны получателя: никаких сообщений не должно быть получено

        # Выбрать более 99 файлов --> Появится сообщение о том, что отправятся только 100 файлов. Возможности прикрепить
        # новые файлы не будет. Ожидается отправка 99 файлов

        # Выбрать 99 изображений (размер не имеет значения) и прикрепить как изображение. --> Все изображения полноразмерно
        # вложатся в тело письма (при тестировании функции drag&drop)

        # Выбрать 99 изображений (размер не имеет значения) и прикрепить как файл. --> Все изображения вложатся в тело письма
        #  (при тестировании функции drag&drop)


        # Продублировать вышеперечисленные действия для файлов из облака

        # ––––––––––––––––––––
