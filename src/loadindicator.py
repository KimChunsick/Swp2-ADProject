#-*- coding: utf-8 -*-
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QPainter, QColor
from PyQt5.QtWidgets import QWidget

class LoadingIndicator(QWidget):

    def __init__(self, delay, parent=None):
        super().__init__(parent)
        palette = QPalette()
        palette.setColor(palette.Background, QColor(0, 0, 0, 170))
        self.setPalette(palette)

        self.timer_id = -1
        self.angle = 0
        self.delay = delay
        self.color = Qt.white
        self.setFocusPolicy(Qt.NoFocus)
        self.setAutoFillBackground(True)

    # 애니메이션 시작
    def start(self):
        if self.timer_id != -1:
            self.killTimer(self.timer_id)
        self.timer_id = self.startTimer(self.delay)

    # 애니메이션 멈춤
    def stop(self):
        if self.timer_id != -1:
            self.killTimer(self.timer_id)
        self.timer_id = -1

    def closeEvent(self, event):
        self.indicator.stop()

    def timerEvent(self, event):
        self.angle = (self.angle + 30) % 360
        self.update()

    def paintEvent(self, event):
        if self.timer_id == -1:
            return

        size = min(self.width(), self.height())

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        # painter.setBack

        outer_radius = (size - 1) * 0.5
        inner_radius = (size - 1) * 0.5 * 0.38

        capsule_height = outer_radius - inner_radius
        capsule_width = capsule_height * .23 if (size > 32) else capsule_height * .35
        capsule_radius = capsule_width / 2

        for i in range(0, 12):
            color = QColor(self.color)

            if self.timer_id != -1:
                color.setAlphaF(1.0 - (i / 12.0))
            else:
                color.setAlphaF(0.2)

            painter.setPen(Qt.NoPen)
            painter.setBrush(color)
            painter.save()
            painter.translate(self.rect().center())
            painter.rotate(self.angle - (i * 30.0))
            painter.drawRoundedRect(capsule_width * -0.5, (inner_radius + capsule_height) * -1, capsule_width, capsule_height, capsule_radius, capsule_radius)
            painter.restore()
