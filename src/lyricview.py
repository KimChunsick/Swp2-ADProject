# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QScrollArea, QPushButton, QSlider, QLineEdit
import PyQt5.QtCore

from src.notification import NotificationCenter, NotificationName
from src.lyricloader import LyricLoader


class LyricView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        NotificationCenter.subscribe(NotificationName.update, self.setLyric)

        self.offset = 0
        self.setWindowTitle('Lyric')
        self.setWindowOpacity(0.5)
        self.setWindowFlags(PyQt5.QtCore.Qt.CustomizeWindowHint | PyQt5.QtCore.Qt.WindowStaysOnTopHint)
        self.main_layout = QGridLayout()

        self.scrollArea = QScrollArea()
        self.scrollArea.setGeometry(QRect(10, 10, 201, 121))
        self.scrollArea.setWidgetResizable(True)

        self.sec_layout = QGridLayout()
        self.fontsize_label = QLabel()
        self.fontsize_label.setText('Font Size')
        self.sec_layout.addWidget(self.fontsize_label, 0, 0, 1, 1)

        self.fontsize_minus_button = QPushButton('-')
        self.fontsize_minus_button.clicked.connect(self.minus)
        self.sec_layout.addWidget(self.fontsize_minus_button, 0, 1, 1, 1)

        self.fontsize_plus_button = QPushButton('+')
        self.fontsize_plus_button.clicked.connect(self.plus)
        self.sec_layout.addWidget(self.fontsize_plus_button, 0, 2, 1, 1)

        self.transparent_label = QLabel()
        self.transparent_label.setText('Transparency')
        self.sec_layout.addWidget(self.transparent_label, 0, 5, 1, 1)

        self.transparent_slider = QSlider(PyQt5.QtCore.Qt.Horizontal)
        self.transparent_slider.setRange(0, 100)
        self.transparent_slider.setValue(50)
        self.transparent_slider.valueChanged[int].connect(self.transparentSlideValueChanged)
        self.sec_layout.addWidget(self.transparent_slider, 0, 6, 1, 1)

        self.main_layout.addLayout(self.sec_layout, 1, 0, 1, 1)


        self.lyric_view = QLabel()
        self.fontsize = 20
        self.lyric_view.setStyleSheet("font: %dpt Consolas" % (self.fontsize))
        self.lyric_view.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.lyric_view.setText('')

        self.scrollArea.setWidget(self.lyric_view)

        self.main_layout.addWidget(self.scrollArea, 0, 0, 1, 9)

        self.thd_layout = QGridLayout()
        self.artist_label = QLabel('Artist : ')
        self.thd_layout.addWidget(self.artist_label, 0, 0, 1, 1)
        self.artist_input = QLineEdit()
        self.thd_layout.addWidget(self.artist_input, 0, 1, 1, 1)
        self.title_label = QLabel('Title : ')
        self.thd_layout.addWidget(self.title_label, 0, 2, 1, 1)
        self.title_input = QLineEdit()
        self.thd_layout.addWidget(self.title_input, 0, 3, 1, 1)
        self.search_button = QPushButton('Search')
        self.search_button.clicked.connect(self.searchLyric)
        self.thd_layout.addWidget(self.search_button, 0, 4, 1, 1)
        self.main_layout.addLayout(self.thd_layout, 2, 0, 1, 1)

        self.setLayout(self.main_layout)

    def minus(self):
        self.fontsize -= 1
        if self.fontsize <= 1:
            self.fontsize = 1
        self.lyric_view.setStyleSheet("font: %dpt Consolas" % (self.fontsize))

    def plus(self):
        self.fontsize += 1
        self.lyric_view.setStyleSheet("font: %dpt Consolas" % (self.fontsize))

    def transparentSlideValueChanged(self):
        self.setWindowOpacity(self.transparent_slider.value() * 0.01)

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

    def searchLyric(self):
        self.setLyricHelper([self.artist_input.text(), self.title_input.text()])

    def setLyric(self, info):
        data = []
        for i in ['-', ':', ',']:
            if i in info:
                data = info.split(i)
                break

        self.artist_input.setText(data[0])
        self.title_input.setText(data[1])
        self.setLyricHelper(data)

    def setLyricHelper(self, data):
        lyric_loader = LyricLoader(data)
        lines = lyric_loader.lyric.split('<br>')
        lyric = ''
        for i in lines:
            lyric += i[10:] + '\r\n'
        self.lyric_view.setText(lyric)
