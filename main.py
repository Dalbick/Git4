import sys
import sqlite3
from PyQt5 import QtWidgets, uic


class Coffee(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        con = sqlite3.connect('coffee.sqlite')
        cur = con.cursor()
        arr = cur.execute('select * from coffee').fetchall()
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(len(arr))
        self.tableWidget.setHorizontalHeaderLabels(['id', 'название сорта', 'степень обжарки',
                                                    'молотый/в зернах', 'описание вкуса',
                                                    'цена(тг)', 'объем упаковки'])
        for i in range(len(arr)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(arr[i][j])))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    coffee = Coffee()
    coffee.show()
    sys.exit(app.exec())
