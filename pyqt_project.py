
import sqlite3
import csv
import sys
import random

from PyQt5 import QtWidgets, QtSql
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QInputDialog, QTextEdit, QMainWindow, QMessageBox
from PyQt5.QtWidgets import QDialogButtonBox, QLineEdit, QTableWidget, QTableWidgetItem, QTableView
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel



class Window1(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.w1 = Window1
        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('Сурдопереводчик')
        self.editor = QTextEdit(self)
        self.editor.resize(800, 500)
        self.editor.move(0, 0)
        self.editor.setStyleSheet('QTextEdit{background-image:url("data\\fon_img.jpg");}')  # установка фона
        self.label1 = QLabel(self)
        self.label1.setText("Сурдопереводчик")
        self.label1.resize(700, 100)
        self.label1.move(20, 20)
        self.label1.setStyleSheet(u"font-size: 80px;") # увеличение шрифта
        self.btn1 = QPushButton("Выбрать русский алфавит", self)
        self.btn1.resize(700, 100)
        self.btn1.move(20, 150)
        self.btn1.setStyleSheet(u"font-size: 50px;")

        self.btn2 = QPushButton("Chose english alphavit", self)
        self.btn2.resize(700, 100)
        self.btn2.move(20, 270)
        self.btn2.setStyleSheet(u"font-size: 50px;")

        self.btn3 = QPushButton("Руководство/Management", self)
        self.btn3.resize(700, 80)
        self.btn3.move(20, 400)
        self.btn3.setStyleSheet(u"font-size: 50px;")

        self.btn1.clicked.connect(self.Russian)  # при нажатии кнопки выполняются функция
        self.btn2.clicked.connect(self.English)
        self.btn3.clicked.connect(self.Rules)


    def Russian(self):
        self.russian_window = Window2() # запись в переменные окна, чтобы их открыть
        self.russian_window.show()

    def English(self):
        self.english_window = Window3()  # запись в переменные окна, чтобы их открыть
        self.english_window.show()

    def Rules(self):
        self.rules_window = Window4()  # запись в переменные окна, чтобы их открыть
        self.rules_window.show()



class Window2(QtWidgets.QWidget):  # второе окно для руско-язычных людей
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Русский язык')
        self.setGeometry(300, 300, 800, 500)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("data\\fon_w2.jpg"))
        self.background.show()
        self.exp_lbl = QLabel(self)
        self.exp_lbl.setText("Поставьте английскую раскладку")
        self.exp_lbl.resize(500, 30)
        self.exp_lbl.move(10, 10)
        self.exp_lbl.setStyleSheet(u"font-size: 20x;")
        self.exp_lbl.show()
        self.test_btn = QPushButton(self)
        self.test_btn.setText("Перейти к тесту")
        self.test_btn.resize(120, 30)
        self.test_btn.move(670, 10)
        self.test_btn.setStyleSheet(u"font-size: 20x;")
        self.test_btn.clicked.connect(self.Dialog)




        with open("data\csv_file_rus.csv") as file_csv:  # открытие csv файла с буквами и их рисунками
            reader = csv.DictReader(file_csv, delimiter=";")
            self.dictionary = {}
            for i in reader:
                rus_letter = str(i["Буква"])   # запись в переменную букв
                rus_img = str(i["Картинка"])   # запись в переменную рисунков
                key, val = rus_letter, rus_img
                self.dictionary[key] = val  # создание словаря где буквы это ключи и значения это рисунки

    def Dialog(self):
        message = 'Вы хотите закончить обучение и перейти к тесту?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                            QtWidgets.QMessageBox.Yes,
                                            QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            self.rus_test()
        else:
            pass


    def rus_test(self):   # запись окна в переменную, для его показа
        self.test_window1 = Test_in_rus1()
        self.test_window1.show()

    def keyPressEvent(self, event):  # получение событий клавиш
        if event.key() == Qt.Key_F:  # проверка нажатия букв на клавиатуре, чтобы нарисовать рисунки по ключю(букве) в словаре
            img1 = self.dictionary["А"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()



        if event.key() == Qt.Key_D:
            img1 = self.dictionary["В"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_U:
            img1 = self.dictionary["Г"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_L:
            img1 = self.dictionary["Д"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_T:
            img1 = self.dictionary["Е"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()



        if event.key() == Qt.Key_P:
            img1 = self.dictionary["З"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()


        if event.key() == Qt.Key_B:
            img1 = self.dictionary["И"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_Q:
            img1 = self.dictionary["Й"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_R:
            img1 = self.dictionary["К"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_K:
            img1 = self.dictionary["Л"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_V:
            img1 = self.dictionary["М"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_Y:
            img1 = self.dictionary["Н"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_J:
            img1 = self.dictionary["О"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_G:
            img1 = self.dictionary["П"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_H:
            img1 = self.dictionary["Р"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_C:
            img1 = self.dictionary["С"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_N:
            img1 = self.dictionary["Т"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_E:
            img1 = self.dictionary["У"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_A:
            img1 = self.dictionary["Ф"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_W:
            img1 = self.dictionary["Ц"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_X:
            img1 = self.dictionary["Ч"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_I:
            img1 = self.dictionary["Ш"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_O:
            img1 = self.dictionary["Щ"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_S:
            img1 = self.dictionary["Ы"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_M:
            img1 = self.dictionary["Ь"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

        if event.key() == Qt.Key_Z:
            img1 = self.dictionary["Я"]
            self.pixmap1 = QPixmap(img1)
            self.image = QLabel(self)
            self.image.resize(300, 300)
            self.image.move(300, 100)
            self.image.setPixmap(self.pixmap1)
            self.image.show()

class Window3(QtWidgets.QWidget):  # окно для англо-язычных
    def __init__(self):
        super().__init__()
        self.setWindowTitle('English language')
        self.setGeometry(300, 300, 800, 500)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("data\\fon_w2.jpg"))
        self.background.show()
        self.test_btn = QPushButton(self)
        self.test_btn.setText("Go to test")
        self.test_btn.resize(120, 30)
        self.test_btn.move(670, 10)
        self.test_btn.clicked.connect(self.Dialog)

        file_txt = open("data\english_alph.txt")  # открытие txt файла
        self.dictionary = {}
        for row in file_txt:
            eng_letter, eng_img = row.rstrip("\n").split(",")  # распределение в переменные буквы и рисунки
            key, val = eng_letter, eng_img
            self.dictionary[key] = val  # создание словаря где ключ это буква, а значение это рисунок

    def Dialog(self):
        message = 'Do you want to finish training and go to the test?'
        reply1 = QtWidgets.QMessageBox.question(self, 'Message', message,
                                            QtWidgets.QMessageBox.Yes,
                                            QtWidgets.QMessageBox.No)

        if reply1 == QtWidgets.QMessageBox.Yes:
            self.eng_test()
        else:
            pass

    def eng_test(self):
        self.test_window1 = Test_in_eng()
        self.test_window1.show()

    def keyPressEvent(self, event):  # получение событий клавиш
        if event.key() == Qt.Key_A:  # проверка нажатия букв на клавиатуре, чтобы нарисовать рисунки по ключю(букве) в словаре

            self.pixmap2 = QPixmap(self.dictionary["A"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_B:
            self.pixmap2 = QPixmap(self.dictionary["B"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()


        if event.key() == Qt.Key_C:
            self.pixmap2 = QPixmap(self.dictionary["C"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_D:
            self.pixmap2 = QPixmap(self.dictionary["D"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_E:
            self.pixmap2 = QPixmap(self.dictionary["E"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_F:
            self.pixmap2 = QPixmap(self.dictionary["F"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_G:
            self.pixmap2 = QPixmap(self.dictionary["G"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_H:
            self.pixmap2 = QPixmap(self.dictionary["H"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_I:
            self.pixmap2 = QPixmap(self.dictionary["I"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_J:
            self.pixmap2 = QPixmap(self.dictionary["J"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_K:
            self.pixmap2 = QPixmap(self.dictionary["K"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_L:
            self.pixmap2 = QPixmap(self.dictionary["L"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_M:
            self.pixmap2 = QPixmap(self.dictionary["M"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_N:
            self.pixmap2 = QPixmap(self.dictionary["N"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_O:
            self.pixmap2 = QPixmap(self.dictionary["O"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_P:
            self.pixmap2 = QPixmap(self.dictionary["P"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_Q:
            self.pixmap2 = QPixmap(self.dictionary["Q"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_R:
            self.pixmap2 = QPixmap(self.dictionary["R"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_S:
            self.pixmap2 = QPixmap(self.dictionary["S"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_T:
            self.pixmap2 = QPixmap(self.dictionary["T"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_U:
            self.pixmap2 = QPixmap(self.dictionary["U"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_V:
            self.pixmap2 = QPixmap(self.dictionary["V"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_W:
            self.pixmap2 = QPixmap(self.dictionary["W"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_X:
            self.pixmap2 = QPixmap(self.dictionary["X"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_Y:
            self.pixmap2 = QPixmap(self.dictionary["Y"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()

        if event.key() == Qt.Key_Z:
            self.pixmap2 = QPixmap(self.dictionary["Z"])
            self.image = QLabel(self)
            self.image.resize(500, 450)
            self.image.move(270, 25)
            self.image.setPixmap(self.pixmap2)
            self.image.show()


class Window4(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Руководство/Management')
        self.setGeometry(300, 300, 800, 500)
        self.background = QLabel(self)
        self.background.setPixmap(QPixmap("data\\fon_w2.jpg"))
        self.background.show()

        self.label_rus_rules1 = QLabel(self)
        self.label_rus_rules1.setText("Руководство по использованию: Вы можете нажимать буквы на")
        self.label_rus_rules1.resize(750, 100)
        self.label_rus_rules1.setStyleSheet(u"font-size: 25px;")
        self.label_rus_rules1.move(20, 10)

        self.label_rus_rules2 = QLabel(self)
        self.label_rus_rules2.setText("клавиатуре и будут изображения с руками жестов c нажатой")
        self.label_rus_rules2.resize(750, 100)
        self.label_rus_rules2.setStyleSheet(u"font-size: 25px;")
        self.label_rus_rules2.move(20, 50)

        self.label_rus_rules3 = QLabel(self)
        self.label_rus_rules3.setText("буквой. Также вы можете перейти к тестам для самопроверки.")
        self.label_rus_rules3.resize(750, 100)
        self.label_rus_rules3.setStyleSheet(u"font-size: 25px;")
        self.label_rus_rules3.move(20, 90)

        self.label_eng_rules1 = QLabel(self)
        self.label_eng_rules1.setText("Management of using: You can press letters on keyboard and")
        self.label_eng_rules1.resize(750, 100)
        self.label_eng_rules1.setStyleSheet(u"font-size: 25px;")
        self.label_eng_rules1.move(20, 230)

        self.label_eng_rules2 = QLabel(self)
        self.label_eng_rules2.setText("there will also be images with hands gestures with a pressed.")
        self.label_eng_rules2.resize(750, 100)
        self.label_eng_rules2.setStyleSheet(u"font-size: 25px;")
        self.label_eng_rules2.move(20, 270)

        self.label_eng_rules3 = QLabel(self)
        self.label_eng_rules3.setText("You can also go to tests for self-examination.")
        self.label_eng_rules3.resize(750, 100)
        self.label_eng_rules3.setStyleSheet(u"font-size: 25px;")
        self.label_eng_rules3.move(20, 310)

class Test_in_rus1(QtWidgets.QWidget):   # тест для руско-язычных
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Тест на русском языке1')
        self.setGeometry(300, 300, 800, 500)
        self.dialog_btn = QPushButton(self)
        self.dialog_btn.setText("Начать")  # кнопка нужна для получение имени пользователя, для того чтобы записывать результат в бд
        self.dialog_btn.resize(100, 30)
        self.dialog_btn.move(10, 10)
        self.dialog_btn.setStyleSheet(u"font-size: 20px;")
        self.dialog_btn.clicked.connect(self.dialog)
        self.line = QLineEdit(self)  # в переменную line будут записываться имена
        self.line.move(10, 50)
        self.right_answ = 0  # переменная нужна для подсчета правильных ответов
        self.start_btn = QPushButton(self)  # кнопка нужна для того чтобы пользователь мог обновлять вопрос
        self.start_btn.setText("Тесты")
        self.start_btn.resize(100, 30)
        self.start_btn.move(10, 100)
        self.start_btn.setStyleSheet(u"font-size: 20px;")
        self.start_btn.clicked.connect(self.start)
        self.start_btn.clicked.connect(self.count_btn_click)
        self.finish_btn = QPushButton(self)  # кнокпа нужна для того чтобы вводить результаты в бд
        self.finish_btn.setText("Закончить")
        self.finish_btn.resize(120, 30)
        self.finish_btn.move(670, 30)
        self.finish_btn.setStyleSheet(u"font-size: 20px;")
        self.finish_btn.clicked.connect(self.finish)
        self.lbl = QLabel(self)
        self.lbl.setText("Тест для проверки знаний")
        self.lbl.resize(500, 30)
        self.lbl.move(250, 10)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        self.lbl.show()
        self.count = 0  # кнопка нужна для подсчета тестов


        with open("data\csv_file_rus_test.csv") as csv_file:  # открытие csv файла для теста
            reader = csv.DictReader(csv_file, delimiter=";")
            self.diction = {}
            self.inv_dict = {}
            self.lst_img = []
            self.lst_letter = []
            for i in reader:
                rus_letter = str(i["Буква"])
                rus_img = str(i["Картинка"])
                key, val = rus_letter, rus_img
                self.inv_dict[val] = key  # создание обратного словаря для того чтобы потом по картинке удалять букву
                self.diction[key] = val
                self.lst_img.append(rus_img)
                self.lst_letter.append(rus_letter)


    def dialog(self):
        text, ok = QInputDialog.getText(self, 'Начать', 'Введите ваше имя:')

        if ok:
            self.line.setText(str(text))

    def count_btn_click(self):
        self.count += 1

    def start(self):
        self.lst_letter = ['А', 'Б ', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О',
                           'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']  # обновление списка
        self.lst_img = ['data\\тест_буква_а.jpg', 'data\\тест_буква_б.jpg', 'data\\тест_буква_в.jpg',
                        'data\\тест_буква_г.jpg', 'data\\тест_буква_д.jpg', 'data\\тест_буква_е.jpg',
                        'data\\тест_буква_ё.jpg', 'data\\тест_буква_ж.jpg', 'data\\тест_буква_з.jpg',
                        'data\\тест_буква_и.jpg', 'data\\тест_буква_й.jpg', 'data\\тест_буква_к.jpg',
                        'data\\тест_буква_л.jpg', 'data\\тест_буква_м.jpg', 'data\\тест_буква_н.jpg',
                        'data\\тест_буква_о.jpg', 'data\\тест_буква_п.jpg', 'data\\тест_буква_р.jpg',
                        'data\\тест_буква_с.jpg', 'data\\тест_буква_т.jpg', 'data\\тест_буква_у.jpg',
                        'data\\тест_буква_ф.jpg', 'data\\тест_буква_х.jpg', 'data\\тест_буква_ц.jpg',
                        'data\\тест_буква_ч.jpg', 'data\\тест_буква_ш.jpg', 'data\\тест_буква_щ.jpg',
                        'data\\тест_буква_ъ.jpg', 'data\\тест_буква_ы.jpg', 'data\\тест_буква_ь.jpg',
                        'data\\тест_буква_э.jpg', 'data\\тест_буква_ю.jpg', 'data\\тест_буква_я.jpg']  # обновление списка

        self.lbl = QLabel(self)
        self.lbl.setText("Выберите правильный вариант")
        self.lbl.resize(500, 30)
        self.lbl.move(250, 320)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        self.lbl.show()
        self.lbl1 = QLabel(self)
        self.lbl1.setText("1)")
        self.lbl1.resize(50, 50)
        self.lbl1.move(135, 400)
        self.lbl1.setStyleSheet(u"font-size: 20px;")
        self.lbl1.show()
        self.lbl2 = QLabel(self)
        self.lbl2.setText("2)")
        self.lbl2.resize(50, 50)
        self.lbl2.move(295, 400)
        self.lbl2.setStyleSheet(u"font-size: 20px;")
        self.lbl2.show()
        self.lbl3 = QLabel(self)
        self.lbl3.setText("3)")
        self.lbl3.resize(50, 50)
        self.lbl3.move(455, 400)
        self.lbl3.setStyleSheet(u"font-size: 20px;")
        self.lbl3.show()
        self.lbl4 = QLabel(self)
        self.lbl4.setText("4)")
        self.lbl4.resize(50, 50)
        self.lbl4.move(595, 400)
        self.lbl4.setStyleSheet(u"font-size: 20px;")
        self.lbl4.show()
        self.a = random.choice(self.lst_img)  # с помощью рандома выбираются картинки
        self.pixmap1 = QPixmap(self.a)
        self.image = QLabel(self)
        self.image.resize(300, 300)
        self.image.move(300, 25)
        self.image.setPixmap(self.pixmap1)
        self.image.show()

        self.lst = []  # список нужен для того чтобы взять со списка с буквами любые 4 рандомных букв (одна из букв соответсвует рисунку)
        self.lst.append(self.inv_dict[self.a])
        self.lst_letter.remove(self.inv_dict[self.a])
        self.sec_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.sec_ran_let)
        self.lst_letter.remove(self.sec_ran_let)
        self.third_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.third_ran_let)
        self.lst_letter.remove(self.third_ran_let)
        self.four_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.four_ran_let)
        self.lst_copy = self.lst

        self.b = random.choice(self.lst)  # рандомно выбирается буква но уже без буквы по рисунку
        self.answ_btn1 = QPushButton(self)
        self.answ_btn1.setText(self.b)
        self.answ_btn1.resize(50, 50)
        self.answ_btn1.move(160, 400)
        self.answ_btn1.setStyleSheet(u"font-size: 25px;")
        self.answ_btn1.show()
        self.answ_btn1.clicked.connect(self.btn1)
        self.lst.remove(self.b)
        self.e = random.choice(self.lst)
        self.answ_btn2 = QPushButton(self)
        self.answ_btn2.setText(self.e)  # из словаря по рисунку выбирается соответсвующая буква
        self.answ_btn2.resize(50, 50)
        self.answ_btn2.move(320, 400)
        self.answ_btn2.setStyleSheet(u"font-size: 25px;")
        self.answ_btn2.show()
        self.answ_btn2.clicked.connect(self.btn2)
        self.lst.remove(self.e)
        self.c = random.choice(self.lst)
        self.answ_btn3 = QPushButton(self)
        self.answ_btn3.setText(self.c)
        self.answ_btn3.resize(50, 50)
        self.answ_btn3.move(480, 400)
        self.answ_btn3.setStyleSheet(u"font-size: 25px;")
        self.answ_btn3.show()
        self.answ_btn3.clicked.connect(self.btn3)
        self.lst.remove(self.c)
        self.d = random.choice(self.lst)
        self.answ_btn4 = QPushButton(self)
        self.answ_btn4.setText(self.d)
        self.answ_btn4.resize(50, 50)
        self.answ_btn4.move(620, 400)
        self.answ_btn4.setStyleSheet(u"font-size: 25px;")
        self.answ_btn4.show()
        self.answ_btn4.clicked.connect(self.btn4)
        self.lst_copy = [self.inv_dict[self.a], self.sec_ran_let, self.third_ran_let, self.four_ran_let]
        # в этом списке первым элементом являяется буква соответсвующая рисунку

    def wrong_ans(self):
        QMessageBox.information(self, "Предупреждение", "неверный ответ", QMessageBox.Ok) # при нажатии не правильной буквы выходит диалог. окно

    def btn1(self):
        if self.answ_btn1.text() == self.lst_copy[0]:  # кнопки сравниваются с правильной буквой
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn2(self):
        if self.answ_btn2.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn3(self):
        if self.answ_btn3.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn4(self):
        if self.answ_btn4.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def finish(self):
        if self.count >= 10:  # пользователь должен сделать как минимум 10 тестов
            self.procent = (self.right_answ / self.count) * 100  # высчитывается процент выполнения

            db = sqlite3.connect('data\\table_rus.db')
            sql = db.cursor()
            db.commit()
            sql.execute(f"INSERT INTO users2(user_name, user_percent) VALUES ('{self.line.text()}', '{self.procent}')")
            db.commit()                                                       # имя пользователя
            self.next_w()
        else:
            QMessageBox.information(self, "Warning", "Do some more tests", QMessageBox.Ok)

    def next_w(self):
        self.result_w = Result_rus()
        self.result_w.show()

class Test_in_eng(QtWidgets.QWidget):  # окно для англо-язычных (здесь все такое как в окне для русско-язычных)
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Test in english language')
        self.setGeometry(300, 300, 800, 500)
        self.right_answ = 0
        self.count = 0
        self.dialog_btn = QPushButton(self)
        self.dialog_btn.setText("Start")
        self.dialog_btn.resize(100, 30)
        self.dialog_btn.move(10, 10)
        self.dialog_btn.setStyleSheet(u"font-size: 20px;")
        self.dialog_btn.clicked.connect(self.dialog)
        self.line = QLineEdit(self)
        self.line.move(10, 50)
        self.start_btn = QPushButton(self)
        self.start_btn.setText("Tests")
        self.start_btn.resize(100, 30)
        self.start_btn.move(10, 100)
        self.start_btn.setStyleSheet(u"font-size: 20px;")
        self.start_btn.clicked.connect(self.tests)
        self.start_btn.clicked.connect(self.count_btn_click)
        self.finish_btn = QPushButton(self)
        self.finish_btn.setText("Finish")
        self.finish_btn.resize(120, 30)
        self.finish_btn.move(670, 30)
        self.finish_btn.setStyleSheet(u"font-size: 20px;")
        self.finish_btn.clicked.connect(self.finish)
        self.lbl = QLabel(self)
        self.lbl.setText("Test for check knoweledges")
        self.lbl.resize(500, 30)
        self.lbl.move(250, 10)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        self.lbl.show()


        file_txt = open("data\english_alph_tets.txt")
        self.dictionary = {}
        self.inv_dict = {}
        self.lst_img = []
        self.lst_letter = []
        for row in file_txt:
            eng_letter, eng_img = row.rstrip("\n").split(",")
            key, val = eng_letter, eng_img
            self.lst_img.append(eng_img)
            self.lst_letter.append(eng_letter)
            self.inv_dict[val] = key
            self.dictionary[key] = val


    def dialog(self):
        text, ok = QInputDialog.getText(self, 'Start', 'Enter your name:')

        if ok:
            self.line.setText(str(text))

    def count_btn_click(self):
        self.count += 1

    def tests(self):
        if self.count == 10:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Dialog")
            dlg.setText("Enough")
            button = dlg.exec()
            if button == QMessageBox.Ok:
                pass
        self.lst_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.lst_img = ['data\\test_letter_a.jpg', 'data\\test_letter_b', 'data\\test_letter_c', 'data\\test_letter_d',
                        'data\\test_letter_e', 'data\\test_letter_f', 'data\\test_letter_g', 'data\\test_letter_h',
                        'data\\test_letter_i', 'data\\test_letter_j', 'data\\test_letter_k', 'data\\test_letter_l',
                        'data\\test_letter_m', 'data\\test_letter_n', 'data\\test_letter_o', 'data\\test_letter_p',
                        'data\\test_letter_q', 'data\\test_letter_r', 'data\\test_letter_s', 'data\\test_letter_t',
                        'data\\test_letter_u', 'data\\test_letter_v', 'data\\test_letter_w', 'data\\test_letter_x',
                        'data\\test_letter_y', 'data\\test_letter_z']
        self.lbl = QLabel(self)
        self.lbl.setText("Choice the right variant")
        self.lbl.resize(500, 30)
        self.lbl.move(250, 360)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        self.lbl.show()
        self.lbl1 = QLabel(self)
        self.lbl1.setText("1)")
        self.lbl1.resize(50, 50)
        self.lbl1.move(135, 420)
        self.lbl1.setStyleSheet(u"font-size: 20px;")
        self.lbl1.show()
        self.lbl2 = QLabel(self)
        self.lbl2.setText("2)")
        self.lbl2.resize(50, 50)
        self.lbl2.move(295, 420)
        self.lbl2.setStyleSheet(u"font-size: 20px;")
        self.lbl2.show()
        self.lbl3 = QLabel(self)
        self.lbl3.setText("3)")
        self.lbl3.resize(50, 50)
        self.lbl3.move(455, 420)
        self.lbl3.setStyleSheet(u"font-size: 20px;")
        self.lbl3.show()
        self.lbl4 = QLabel(self)
        self.lbl4.setText("4)")
        self.lbl4.resize(50, 50)
        self.lbl4.move(595, 420)
        self.lbl4.setStyleSheet(u"font-size: 20px;")
        self.lbl4.show()

        self.a = random.choice(self.lst_img)
        self.pixmap1 = QPixmap(self.a)
        self.image = QLabel(self)
        self.image.resize(300, 300)
        self.image.move(250, 50)
        self.image.setPixmap(self.pixmap1)
        self.image.show()

        self.lst = []
        self.lst.append(self.inv_dict[self.a])
        self.lst_letter.remove(self.inv_dict[self.a])
        self.sec_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.sec_ran_let)
        self.lst_letter.remove(self.sec_ran_let)
        self.third_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.third_ran_let)
        self.lst_letter.remove(self.third_ran_let)
        self.four_ran_let = random.choice(self.lst_letter)
        self.lst.append(self.four_ran_let)
        self.lst_copy = self.lst

        self.b = random.choice(self.lst)  # рандомно выбирается буква но уже без буквы по рисунку
        self.answ_btn1 = QPushButton(self)
        self.answ_btn1.setText(self.b)
        self.answ_btn1.resize(50, 50)
        self.answ_btn1.move(160, 420)
        self.answ_btn1.setStyleSheet(u"font-size: 25px;")
        self.answ_btn1.show()
        self.answ_btn1.clicked.connect(self.btn1)
        self.lst.remove(self.b)
        self.e = random.choice(self.lst)
        self.answ_btn2 = QPushButton(self)
        self.answ_btn2.setText(self.e)  # из словаря по рисунку выбирается соответсвующая буква
        self.answ_btn2.resize(50, 50)
        self.answ_btn2.move(320, 420)
        self.answ_btn2.setStyleSheet(u"font-size: 25px;")
        self.answ_btn2.show()
        self.answ_btn2.clicked.connect(self.btn2)
        self.lst.remove(self.e)
        self.c = random.choice(self.lst)
        self.answ_btn3 = QPushButton(self)
        self.answ_btn3.setText(self.c)
        self.answ_btn3.resize(50, 50)
        self.answ_btn3.move(480, 420)
        self.answ_btn3.setStyleSheet(u"font-size: 25px;")
        self.answ_btn3.show()
        self.answ_btn3.clicked.connect(self.btn3)
        self.lst.remove(self.c)
        self.d = random.choice(self.lst)
        self.answ_btn4 = QPushButton(self)
        self.answ_btn4.setText(self.d)
        self.answ_btn4.resize(50, 50)
        self.answ_btn4.move(620, 420)
        self.answ_btn4.setStyleSheet(u"font-size: 25px;")
        self.answ_btn4.show()
        self.answ_btn4.clicked.connect(self.btn4)
        self.lst_copy = [self.inv_dict[self.a], self.sec_ran_let, self.third_ran_let, self.four_ran_let]

    def wrong_ans(self):
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Mistake")
        dlg.setText("Wrong answer")
        button = dlg.exec()

        if button == QMessageBox.Ok:
            pass

    def btn1(self):
        if self.answ_btn1.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn2(self):
        if self.answ_btn2.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn3(self):
        if self.answ_btn3.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()

    def btn4(self):
        if self.answ_btn4.text() == self.lst_copy[0]:
            self.right_answ += 1
        else:
            self.right_answ = self.right_answ  # по нажатию неправильной буквы количество правильных ответов остается неизменным
            self.wrong_ans()



    def finish(self):
        if self.count >= 10:
            self.procent = (self.right_answ / self.count) * 100

            db = sqlite3.connect('data\\table_eng.db')
            sql = db.cursor()
            db.commit()
            sql.execute(f"INSERT INTO users(user_name, user_percent) VALUES ('{self.line.text()}', '{self.procent}')")
            db.commit()

            self.next_w()
        else:
            QMessageBox.information(self, "Warning", "Do some more tests", QMessageBox.Ok)

    def next_w(self):
        self.result_w = Result_eng()
        self.result_w.show()

class Result_eng(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Result')
        self.setGeometry(300, 300, 800, 500)
        self.lbl = QLabel(self)
        self.lbl.setText("Below are the results of people who passed the tests")
        self.lbl.resize(700, 30)
        self.lbl.move(10, 10)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('data\\table_eng.db')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('users')
        model.select()
        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(50, 50)
        view.resize(450, 400)

class Result_rus(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Результаты')
        self.setGeometry(300, 300, 800, 500)
        self.lbl = QLabel(self)
        self.lbl.setText("Ниже представлены результаты людей пройденных тест")
        self.lbl.resize(700, 30)
        self.lbl.move(10, 10)
        self.lbl.setStyleSheet(u"font-size: 20px;")
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('data\\table_rus.db')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('users2')
        model.select()
        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(50, 50)
        view.resize(450, 400)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window1()
    ex.show()
    sys.exit(app.exec_())
