import os
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtCore import QSettings
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import QVBoxLayout
from World_time_lib import ORGANIZATION_NAME, APPLICATION_NAME
from World_time_help import Ui_Help_Window

from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWidgets import QMenu
from PyQt6 import QtGui


class MyWebView(QWebEngineView):
    # noinspection PyUnresolvedReferences
    def contextMenuEvent(self, event):
        # 1. Создаем свое меню вручную
        menu = QMenu(self)
        page = self.page()

        # 2. Добавляем только нужные действия на русском языке
        # Метод page().action(WebAction) возвращает готовый объект QAction

        act_back = page.action(QWebEnginePage.WebAction.Back)
        act_back.setText("Назад")
        menu.addAction(act_back)

        act_fwd = page.action(QWebEnginePage.WebAction.Forward)
        act_fwd.setText("Вперед")
        menu.addAction(act_fwd)

        act_reload = page.action(QWebEnginePage.WebAction.Reload)
        act_reload.setText("Перезагрузить")
        menu.addAction(act_reload)

        menu.addSeparator()

        act_sel_all = page.action(QWebEnginePage.WebAction.SelectAll)
        act_sel_all.setText("Выделить всё")
        menu.addAction(act_sel_all)

        act_copy = page.action(QWebEnginePage.WebAction.Copy)
        act_copy.setText("Копировать")
        menu.addAction(act_copy)
        # --- Кнопка Закрыть ---
        # Добавляем отступ, чтобы кнопка Закрыть была чуть в стороне от навигации
        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        toolbar.addWidget(spacer)  # Этот "распор" прижмет кнопку Закрыть вправо

        # Создаем само действие
        # noinspection PyUnresolvedReferences
        close_action = QtGui.QAction("Закрыть", self)
        close_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton))
        close_action.triggered.connect(self.close)  # Подключаем к закрытию окна
        toolbar.addAction(close_action)

        # 3. Показываем меню
        menu.exec(event.globalPos())


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

        # 1. Создаем сам виджет браузера
        self.browser = MyWebView()

        # Проверяем, нет ли уже layout у frame (Designer иногда его создает)
        if self.frame.layout() is None:
            layout = QVBoxLayout(self.frame)
            layout.setContentsMargins(0, 0, 0, 0)  # Убираем белые рамки вокруг браузера
            self.frame.setLayout(layout)
        self.frame.layout().addWidget(self.browser)
        # 1. Создаем панель инструментов
        self.setup_navigation()
        self.load_url()

    # noinspection PyUnresolvedReferences
    def setup_navigation(self):
        toolbar = self.addToolBar("Навигация")
        toolbar.setMovable(False)  # Закрепляем, чтобы нельзя было перетащить
        toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextBesideIcon)
        # toolbar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)

        # 2. Получаем стандартные действия от страницы браузера
        page = self.browser.page()

        # Назад
        back_action = page.action(QWebEnginePage.WebAction.Back)
        back_action.setText("Назад")
        back_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowBack))
        toolbar.addAction(back_action)

        # Вперед
        forward_action = page.action(QWebEnginePage.WebAction.Forward)
        forward_action.setText("Вперед")
        forward_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_ArrowForward))
        toolbar.addAction(forward_action)

        toolbar.addSeparator()

        # Перезагрузить
        reload_action = page.action(QWebEnginePage.WebAction.Reload)
        reload_action.setText("Обновить")
        reload_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_BrowserReload))
        toolbar.addAction(reload_action)

        toolbar.addSeparator()
        # Выделить всё
        select_all_action = page.action(QWebEnginePage.WebAction.SelectAll)
        select_all_action.setText("Выделить всё")
        # Используем стандартную иконку (например, Edit)
        select_all_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_FileDialogDetailedView))
        toolbar.addAction(select_all_action)

        # Копировать (будет активно, только если выделен текст)
        copy_action = page.action(QWebEnginePage.WebAction.Copy)
        copy_action.setText("Копировать")
        copy_action.setIcon(
            self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogSaveButton))  # Или любая другая иконка
        toolbar.addAction(copy_action)
        # --- Кнопка Закрыть ---
        # Добавляем отступ, чтобы кнопка Закрыть была чуть в стороне от навигации
        spacer = QtWidgets.QWidget()
        spacer.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Preferred)
        toolbar.addWidget(spacer)  # Этот "распор" прижмет кнопку Закрыть вправо

        # Создаем само действие
        # noinspection PyUnresolvedReferences
        close_action = QtGui.QAction("Закрыть", self)
        close_action.setIcon(self.style().standardIcon(QtWidgets.QStyle.StandardPixmap.SP_DialogCloseButton))
        close_action.triggered.connect(self.close)  # Подключаем к закрытию окна
        toolbar.addAction(close_action)

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
