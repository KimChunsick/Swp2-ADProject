from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import pyqtSlot
from src.notification import NotificationCenter, NotificationName

class WebPlayer(QWebEngineView):

    def __init__(self, parent=None):
        super().__init__(parent)

        file = open('./support/webplayer.html', 'r')
        self.html = file.read()

        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        self.setHtml(self.html)
        self.web_channel = QWebChannel(self)
        self.web_channel.registerObject('handler', self)
        self.page().setWebChannel(self.web_channel)
        NotificationCenter.subscribe(NotificationName.play, self.play)

    def play(self, token):
        html = self.html.replace('{0}', token)
        self.setHtml(html)


    @pyqtSlot()
    def endVideo(self):
        NotificationCenter.notification(NotificationName.end_video)
