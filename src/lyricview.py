# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect
from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QScrollArea, QPushButton, QSlider
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
        self.setWindowFlags(PyQt5.QtCore.Qt.CustomizeWindowHint)
        self.main_layout = QGridLayout()

        self.scrollArea = QScrollArea()
        self.scrollArea.setGeometry(QRect(10, 10, 201, 121))
        self.scrollArea.setWidgetResizable(True)

        self.fontsize_label = QLabel()
        self.fontsize_label.setText('font size')
        self.main_layout.addWidget(self.fontsize_label,1,0,1,1)

        self.fontsize_minus_button = QPushButton('-')
        self.fontsize_minus_button.clicked.connect(self.minus)
        self.main_layout.addWidget(self.fontsize_minus_button, 1,1,1,1)

        self.fontsize_plus_button = QPushButton('+')
        self.fontsize_plus_button.clicked.connect(self.plus)
        self.main_layout.addWidget(self.fontsize_plus_button, 1,2,1,1)

        self.transparent_label = QLabel()
        self.transparent_label.setText('transparency')
        self.main_layout.addWidget(self.transparent_label,1,5,1,1)

        self.transparent_slider = QSlider(PyQt5.QtCore.Qt.Horizontal)
        self.transparent_slider.setRange(0, 100)
        self.transparent_slider.setValue(50)
        self.transparent_slider.valueChanged[int].connect(self.transparentSlideValueChanged)
        self.main_layout.addWidget(self.transparent_slider, 1,6,2,1)

        self.lyric_view = QLabel()
        self.fontsize = 20
        self.lyric_view.setStyleSheet("font: %dpt Consolas" % (self.fontsize))
        self.lyric_view.setAlignment(PyQt5.QtCore.Qt.AlignCenter)
        self.lyric_view.setText('')

        self.scrollArea.setWidget(self.lyric_view)

        self.main_layout.addWidget(self.scrollArea,0,0,1,9)
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

    def setLyric(self, info):
        data = []
        for i in ['-',':',',']:
            if i in info:
                data = info.split(i)
                break
        lyric_loader = LyricLoader(data)
        lines = lyric_loader.lyric.split('<br>')
        lyric = ''
        for i in lines:
            lyric += i[10:] + '\r\n'
        self.lyric_view.setText(lyric)

