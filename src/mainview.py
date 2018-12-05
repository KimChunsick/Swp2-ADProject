#-*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings

html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        <style>
            .player iframe {
                position: absolute;
                width: 100%;
                height: 100%;
                left: 0;
                top: 0;
            }
            body {
                overflow:hidden;
            }
        </style>
    </head>
    <body>
        <div class="player">
            <iframe id="ytplayer" allowfullscreen frameborder="0" width="100%" height="100%" scrolling="no" src="https://www.youtube.com/embed/{0}?enablejsapi=1"></iframe>
        </div>
        <script src=https://www.youtube.com/player_api></script>
        <script>
        var player;
        function onYouTubePlayerAPIReady() {
            player = new YT.Player('ytplayer', {
                events: {
                    'onReady': onPlayerReady
                }
            });
        }
        function onPlayerReady(event) {
            event.target.playVideo();
        }
        </script>
    </body>
</html>
""".replace("{0}", "lDPcSLGB0nQ")

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Youtube Player")
        self.main_layout = QGridLayout()

        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        self.web_view = QWebEngineView()
        self.web_view.setHtml(html)
        self.web_view.setObjectName("webview")
        self.main_layout.addWidget(self.web_view)
        self.setLayout(self.main_layout)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    view = MainView()
    view.show()
    sys.exit(app.exec_())