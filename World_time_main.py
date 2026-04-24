import sqlite3
from zoneinfo import ZoneInfo
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import QTableWidgetItem, QMessageBox, QAbstractItemView, QDialog
from PyQt6.QtCore import QResource, QTranslator, QLibraryInfo, QSettings, QDateTime, QRegularExpression, QTimeZone
import sys
from typing import Final
from pathlib import Path

from World_time import Ui_MainWindow
from World_time_add_dialog import Ui_DialogAdd
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from Qt6_palette import PaletteManager, APP_STYLE, dict_colors
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPalette, QColor
from datetime import datetime

city_regex = QRegularExpression(r"^(?=.*[a-zA-Zа-яА-ЯёЁ])[a-zA-Zа-яА-ЯёЁ0-9\s\.\-\,]+$")

ORGANIZATION_NAME: Final[str] = "isva_company"  # Имя организации разработчика для сохранения параметров в реестре
APPLICATION_NAME: Final[str] = "World_time_Application"  # Название приложения для сохранения параметров в реестре
DB_NAME: Final[str] = 'world_cities.db'

# В месте, где вы инициализируете менеджер палитр или окно:
error_palette_theme = {"Темная": {"Base": "#8B6A6A", "Text": "white"},
                       "Светлая": {"Base": "#FF9293", "Text": "#FFFFFF"},
                       "Зеленая": {"Base": "#708628", "Text": "#0f2414"},
                       "Голубая": {"Base": "#6A6AA6", "Text": "#0d1a26"},
                       "Пурпурная": {"Base": "#FF59FF", "Text": "#FFFFFF"},
                       "Розовая": {"Base": "#FF5689", "Text": "#FFFFFF"},
                       "Красная": {"Base": "#CC0000", "Text": "#FFFFFF"},
                       "Бирюзовая": {"Base": "#7FCECE", "Text": "#FFFFFF"},
                       "Янтарная": {"Base": "#CAAE6A", "Text": "#FFFFFF"},
                       "Голубая 2": {"Base": "#0000FF", "Text": "#FFFFFF"},
                       "Пастельная": {"Base": "#EA93FF", "Text": "#FFFFFF"},
                       "Арктическая, холодная": {"Base": "#20232E", "Text": "#FFFFFF"},
                       "Контрастная, фиолетово‑неоновая)": {"Base": "#BD93F9", "Text": "#FF79C6"},
                       "Solarized Dark - классическая «дизайнерская»": {"Base": "#268bd2", "Text": "#eee8d5"},
                       "Gruvbox - теплая, «крафтовая»": {"Base": "#fabd2f", "Text": "#282828"},
                       "One Dark - профессиональная темно-серая": {"Base": "#61afef", "Text": "#282c34"},
                       "Cyberpunk - экстремально контрастная": {"Base": "#ff0000", "Text": "#000000"},
                       "Бренд Ferrari": {"Base": "#ff2800", "Text": "#FFFFFF"},
                       "Бренд Moulinex": {"Base": "#da291c", "Text": "#FFFFFF"},
                       "Commodore 64 (Ретро)": {"Base": "#815096", "Text": "#ffffff"},
                       "IBM 3270 (Зеленый терминал)": {"Base": "#00FF00", "Text": "#000000"},
                       }


class MyPaletteManager(PaletteManager):
    def __init__(self, main_window, p_app, p_dict_themes, p_error_palette, palette_combo):
        super().__init__(main_window, p_app, p_dict_themes, palette_combo)
        self.error_palette = p_error_palette
        self.error_palette["standard"] = {"Base": "#8B6A6A", "Text": "#111111"}
        # self.error_palette["standard"] = {"Base": "#000000", "Text": "#000000"}

    def get_error_palette(self):
        if self.palette_combo.currentText() == "Системная ":
            palette_theme = "standard"
        else:
            palette_theme = self.palette_combo.currentText()

        palette = self.error_palette.get(palette_theme, self.error_palette["standard"])
        base_palette = palette.get("Base", self.error_palette["standard"]["Base"])
        text_palette = palette.get("Text", self.error_palette["standard"]["Text"])
        return base_palette, text_palette

def register_resources():
    rcc_path = Path(__file__).parent / "World_time.rcc"
    rcc_path_str = str(rcc_path)
    QResource.registerResource(rcc_path_str)


class AddDialog(QDialog, Ui_DialogAdd):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.db_connect = main_window.db_connect
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.window_section = "Add_Window"  # Секция параметров окна
        # Получаем геометрию, сразу указывая тип возвращаемого значения (QByteArray)
        self.save_geometry = self.settings.value(self.window_section + "/geometry")
        self.save_windowState = self.settings.value(self.window_section + "/windowState")
        self.find_cities_table_columns_state = None
        self.find_cities_table_columns_count = 0
        self.find_cities_table_columns_count_restored = 0
        # Проверяем, что данные не None и восстанавливаем
        if self.save_geometry is not None:
            self.restoreGeometry(self.save_geometry)
        validator = QRegularExpressionValidator(city_regex, self.city_edit)
        self.city_edit.setValidator(validator)
        self.find_button.clicked.connect(self.on_find_city)
        self.add_button.clicked.connect(self.on_add_city)
        self.find_cities_table.itemSelectionChanged.connect(self.on_selection_changed)
        self.add_button.setEnabled(False)
        # Редактирование начнется при двойном клике или нажатии F2
        self.find_cities_table.setEditTriggers(self.find_cities_table.EditTrigger.DoubleClicked |
                                               self.find_cities_table.EditTrigger.EditKeyPressed)
        self.find_cities_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.find_cities_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.find_cities_table.hideColumn(4)
        self.find_cities_table.hideColumn(5)
        self.restore_table_state()
        self.find_cities_table.itemDoubleClicked.connect(self.store_old_value)
        self.find_cities_table.itemChanged.connect(self.on_item_changed)

        self.old_city_full = ""
        self.city_root = ""
        self.find_city_operation = False

    def restore_table_state(self):
        self.find_cities_table_columns_count = self.find_cities_table.columnCount()
        self.find_cities_table_columns_count_restored = self.settings.value(
            self.window_section + "/find_cities_table_columns_count",
            0, type=int)
        self.find_cities_table_columns_state = self.settings.value(
            self.window_section + "/find_cities_table_columns_state")
        if self.find_cities_table_columns_count == self.find_cities_table_columns_count_restored:
            if self.find_cities_table_columns_state:
                self.find_cities_table.horizontalHeader().restoreState(self.find_cities_table_columns_state)

    def store_old_value(self, item):
        if item.column() == 0:
            full_text = item.text().strip()
            self.old_city_full = full_text
            # Берем часть до первой запятой и очищаем от пробелов
            self.city_root = full_text.split(',')[0].strip()

    def on_item_changed(self, item):
        # 1. Проверяем, что это нужный столбец
        if item.column() != 0:
            return
        new_name = item.text().strip()

        # --- БЛОК ВАЛИДАЦИИ ---
        match = city_regex.match(new_name)
        starts_correctly = new_name.lower().startswith(self.city_root.lower())
        item.tableWidget().blockSignals(True)
        row = item.tableWidget().currentRow()
        item_note: QTableWidgetItem = item.tableWidget().item(row, 3)
        item_note_text = ""
        if item_note:
            item_note_text = item_note.text().strip()
        if len(new_name) < 2 or not match.hasMatch() or not starts_correctly:
            # Если проверка НЕ прошла
            item.tableWidget().blockSignals(True)
            if not self.find_city_operation:
                QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверное название!")
                allow_change = False
                if not starts_correctly and len(new_name) >= 2 and match.hasMatch():
                    answer = self.message("Неверное название",
                                          f"Вы уверены, что хотите изменить название населенного пункта?",
                                          f"Внимание!!! Новое название: {new_name}")
                    if answer == QMessageBox.StandardButton.Yes:
                        allow_change = True
                if not allow_change:
                    item.setText(self.old_city_full)  # Откатываем к старому
                    item.tableWidget().blockSignals(False)
                    return  # ПРЕРЫВАЕМ выполнение, в базу ничего не пишем
        # --- БЛОК СОХРАНЕНИЯ (выполнится, только если валидация прошла) ---
        # Наверно надо удалить НАЧАЛО
        if item_note_text == "Неверное название!":
            item_note.setText("")
            self.add_button.setEnabled(True)
        # Наверно надо удалить Конец
        item.setText(new_name)  # Чистим пробелы
        item.tableWidget().blockSignals(False)

    def message(self, window_title, text, informative_text):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle(window_title)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        return msg.exec()

    def on_selection_changed(self):
        # Включаем кнопку только если есть выделенная строка
        enabled = False
        if len(self.find_cities_table.selectedItems()) > 0:
            row = self.find_cities_table.currentRow()
            if row != -1:
                note = self.find_cities_table.item(row, 3).text().strip()
                if not note:
                    enabled = True
        self.add_button.setEnabled(enabled)

    def on_find_city(self):
        city_query = self.city_edit.text().strip()
        region_query = self.reregion_edit.text().strip()
        if not self.city_edit.hasAcceptableInput():
            # Выводим ошибку пользователю
            QMessageBox.critical(self, 'Ошибка!', 'Название должно содержать буквы!')
            return

        # 2. Дополнительная "грубая" проверка на цифры
        if city_query.isdigit():
            QMessageBox.critical(self, 'Ошибка!', 'Введите название населенного пункта, а не индекс!')
            return

        # Если всё ок — идем в Nominatim

        if len(city_query) < 3:
            QMessageBox.critical(self, 'Ошибка!', 'Слишком короткое название!')
            return
        geolocator = Nominatim(user_agent="city_time_app_v4")
        locations = list()
        try:
            full_query = city_query
            if region_query:
                full_query = f"{city_query}, {region_query}"

            # Ищем только населенные пункты
            locations = geolocator.geocode(full_query, featuretype='settlement', language='ru', exactly_one=False,
                                           limit=60)
        except (Exception,):
            button_yes_no = QMessageBox.question(self, "Ошибка",
                                                 f"Ошибка, возможно нет доступа к интернету.\n Продолжить ввод?",
                                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                                 QMessageBox.StandardButton.No)
            if button_yes_no == QMessageBox.StandardButton.No:
                self.close()
                return
        if not locations:
            QMessageBox.critical(self, "Не найден.", f"Населенный пункт {city_query} не найден.")
            return
        self.find_cities_table.setRowCount(0)
        self.find_city_operation = True
        for loc in locations:
            osm_id = loc.raw.get('osm_id')
            osm_type = loc.raw.get('osm_type')
            row = self.find_cities_table.rowCount()
            self.find_cities_table.insertRow(row)

            # --- СТОЛБЕЦ 0: Название (ИЗМЕНЯЕМЫЙ) ---
            item_name = QtWidgets.QTableWidgetItem(loc.address)
            # Разрешаем: работу, выделение и РЕДАКТИРОВАНИЕ
            # noinspection PyTypeChecker
            item_name.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                               QtCore.Qt.ItemFlag.ItemIsSelectable |
                               QtCore.Qt.ItemFlag.ItemIsEditable)  # noinspection
            match = city_regex.match(loc.address)
            find_city = self.is_city_in_db(osm_id, osm_type)
            city_in_db = "Есть в БД" if find_city else \
                ("Неверное название!" if len(loc.address) < 2 or not match.hasMatch() else "")
            if find_city:
                item_name = QtWidgets.QTableWidgetItem(find_city)
            self.find_cities_table.setItem(row, 0, item_name)
            # --- ОСТАЛЬНЫЕ СТОЛБЦЫ (ТОЛЬКО ДЛЯ ЧТЕНИЯ) ---
            # Список данных для остальных ячеек

            other_data = [f"{loc.latitude:.6f}", f"{loc.longitude:.6f}", city_in_db, str(osm_id), osm_type]

            for i, value in enumerate(other_data, start=1):
                item = QtWidgets.QTableWidgetItem(value)
                # Разрешаем только работу и выделение (БЕЗ редактирования)
                # noinspection PyTypeChecker
                if i <= 2:
                    item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                          QtCore.Qt.AlignmentFlag.AlignVCenter)

                # noinspection PyTypeChecker
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                              QtCore.Qt.ItemFlag.ItemIsSelectable)
                self.find_cities_table.setItem(row, i, item)
        self.find_city_operation = False
        self.find_cities_table.setCurrentCell(0, 0)

    def is_city_in_db(self, osm_id, osm_type):
        cursor = self.db_connect.cursor()
        cursor.execute(
            "SELECT display_name FROM cities WHERE osm_id = ? AND osm_type = ? LIMIT 1",
            (osm_id, osm_type)
        )
        rows = cursor.fetchone()
        if rows:
            return rows[0]
        else:
            return None

    def on_add_city(self):
        row = self.find_cities_table.currentRow()
        if row != -1:
            display_name = self.find_cities_table.item(row, 0).text()
            latitude = float(self.find_cities_table.item(row, 1).text())
            longitude = float(self.find_cities_table.item(row, 2).text())
            osm_id = int(self.find_cities_table.item(row, 4).text())
            osm_type = self.find_cities_table.item(row, 5).text()
            tf = TimezoneFinder()
            tz_name = tf.timezone_at(lng=longitude, lat=latitude)
            cursor = self.db_connect.cursor()
            try:
                cursor.execute('''
                    INSERT INTO cities (display_name, latitude, longitude, timezone, osm_id, osm_type)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (display_name, latitude, longitude, tz_name, osm_id, osm_type))
                self.db_connect.commit()
                QMessageBox.information(self, "Добавление", f"Населенный пункт {display_name} добавлен.")
                self.find_cities_table.setItem(row, 3, QtWidgets.QTableWidgetItem("Добавлен в БД"))
                self.on_selection_changed()
            except sqlite3.Error as e:
                QMessageBox.critical(self, "Ошибка БД", f"Не удалось добавить: {e}")
                self.db_connect.rollback()  # Отменяет операцию, если что-то пошло не так

    def closeEvent(self, event):
        # Ваше действие при закрытии окна
        if self.save_geometry != self.saveGeometry():
            self.settings.setValue(self.window_section + "/geometry",
                                   self.saveGeometry())  # Сохранение размера окна
        self.save_table_state()
        # Если состояние окна изменилось, то сохраняем
        event.accept()  # Закрываем основное окно

    def save_table_state(self):
        # Получаем состояние горизонтального заголовка (ширина, порядок, видимость)
        state = self.find_cities_table.horizontalHeader().saveState()
        if self.find_cities_table_columns_state != state:
            self.settings.setValue(self.window_section + "/find_cities_table_columns_state", state)
        self.find_cities_table_columns_state = self.settings.value(
            self.window_section + "/find_cities_table_columns_state")
        if self.find_cities_table_columns_count != self.find_cities_table_columns_count_restored:
            self.settings.setValue(self.window_section + "/find_cities_table_columns_count",
                                   self.find_cities_table_columns_count)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):  # Создаем свой класс на базе класса Ui_MainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.target_combo = None
        self.settings = QSettings(ORGANIZATION_NAME, APPLICATION_NAME)
        self.window_section = "Main_Window"  # Секция параметров окна
        self.values_section = "Values"  # Секция параметров переменных
        self.find_cities_table_columns_state = None
        # Получаем геометрию, сразу указывая тип возвращаемого значения (QByteArray)
        self.save_geometry = self.settings.value(self.window_section + "/geometry")
        self.save_windowState = self.settings.value(self.window_section + "/windowState")

        # Проверяем, что данные не None и восстанавливаем
        if self.save_geometry is not None:
            self.restoreGeometry(self.save_geometry)
        if self.save_windowState is not None:
            self.restoreState(self.save_windowState)
        self.default_city = self.settings.value(self.values_section + "/default_city", "", type=str)
        self.default_sorted = self.settings.value(self.values_section + "/sorted", "Без сортировки", type=str)
        self.db_connect = sqlite3.connect(DB_NAME)
        # Регистрируем функцию в SQLite, чтобы она была доступна в SQL-запросах
        self.db_connect.create_function("GET_TZ_OFFSET", 2, self.sql_get_offset)
        self.init_db()
        # self.on_now()
        self.get_cities_for_combo()
        self.update_city_combos()
        # В __init__ вашего окна:
        self.now_button.clicked.connect(self.on_now)
        self.city_table.itemSelectionChanged.connect(self.on_selection_changed)
        self.calculation_datetime.dateTimeChanged.connect(self.refresh_main_table)
        self.delete_button.clicked.connect(self.delete_selected_city)
        self.add_button.clicked.connect(self.add_city)
        self.save_city_button.clicked.connect(self.on_save_city)
        self.save_palette_button.clicked.connect(self.on_save_palette)
        self.save_sorted_button.clicked.connect(self.on_save_sorted)
        self.set_default_sorted()
        self.city_combo.currentTextChanged.connect(self.on_now)
        # self.sort_combo.currentTextChanged.connect(self.on_now)
        self.sort_combo.currentTextChanged.connect(self.refresh_main_table)
        self.default_sity_button.clicked.connect(self.set_default_city)
        self.old_city_full = ""
        self.city_root = ""
        self.city_table_columns_state = None
        self.city_table_columns_count = 0
        self.city_table_columns_count_restored = 0
        self.city_table.itemChanged.connect(self.on_item_changed)
        self.city_table.setEditTriggers(self.city_table.EditTrigger.DoubleClicked |
                                        self.city_table.EditTrigger.EditKeyPressed)
        self.city_table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.city_table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.city_table.itemDoubleClicked.connect(self.store_old_value)
        # self.city_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        self.city_table.hideColumn(6)
        self.city_table.hideColumn(7)
        self.restore_table_state()

        # Подключаем сигнал изменения текста
        self.search_edit.textChanged.connect(self.apply_search_logic)

        # 2. Подключаем переключение радиокнопок для сброса состояния
        self.radio_filter.toggled.connect(self.change_search_logic)
        self.radio_search.toggled.connect(self.change_search_logic)

        self.manager = MyPaletteManager(self, app, dict_colors, error_palette_theme, self.palette_combo)
        self.palette_combo.currentTextChanged.connect(self.set_palette)
        self.palette_combo.setCurrentText(self.settings.value(self.values_section + "/palette", "Системная ", type=str))
        self.on_now()
        self.city_table.setFocus()

    @staticmethod
    def sql_get_offset(tz_name, timestamp):
        try:
            dt = datetime.fromtimestamp(timestamp, tz=ZoneInfo("UTC"))
            offset_td = ZoneInfo(tz_name).utcoffset(dt)
            if offset_td is not None:
                offset = offset_td.total_seconds()
            else:
                offset = 0  # Или другое значение по умолчанию
            return offset / 3600
        except (Exception,):
            return 0

    def change_search_logic(self):
        self.reset_table_visibility()
        self.apply_search_logic()

    def restore_table_state(self):
        self.city_table_columns_count = self.city_table.columnCount()
        self.city_table_columns_count_restored = self.settings.value(self.window_section + "/city_table_columns_count",
                                                                     0, type=int)
        self.city_table_columns_state = self.settings.value(self.window_section + "/city_table_columns_state")
        if self.city_table_columns_count == self.city_table_columns_count_restored:
            if self.city_table_columns_state:
                self.city_table.horizontalHeader().restoreState(self.city_table_columns_state)

    def set_palette(self):
        self.manager.set_palette()
        self.apply_search_logic()
        row = self.city_table.currentRow()
        if row >= 0:
            self.city_table.selectRow(row)

    def reset_table_visibility(self):
        """Сбрасывает скрытие строк и подготавливает таблицу к новому режиму."""
        for row in range(self.city_table.rowCount()):
            self.city_table.setRowHidden(row, False)
        if self.city_table.rowCount() > 0:
            self.delete_button.setEnabled(True)
            row = self.city_table.currentRow()
            if row >= 0:
                self.city_table.selectRow(row)

    def apply_search_logic(self):
        search_text = self.search_edit.text().strip().lower()
        self.manager.get_error_palette()

        # Стили для поля ввода
        current_palette = self.palette()
        error_palette = self.palette()
        base_palette, text_palette = self.manager.get_error_palette()
        error_palette.setColor(QPalette.ColorRole.Base, QColor(base_palette))
        error_palette.setColor(QPalette.ColorRole.Text, QColor(text_palette))

        # Если поле пустое — сбрасываем всё
        if not search_text:
            self.reset_table_visibility()
            # Сбрасываем к актуальной теме менеджера, а не к системному дефолту
            self.search_edit.setPalette(current_palette)
            if self.radio_search.isChecked():
                self.city_table.clearSelection()
            if self.city_table.rowCount() > 0:
                # Выделяем первую строку программно
                self.city_table.selectRow(0)
            return

        found_any = False
        first_visible_row = -1  # Переменная для хранения первой найденной строки

        if self.radio_filter.isChecked():
            # --- РЕЖИМ ФИЛЬТРАЦИИ ---
            for row in range(self.city_table.rowCount()):
                item = self.city_table.item(row, 0)
                if item:
                    is_match = item.text().lower().startswith(search_text)
                    self.city_table.setRowHidden(row, not is_match)
                    if is_match:
                        found_any = True
                        if first_visible_row == -1:
                            first_visible_row = row

            # «ФИШКА»: Если что-то нашли, делаем эту строку текущей
            if first_visible_row != -1:
                self.city_table.blockSignals(True)
                self.city_table.selectRow(first_visible_row)
                self.city_table.blockSignals(False)
            else:
                self.city_table.clearSelection()

        elif self.radio_search.isChecked():
            # --- РЕЖИМ ПОИСКА (ПЕРЕХОДА) ---
            for row in range(self.city_table.rowCount()):
                item = self.city_table.item(row, 0)
                if item and item.text().lower().startswith(search_text):
                    self.city_table.blockSignals(True)
                    self.city_table.selectRow(row)
                    self.city_table.scrollToItem(item, QAbstractItemView.ScrollHint.PositionAtTop)
                    self.city_table.blockSignals(False)
                    found_any = True
                    break

            if not found_any:
                self.city_table.clearSelection()
        # Устанавливаем цвет фона в зависимости от результата
        if found_any:
            # Возвращаем цвета текущей темы
            self.search_edit.setPalette(current_palette)
            self.delete_button.setEnabled(True)
        else:
            # Создаем копию текущей палитры темы и меняем ТУТ только фон
            self.search_edit.setPalette(error_palette)
            self.delete_button.setEnabled(False)

        # «ФИШКА»: Возвращаем фокус, чтобы можно было стирать/исправлять
        # self.search_edit.setFocus()

    def store_old_value(self, item):
        if item.column() == 0:
            full_text = item.text().strip()
            self.old_city_full = full_text
            # Берем часть до первой запятой и очищаем от пробелов
            self.city_root = full_text.split(',')[0].strip()

    def on_item_changed(self, item):
        # 1. Проверяем, что это нужный столбец
        if item.column() != 0:
            return

        new_name = item.text().strip()

        # --- БЛОК ВАЛИДАЦИИ ---
        match = city_regex.match(new_name)
        starts_correctly = new_name.lower().startswith(self.city_root.lower())
        # Если проверка НЕ прошла
        allow_change = False
        if len(new_name) < 2 or not match.hasMatch() or not starts_correctly:
            # Если проверка НЕ прошла
            item.tableWidget().blockSignals(True)
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверное название!")
            if not starts_correctly and len(new_name) >= 2 and match.hasMatch():
                answer = self.message("Неверное название",
                                      f"Вы уверены, что хотите изменить название населенного пункта?",
                                      f"Внимание!!! Новое название: {new_name}")
                if answer == QMessageBox.StandardButton.Yes:
                    allow_change = True
            if not allow_change:
                item.setText(self.old_city_full)  # Откатываем к старому
                item.tableWidget().blockSignals(False)
                return  # ПРЕРЫВАЕМ выполнение, в базу ничего не пишем

        # --- БЛОК СОХРАНЕНИЯ (выполнится, только если валидация прошла) ---
        item.tableWidget().blockSignals(True)
        item.setText(new_name)  # Чистим пробелы
        item.tableWidget().blockSignals(False)

        row = item.row()
        try:
            # Достаем ID из скрытых колонок (6 и 7)
            osm_id = int(self.city_table.item(row, 6).text())
            osm_type = self.city_table.item(row, 7).text()

            # Теперь вызываем запись в SQLite
            self.update_city_name_in_db(osm_id, osm_type, new_name)

            # И обновляем комбобоксы
            QtCore.QTimer.singleShot(0, self.update_city_combos)

        except AttributeError:
            pass

    def update_city_name_in_db(self, osm_id, osm_type, new_name):
        query = "UPDATE cities SET display_name = ? WHERE osm_id = ? AND osm_type = ?"
        self.db_connect.execute(query, (new_name, osm_id, osm_type))
        self.db_connect.commit()

    def on_save_city(self):
        if self.default_city != self.city_combo.currentText():
            self.default_city = self.city_combo.currentText()
            self.settings.setValue(self.values_section + "/default_city", self.default_city)

    def on_save_sorted(self):
        if self.default_sorted != self.sort_combo.currentText():
            self.default_sorted = self.sort_combo.currentText()
            self.settings.setValue(self.values_section + "/sorted", self.default_sorted)

    def on_save_palette(self):
        self.settings.setValue(self.values_section + "/palette", self.palette_combo.currentText())

    def add_city(self):
        dialog = AddDialog(self)
        dialog.exec()
        self.update_city_combos()
        self.refresh_main_table()

    def set_default_sorted(self):
        index = self.sort_combo.findText(self.default_sorted)
        if index != -1:
            self.sort_combo.setCurrentIndex(index)
        else:
            if self.sort_combo.count() > 0:
                self.sort_combo.setCurrentIndex(0)

    def set_default_city(self):
        index = self.city_combo.findText(self.default_city)
        if index != -1:
            self.city_combo.setCurrentIndex(index)
        else:
            if self.city_combo.count() > 0:
                self.city_combo.setCurrentIndex(0)

    def delete_selected_city(self):
        # 1. Получаем индекс текущей выбранной строки
        current_row = self.city_table.currentRow()

        # Защитная проверка (если кнопка вдруг была активна, но строка не выбрана)
        if current_row == -1:
            return

        # 2. Извлекаем данные из скрытых колонок (6 и 7)
        # Данные в QTableWidgetItem всегда хранятся как текст, поэтому osm_id преобразуем в int
        try:
            osm_id = int(self.city_table.item(current_row, 6).text())
            osm_type = self.city_table.item(current_row, 7).text()
            city_name = self.city_table.item(current_row, 0).text()  # Название для вопроса
        except (AttributeError, ValueError):
            return

        # Кнопки в PyQt6 возвращают объект StandardButton
        answer = self.message("Подтверждение удаления",
                              f"Вы уверены, что хотите удалить населенный пункт из базы?",
                              f"Населенный пункт: {city_name}")

        if answer == QMessageBox.StandardButton.Yes:
            # 4. Вызываем ваш метод работы с БД
            try:
                self.db_delete_logic(osm_id, osm_type)

                # 5. Обновляем UI: удаляем строку из таблицы и обновляем комбобоксы
                self.city_table.removeRow(current_row)
                self.update_city_combos()  # Чтобы город исчез из списков выбора

                # Если таблица опустела, блокируем кнопку программно
                if self.city_table.rowCount() == 0:
                    self.set_enabled_widget(False)
                self.city_table.setFocus()
            except Exception as e:
                QMessageBox.critical(self, "Ошибка БД", f"Не удалось удалить: {e}")

    def message(self, window_title, text, informative_text):
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Question)
        msg.setWindowTitle(window_title)
        msg.setText(text)
        msg.setInformativeText(informative_text)
        msg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        msg.setDefaultButton(QMessageBox.StandardButton.No)
        return msg.exec()

    def db_delete_logic(self, osm_id, osm_type):
        try:
            self.db_connect.execute("DELETE FROM cities WHERE osm_id = ? AND osm_type = ?",
                                    (osm_id, osm_type))
            self.db_connect.commit()
            return True
        except sqlite3.Error as e:
            # Здесь можно вывести сообщение в статус-бар или лог
            QMessageBox.critical(self, "Ошибка БД", f"Не удалось удалить: {e}")
            self.db_connect.rollback()  # Отменяет операцию, если что-то пошло не так
            return False

    def on_selection_changed(self):
        # Включаем кнопку только если есть выделенная строка
        is_selected = len(self.city_table.selectedItems()) > 0
        self.delete_button.setEnabled(is_selected)
        # self.set_enabled_widget(is_selected)

    def get_time_data(self, source_tz_name, input_dt, source_city, longitude):
        cursor = self.db_connect.cursor()
        """
        Получает все города из БД и рассчитывает время/разницу
        относительно исходного города и даты.
        """
        results_for_table = []

        # Создаем объект времени в исходном часовом поясе
        try:
            src_tz = ZoneInfo(source_tz_name)
            # Если input_dt пришел из QDateTime.toPython(), он naive. Привязываем:
            src_dt = input_dt.replace(tzinfo=src_tz)
            ts = src_dt.timestamp()

        except (Exception,):
            QMessageBox.critical(self, 'Ошибка!', f'Ошибка часового пояса {source_tz_name} для {source_city}!')
            return None
        sort_mode = self.sort_combo.currentText()
        if sort_mode == "По названию":
            # Сортируем по названию
            order_clause = "ORDER BY display_name ASC"
            params = ()
        elif sort_mode == "По разности времени":
            # Считаем смещение исходного города
            src_offset = src_dt.utcoffset().total_seconds() / 3600
            # Сортируем по разнице оффсетов, а внутри одного пояса — по долготе
            order_clause = "ORDER BY abs(? - GET_TZ_OFFSET(timezone, ?)) ASC, abs(? - longitude) ASC"
            params = (src_offset, ts, longitude)
        elif sort_mode == "По относительной долготе":
            # Сортируем по долготе
            order_clause = "ORDER BY abs(? - longitude) ASC"
            params = (longitude,)
        else:
            # Без сортировки
            order_clause = ""
            params = ()

        query = f"SELECT display_name, latitude, longitude, timezone, osm_id, osm_type FROM cities {order_clause}"
        cursor.execute(query, params)
        rows = cursor.fetchall()

        for display_name, lat, lon, timezone, osm_id, osm_type in rows:
            try:
                target_tz = ZoneInfo(timezone)
                target_dt = src_dt.astimezone(target_tz)

                # Расчет разницы в часах и минутах
                diff_sec = target_dt.utcoffset().total_seconds() - src_dt.utcoffset().total_seconds()
                diff_str = self.get_difference(diff_sec)
                # Формируем строку для QTableWidget
                results_for_table.append({
                    'display_name': display_name,
                    'lat': lat,
                    'lon': lon,
                    'timezone': timezone,
                    'osm_id': osm_id,
                    'osm_type': osm_type,
                    'local_time': target_dt.strftime('%d.%m.%Y %H:%M'),
                    'difference': diff_str
                })
            except (Exception,):
                QMessageBox.critical(self, 'Ошибка!', f'Ошибка часового пояса {timezone} для {display_name}!')
        return results_for_table

    @staticmethod
    def get_difference(diff_sec):
        if diff_sec == 0:
            diff_str = "совпадает с местным временем"
        else:
            h, m = divmod(abs(int(diff_sec)), 3600)
            m //= 60
            diff_str = ""
            if h > 0:
                diff_str += f"{h} ч."
            if m > 0:
                diff_str += f"{m} мин."
            if diff_sec < 0:
                diff_str += " раньше"
            else:
                diff_str += " позже"
            diff_str = "на " + diff_str
        return diff_str

    def refresh_main_table(self):

        source_tz, source_longitude = self.city_combo.currentData().split("~")

        # Берем скрытое значение (timezone)
        input_dt = self.calculation_datetime.dateTime().toPyDateTime()  # Конвертируем в Python datetime

        if not source_tz:
            self.edit_delete_button_state()
            return

        # 2. Получаем список словарей из нашего метода логики
        cities_data = self.get_time_data(source_tz, input_dt, self.city_combo.currentText(), float(source_longitude))

        # 3. Очищаем таблицу перед заполнением
        self.city_table.setRowCount(0)

        # 4. Заполняем таблицу строками
        if cities_data is not None:
            self.city_table.blockSignals(True)
            for row_idx, city in enumerate(cities_data):
                self.city_table.insertRow(row_idx)

                name_item = QTableWidgetItem(city['display_name'])
                # Устанавливаем флаги: стандартные + возможность редактирования
                # noinspection PyTypeChecker
                name_item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                                   QtCore.Qt.ItemFlag.ItemIsSelectable |
                                   QtCore.Qt.ItemFlag.ItemIsEditable)  # noinspection
                self.city_table.setItem(row_idx, 0, name_item)
                # Видимые данные
                other_data = [f"{city['lat']:.6f}", f"{city['lon']:.6f}", city['timezone'], city['local_time'],
                              city['difference'], str(city['osm_id']), city['osm_type']]

                for i, value in enumerate(other_data, start=1):
                    item = QtWidgets.QTableWidgetItem(value)

                    # Условие для первых двух колонок (так как start=1, это i=1 и i=2)
                    if i <= 2:
                        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignRight |
                                              QtCore.Qt.AlignmentFlag.AlignVCenter)

                    # Ваши флаги
                    # noinspection PyTypeChecker
                    item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled |
                                  QtCore.Qt.ItemFlag.ItemIsSelectable)

                    self.city_table.setItem(row_idx, i, item)

            self.city_table.blockSignals(False)
        if self.city_table.rowCount() > 0:
            # Выделяем первую строку программно
            self.city_table.selectRow(0)
        self.edit_delete_button_state()
        self.apply_search_logic()

    def edit_delete_button_state(self):
        # Блокируем, если строк 0, разблокируем, если > 0
        has_rows = self.city_table.rowCount() > 0
        self.set_enabled_widget(has_rows)

    def set_enabled_widget(self, enable):
        self.delete_button.setEnabled(enable)
        self.search_edit.setEnabled(enable)
        self.radio_filter.setEnabled(enable)
        self.radio_search.setEnabled(enable)

    # Вызывайте это в конце refresh_main_table() и delete_selected_city()

    def update_city_combos(self):
        self.city_combo.blockSignals(True)  # Временно выключаем сигналы комбобокса
        self.city_combo.clear()
        for name, tz, longitude in self.get_cities_for_combo():
            self.city_combo.addItem(name, tz + "~" + str(longitude))
        self.set_default_city()
        self.city_combo.blockSignals(False)  # Включаем обратно

    def get_cities_for_combo(self):
        """
        Возвращает список кортежей (display_name, timezone)
        из БД для загрузки в QComboBox.
        """
        cursor = self.db_connect.cursor()
        # Получаем названия и зоны, сортируем по алфавиту
        cursor.execute("SELECT display_name, timezone, longitude FROM cities ORDER BY display_name ASC")
        return cursor.fetchall()

    def on_now(self):
        if self.city_combo.count() > 0:
            source_tz_str = self.city_combo.currentData().split("~")[0]

            if source_tz_str:
                # 1. Создаем объект часового пояса
                tz = QTimeZone(source_tz_str.encode())

                if tz.isValid():
                    # 2. СНАЧАЛА устанавливаем часовой пояс в сам виджет
                    # Это автоматически установит TimeSpec в Qt.TimeSpec.TimeZone
                    self.calculation_datetime.setTimeZone(tz)

                    # 3. Получаем текущее время в UTC и конвертируем в этот пояс
                    current_time_in_tz = QDateTime.currentDateTimeUtc().toTimeZone(tz)

                    # 4. Передаем готовый объект времени в виджет
                    self.calculation_datetime.setDateTime(current_time_in_tz)

                    # print(f"Установлен пояс: {source_tz_str}, Время: {current_time_in_tz.toString()}")

    def init_db(self):
        cursor = self.db_connect.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS cities (
                osm_id INTEGER,
                osm_type TEXT,
                display_name TEXT,  -- Название населенного пункта (изменяемое)
                latitude REAL,
                longitude REAL,
                timezone TEXT NOT NULL,
                PRIMARY KEY (osm_id, osm_type)
            )
        ''')
        self.db_connect.commit()

    def closeEvent(self, event):
        # Ваше действие при закрытии окна
        if self.save_geometry != self.saveGeometry():
            self.settings.setValue(self.window_section + "/geometry",
                                   self.saveGeometry())  # Сохранение размера окна
        # Если состояние окна изменилось, то сохраняем
        if self.save_windowState != self.saveState():
            self.settings.setValue(self.window_section + "/windowState",
                                   self.saveState())  # Сохранение состояния окна
        self.save_table_state()
        if hasattr(self, 'db_connect'):
            self.db_connect.close()
        event.accept()  # Закрываем основное окно

    def save_table_state(self):
        # Получаем состояние горизонтального заголовка (ширина, порядок, видимость)
        state = self.city_table.horizontalHeader().saveState()
        if self.city_table_columns_state != state:
            self.settings.setValue(self.window_section + "/city_table_columns_state", state)
        self.city_table_columns_state = self.settings.value(self.window_section + "/city_table_columns_state")
        if self.city_table_columns_count != self.city_table_columns_count_restored:
            self.settings.setValue(self.window_section + "/city_table_columns_count", self.city_table_columns_count)


if __name__ == "__main__":
    register_resources()
    app = QApplication(sys.argv)
    app.setStyle(APP_STYLE)
    # Создаём переводчик
    qt_translator = QTranslator()
    qt_translator.load(
        "qtbase_ru",
        QLibraryInfo.path(QLibraryInfo.LibraryPath.TranslationsPath)
    )
    app.installTranslator(qt_translator)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
