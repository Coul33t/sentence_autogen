# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineedit_input_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_input_file.setGeometry(QtCore.QRect(110, 10, 671, 22))
        self.lineedit_input_file.setObjectName("lineedit_input_file")
        self.pushbutton_input_file = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_input_file.setGeometry(QtCore.QRect(10, 10, 93, 28))
        self.pushbutton_input_file.setObjectName("pushbutton_input_file")
        self.lineedit_output_file = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_output_file.setGeometry(QtCore.QRect(110, 60, 671, 22))
        self.lineedit_output_file.setObjectName("lineedit_output_file")
        self.label_output_file = QtWidgets.QLabel(self.centralwidget)
        self.label_output_file.setGeometry(QtCore.QRect(30, 60, 71, 16))
        self.label_output_file.setObjectName("label_output_file")
        self.pushbutton_one_sentence = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_one_sentence.setGeometry(QtCore.QRect(10, 200, 93, 28))
        self.pushbutton_one_sentence.setObjectName("pushbutton_one_sentence")
        self.textbrowser_one_sentence = QtWidgets.QTextBrowser(self.centralwidget)
        self.textbrowser_one_sentence.setGeometry(QtCore.QRect(110, 200, 671, 192))
        self.textbrowser_one_sentence.setObjectName("textbrowser_one_sentence")
        self.spinbox_markov = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_markov.setGeometry(QtCore.QRect(120, 120, 42, 22))
        self.spinbox_markov.setObjectName("spinbox_markov")
        self.label_markov = QtWidgets.QLabel(self.centralwidget)
        self.label_markov.setGeometry(QtCore.QRect(120, 100, 51, 16))
        self.label_markov.setObjectName("label_markov")
        self.pushbutton_full_sentences = QtWidgets.QPushButton(self.centralwidget)
        self.pushbutton_full_sentences.setGeometry(QtCore.QRect(10, 397, 771, 141))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pushbutton_full_sentences.setFont(font)
        self.pushbutton_full_sentences.setObjectName("pushbutton_full_sentences")
        self.label_sentence_number = QtWidgets.QLabel(self.centralwidget)
        self.label_sentence_number.setGeometry(QtCore.QRect(170, 100, 191, 16))
        self.label_sentence_number.setObjectName("label_sentence_number")
        self.lineedit_sentence_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineedit_sentence_number.setGeometry(QtCore.QRect(170, 120, 191, 22))
        self.lineedit_sentence_number.setObjectName("lineedit_sentence_number")
        self.label_min_words = QtWidgets.QLabel(self.centralwidget)
        self.label_min_words.setGeometry(QtCore.QRect(410, 100, 161, 16))
        self.label_min_words.setObjectName("label_min_words")
        self.label_max_words = QtWidgets.QLabel(self.centralwidget)
        self.label_max_words.setGeometry(QtCore.QRect(590, 100, 161, 16))
        self.label_max_words.setObjectName("label_max_words")
        self.spinbox_min_words = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_min_words.setGeometry(QtCore.QRect(410, 120, 42, 22))
        self.spinbox_min_words.setObjectName("spinbox_min_words")
        self.spinbox_max_words = QtWidgets.QSpinBox(self.centralwidget)
        self.spinbox_max_words.setGeometry(QtCore.QRect(590, 120, 42, 22))
        self.spinbox_max_words.setObjectName("spinbox_max_words")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushbutton_input_file.setText(_translate("MainWindow", "Input file"))
        self.label_output_file.setText(_translate("MainWindow", "Output file"))
        self.pushbutton_one_sentence.setText(_translate("MainWindow", "Bot me once"))
        self.label_markov.setText(_translate("MainWindow", "Markov"))
        self.pushbutton_full_sentences.setText(_translate("MainWindow", "Let\'s go"))
        self.label_sentence_number.setText(_translate("MainWindow", "Number of sentences to generate"))
        self.label_min_words.setText(_translate("MainWindow", "Minimum number of words"))
        self.label_max_words.setText(_translate("MainWindow", "Maximum number of words"))

