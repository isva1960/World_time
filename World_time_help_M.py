import sys, os
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QTranslator, QLibraryInfo, QSettings, QResource
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout, QApplication
from World_time_lib import ORGANIZATION_NAME, APPLICATION_NAME
from World_time_help import Ui_Help_Window
from pathlib import Path

TST = True


def register_resources():
    rcc_path = Path(__file__).parent / "World_time.rcc"
    rcc_path_str = str(rcc_path)
    QResource.registerResource(rcc_path_str)


class Help_Window(QtWidgets.QMainWindow, Ui_Help_Window):
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
        # Абсолютный путь к index.html
        # Создаём layout для frame
        layout = QVBoxLayout(self.frame)
        layout.addWidget(self.browser)
        # Привязываем layout к frame
        self.frame.setLayout(layout)
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
        if not TST:
            if self.save_geometry != self.saveGeometry():
                self.settings.setValue(self.window_section + "/geometry",
                                       self.saveGeometry())  # Сохранение размера окна
            # Если состояние окна изменилось, то сохраняем
            if self.save_windowState != self.saveState():
                self.settings.setValue(self.window_section + "/windowState",
                                       self.saveState())  # Сохранение состояния окна
        event.accept()  # Закрываем окно


if __name__ == '__main__':
    register_resources()
    app = QApplication(sys.argv)
    # app.setStyle(APP_STYLE)
    # Создаём переводчик
    qt_translator = QTranslator()
    qt_translator.load(
        "qtbase_ru",
        QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    )
    app.installTranslator(qt_translator)
    Window = Help_Window()
    Window.show()
    sys.exit(app.exec())
