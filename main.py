import sqlite3
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt6 import uic


class MyWidget(QMainWindow):

    def __init__(self):
        super().__init__()
        
        uic.loadUi('main.ui', self)
        self.refreshBtn.clicked.connect(self.refresh)

        self.table.setRowCount(1)
        self.table.setColumnCount(7)

        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()

        self.refresh()

    def refresh(self):
        self.cursor.execute('SELECT * FROM coffee')
        coffees = self.cursor.fetchall()
        self.table.setRowCount(len(coffees))

        for coffee in coffees:
            self.table.setItem(coffees.index(coffee), 0, QTableWidgetItem(str(coffee[0])))
            self.table.setItem(coffees.index(coffee), 1, QTableWidgetItem(coffee[1]))
            self.table.setItem(coffees.index(coffee), 2, QTableWidgetItem(coffee[2]))
            self.table.setItem(coffees.index(coffee), 3, QTableWidgetItem(coffee[3]))
            self.table.setItem(coffees.index(coffee), 4, QTableWidgetItem(str(coffee[4])))
            self.table.setItem(coffees.index(coffee), 5, QTableWidgetItem(str(coffee[5])))
            self.table.setItem(coffees.index(coffee), 6, QTableWidgetItem(str(coffee[6])))
        


def create_db():
    DATA = [
        ("Эфиопия Йиргачеф", "Средняя", "В зернах", "Цветочные ноты, лёгкая кислинка, цитрус", 1200, 250),
        ("Колумбия Супремо", "Средняя", "Молотый", "Карамель, шоколад, умеренная кислинка", 950, 250),
        ("Гватемала Антигуа", "Тёмная", "В зернах", "Ореховые и шоколадные нотки, глубокий вкус", 1100, 500),
        ("Кения АА", "Светлая", "Молотый", "Ягодные и фруктовые ноты, приятная кислинка", 1300, 250),
        ("Бразилия Сантос", "Средняя", "В зернах", "Нежный ореховый вкус, лёгкая сладость", 850, 500),
        ("Индонезия Суматра", "Тёмная", "Молотый", "Землистый вкус с шоколадными оттенками", 1400, 250),
        ("Коста-Рика Тарразу", "Средняя", "В зернах", "Яркая кислинка, нотки цитрусовых и яблок", 1250, 250),
        ("Ямайка Блю Маунтин", "Светлая", "Молотый", "Бархатистый вкус с нотами орехов и меда", 3000, 250),
        ("Панама Гейша", "Светлая", "В зернах", "Фруктовые и цветочные ноты, лёгкий аромат", 4500, 250),
        ("Мексика Чиапас", "Средняя", "Молотый", "Нежный вкус с нотками шоколада и ванили", 1100, 250),
        ("Вьетнам Робуста", "Тёмная", "В зернах", "Насыщенный, крепкий вкус с горчинкой", 800, 500),
        ("Уганда Бугису", "Средняя", "Молотый", "Сладковатый вкус с нотами винограда и специй", 1150, 250),
        ("Никарагуа Марагоджип", "Средняя", "В зернах", "Глубокий вкус с карамельными и ореховыми нотками", 1250, 250),
        ("Танзания Пибери", "Светлая", "Молотый", "Яркие цитрусовые и ягодные нотки", 1350, 250),
        ("Перу Органик", "Средняя", "В зернах", "Чистый вкус с нотками миндаля и молочного шоколада", 1200, 500),
        ("Ямайка Хайлендс", "Тёмная", "Молотый", "Глубокий вкус с ароматом специй и какао", 3100, 250),
    ]

    conn = sqlite3.connect('coffee.sqlite')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS coffee (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   roast_level TEXT,
                   ground_or_beans TEXT,
                   taste_description TEXT,
                   price INTEGER,
                   package_volume INTEGER)''')
    conn.commit()

    for data in DATA:
        cursor.execute(f'INSERT INTO coffee (name, roast_level, ground_or_beans, taste_description, price, package_volume) VALUES (?, ?, ?, ?, ?, ?)', data)
    conn.commit()

    conn.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())