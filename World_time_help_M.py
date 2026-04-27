import os
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QSettings
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout
from World_time_lib import ORGANIZATION_NAME, APPLICATION_NAME
from World_time_help import Ui_Help_Window

class HelpWindow(QtWidgets.QMainWindow, Ui_Help_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.WindowType.Window)
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.window_section = "Help_Window"  # Секция параметров окна
        self.save_geometry = self.settings.value(self.window_section + "/geometry")
        self.save_windowState = self.settings.value(self.window_section + "/windowState")

        # Проверяем, что данные не None и восстанавливаем
        if self.save_geometry is not None:
            self.restoreGeometry(self.save_geometry)
        if self.save_windowState is not None:
            self.restoreState(self.save_windowState)

        self.browser = QWebEngineView()

        # Проверяем, нет ли уже layout у frame (Designer иногда его создает)
        if self.frame.layout() is None:
            layout = QVBoxLayout(self.frame)
            layout.setContentsMargins(0, 0, 0, 0)  # Убираем белые рамки вокруг браузера
            self.frame.setLayout(layout)
        self.frame.layout().addWidget(self.browser)
        self.load_url()

    def load_url(self, url=None):
        """Загрузить страницу в браузер"""
        if not url:
            url = "Help_World_time//index.html"
        if url.startswith("http"):
            self.browser.load(QUrl(url))
        else:
            # локальный HTML-файл
            self.browser.load(QUrl.fromLocalFile(os.path.abspath(url)))

    def closeEvent(self, event):
        # Ваше действие при закрытии окна
        # Если размер окна изменился, то сохраняем.
        if self.save_geometry != self.saveGeometry():
            self.settings.setValue(self.window_section + "/geometry",
                                   self.saveGeometry())  # Сохранение размера окна
        # Если состояние окна изменилось, то сохраняем
        if self.save_windowState != self.saveState():
            self.settings.setValue(self.window_section + "/windowState",
                                   self.saveState())  # Сохранение состояния окна
        event.accept()  # Закрываем окно
