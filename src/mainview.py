#-*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from src.playlist import PlayList
from src.webplayer import WebPlayer
from src.addlist import AddList

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Youtube Player')
        self.main_layout = QGridLayout()

        text_css = """
        QPushButton {
            border-style: solid;
            border-color: gray;
            border-width: 2px;
            border-radius: 10px; 
        }
        """

        self.web_player = WebPlayer()
        self.main_layout.addWidget(self.web_player, 0, 0, 2, 5)

        self.list_view = PlayList()
        self.main_layout.addWidget(self.list_view, 0, 6, 1, 2)

        self.add_button = QPushButton('노래 추가')
        self.add_button.clicked.connect(self.add)
        # self.add_button.setStyleSheet(text_css)
        self.main_layout.addWidget(self.add_button, 1, 6, 1, 1)

        self.delete_button = QPushButton('노래 삭제')
        self.delete_button.clicked.connect(self.delete)
        # self.delete_button.setStyleSheet(text_css)
        self.main_layout.addWidget(self.delete_button, 1, 7, 1, 1)

        self.add_list = AddList()
        self.add_list.hide()

        self.setLayout(self.main_layout)

    def closeEvent(self, event):
        replay = QMessageBox.question(self, 'Message', '정말 프로그램을 종료하시겠습니까?', QMessageBox.Yes, QMessageBox.No)

        if replay == QMessageBox.Yes:
            QApplication.instance().closeAllWindows()
        else:
            event.ignore()

    def delete(self):
        key = self.list_view.currentIndex().data()
        message = '{0}를 재생목록에서 삭제하시겠습니까?'.format(key)
        replay = QMessageBox.question(self, 'Message', message, QMessageBox.Yes, QMessageBox.No)

        if replay == QMessageBox.Yes:
            self.list_view.remove_video(key)

    def add(self):
        self.add_list.show()

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    view = MainView()
    view.show()
    sys.exit(app.exec_())