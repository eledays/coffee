import sqlite3
import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt6 import uic


class Databaser:

    def __init__(self):
        self.conn = sqlite3.connect('coffee.sqlite')
        self.cursor = self.conn.cursor()

    def create_table(self):
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

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS coffee (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    roast_level TEXT,
                    ground_or_beans TEXT,
                    taste_description TEXT,
                    price INTEGER,
                    package_volume INTEGER)''')
        self.conn.commit()

        for data in DATA:
            self.cursor.execute(f'INSERT INTO coffee (name, roast_level, ground_or_beans, taste_description, price, package_volume) VALUES (?, ?, ?, ?, ?, ?)', data)
        self.conn.commit()

    def get_all(self):
        self.cursor.execute('SELECT * FROM coffee')
        return self.cursor.fetchall()
    
    def get_names(self):
        self.cursor.execute('SELECT name FROM coffee')
        return [e[0] for e in self.cursor.fetchall()]
    
    def get_max_id(self):
        self.cursor.execute('SELECT MAX(id) FROM coffee')
        return self.cursor.fetchone()[0]
    
    def get_by_name(self, name):
        self.cursor.execute('SELECT * FROM coffee WHERE name = ?', (name,))
        return self.cursor.fetchone()
    
    def add(self, name, roast_level, ground_or_beans, taste_description, price, package_volume):
        self.cursor.execute(f'''INSERT INTO coffee (name, roast_level, ground_or_beans, taste_description, price, package_volume) 
                            VALUES (?, ?, ?, ?, ?, ?)''', 
                            (name, roast_level, ground_or_beans, taste_description, price, package_volume))
        self.conn.commit()
    
    def update(self, id, name, roast_level, ground_or_beans, taste_description, price, package_volume):
        self.cursor.execute(f'''UPDATE coffee SET 
                            name=?, roast_level=?, ground_or_beans=?, 
                            taste_description=?, price=?, package_volume=? 
                            WHERE id=?''', 
                            (name, roast_level, ground_or_beans, taste_description, price, package_volume, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()


class MyWidget(QMainWindow):

    def __init__(self, db):
        super().__init__()

        self.db = db
        
        uic.loadUi('main.ui', self)
        self.refreshBtn.clicked.connect(self.refresh)
        self.editBtn.clicked.connect(self.edit)

        self.table.setRowCount(1)
        self.table.setColumnCount(7)

        self.refresh()

    def refresh(self):
        coffees = self.db.get_all()
        self.table.setRowCount(len(coffees))

        for coffee in coffees:
            self.table.setItem(coffees.index(coffee), 0, QTableWidgetItem(str(coffee[0])))
            self.table.setItem(coffees.index(coffee), 1, QTableWidgetItem(coffee[1]))
            self.table.setItem(coffees.index(coffee), 2, QTableWidgetItem(coffee[2]))
            self.table.setItem(coffees.index(coffee), 3, QTableWidgetItem(coffee[3]))
            self.table.setItem(coffees.index(coffee), 4, QTableWidgetItem(str(coffee[4])))
            self.table.setItem(coffees.index(coffee), 5, QTableWidgetItem(str(coffee[5])))
            self.table.setItem(coffees.index(coffee), 6, QTableWidgetItem(str(coffee[6])))
    
    def edit(self):
        self.second_window = SecondWidget(db)
        self.second_window.show()


class SecondWidget(QMainWindow):

    def __init__(self, db):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)

        self.db = db
        
        self.editBtn.toggled.connect(self.editMode)
        self.addBtn.toggled.connect(self.addMode)
        self.editComboBox.currentTextChanged.connect(self.updateEditComboBox)
        self.finishButton.clicked.connect(self.finish)

        names = self.db.get_names()
        self.editComboBox.addItems(names)

        self.idLine.setText(str(self.db.get_max_id() + 1))

    def editMode(self):
        self.editComboBox.setEnabled(True)
        self.updateEditComboBox()
        
    def addMode(self):
        self.editComboBox.setEnabled(False)

        self.idLine.setText(str(self.db.get_max_id() + 1))
        self.nameLine.clear()
        self.roastLine.clear()
        self.groundOrBeansComboBox.setCurrentIndex(0)
        self.tasteLine.clear()
        self.priceLine.clear()
        self.packageVolumeLine.clear()

    def updateEditComboBox(self):
        if not self.editBtn.isChecked():
            return

        id, name, roast_level, ground_or_beans, taste, price, package_volume = \
        self.db.get_by_name(self.editComboBox.currentText())

        self.idLine.setText(str(id))
        self.nameLine.setText(name)
        self.roastLine.setText(roast_level)
        self.groundOrBeansComboBox.setCurrentIndex(int(ground_or_beans == 'В зернах'))
        self.tasteLine.setText(taste)
        self.priceLine.setText(str(price))
        self.packageVolumeLine.setText(str(package_volume))

    def finish(self):
        if int(self.idLine.text()) == self.db.get_max_id() + 1:
            self.db.add(self.nameLine.text(), self.roastLine.text(),\
                        self.groundOrBeansComboBox.currentText(), self.tasteLine.toPlainText(),\
                        int(self.priceLine.text()), int(self.packageVolumeLine.text()))
        else:
            self.db.update(int(self.idLine.text()), self.nameLine.text(), self.roastLine.text(),\
                        self.groundOrBeansComboBox.currentText(), self.tasteLine.toPlainText(),\
                        int(self.priceLine.text()), int(self.packageVolumeLine.text()))
        self.close()


if __name__ == '__main__':
    db = Databaser()
    app = QApplication(sys.argv)
    ex = MyWidget(db)
    ex.show()
    sys.exit(app.exec())