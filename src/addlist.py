#-*- coding: utf-8 -*-
from PyQt5.QtWidgets import QWidget, QLineEdit, QGridLayout, QListView, QPushButton, QMessageBox
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from src.notification import NotificationCenter, NotificationName
from src.loadindicator import LoadingIndicator
from urllib import request
from urllib.parse import quote
import json
import ssl
import threading

class AddList(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 클래스 기본 셋팅
        ssl._create_default_https_context = ssl._create_unverified_context
        self.query = 'https://www.googleapis.com/youtube/v3/search?part=snippet&q={0}&maxResults=15&type=video&key=[your_youtube_api_key]'
        self.set_key_in_query()

        # UI 셋팅
        self.setWindowTitle('노래 추가')
        self.main_layout = QGridLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText('동영상 제목을 입력해주세요.')
        self.main_layout.addWidget(self.input_field, 0, 0, 1, 1)

        self.search_button = QPushButton('검색')
        self.search_button.clicked.connect(self.did_clicked_item)
        self.main_layout.addWidget(self.search_button, 0, 1, 1, 1)

        self.list_view = QListView()
        self.main_layout.addWidget(self.list_view, 1, 0, 1, 2)

        self.searched_data = dict()
        self.model = QStandardItemModel()
        self.list_view.clicked.connect(self.did_clicked_item)
        self.list_view.setModel(self.model)

        self.indicator = LoadingIndicator(70)
        self.indicator.start()
        self.indicator.hide()
        self.main_layout.addWidget(self.indicator, 0, 0, 2, 3)

        self.setLayout(self.main_layout)

    def showEvent(self, event):
        self.input_field.setText("")
        self.model.removeRows(0, self.model.rowCount())

    # key.key 파일에서 불러온 youtube api key값을 적용
    def set_key_in_query(self):
        try:
            import os
            path = os.getcwd() + '/support/key.key'
            file = open(path, 'r')
            self.query = self.query.replace('[your_youtube_api_key]', file.read())
            file.close()
        except Exception as e:
            import sys
            QMessageBox.critical(self, 'Message', '프로그램에서 예상치 못한 오류가 발생했습니다.\n프로그램을 종료합니다.', QMessageBox.Yes)
            print(e)
            sys.exit(-1)

    # 검색한 결과를 보여줌
    def show_search_result(self):
        query = self.query.format(quote(self.input_field.text()))
        result = request.urlopen(query).read().decode('utf-8')
        json_result = json.loads(result)
        self.model.removeRows(0, self.model.rowCount())
        for temp in json_result['items']:
            title = temp['snippet']['title']
            videoId = temp['id']['videoId']
            self.searched_data[title] = videoId
            self.model.appendRow(QStandardItem(title))
        self.indicator.hide()

    # 검색 버튼을 눌렀을 때
    def did_clicked_search(self):
        if self.input_field.text() == '':
            return

        self.indicator.show()
        thread = threading.Thread(target=self.show_search_result)
        thread.daemon = True
        thread.start()

    # 검색한 결과에서 노래를 골랐을 때
    def did_clicked_item(self, sender):
        key = sender.data()
        value = self.searched_data[key]
        NotificationCenter.notification(NotificationName.add_video, (key, value))
