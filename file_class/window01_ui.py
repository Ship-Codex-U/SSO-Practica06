# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window01.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1061, 555)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.w_memory = QWidget(self.centralwidget)
        self.w_memory.setObjectName(u"w_memory")
        self.w_memory.setGeometry(QRect(20, 210, 1021, 271))
        self.cb_seleccionar_algoritmo = QComboBox(self.centralwidget)
        self.cb_seleccionar_algoritmo.setObjectName(u"cb_seleccionar_algoritmo")
        self.cb_seleccionar_algoritmo.setGeometry(QRect(750, 90, 231, 21))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(600, 90, 141, 20))
        self.b_ejecutar = QPushButton(self.centralwidget)
        self.b_ejecutar.setObjectName(u"b_ejecutar")
        self.b_ejecutar.setGeometry(QRect(750, 140, 231, 20))
        self.b_cargar_datos = QPushButton(self.centralwidget)
        self.b_cargar_datos.setObjectName(u"b_cargar_datos")
        self.b_cargar_datos.setGeometry(QRect(20, 10, 121, 24))
        self.pt_editar_texto = QPlainTextEdit(self.centralwidget)
        self.pt_editar_texto.setObjectName(u"pt_editar_texto")
        self.pt_editar_texto.setEnabled(True)
        self.pt_editar_texto.setGeometry(QRect(20, 50, 351, 131))
        self.b_reestablecer = QPushButton(self.centralwidget)
        self.b_reestablecer.setObjectName(u"b_reestablecer")
        self.b_reestablecer.setGeometry(QRect(750, 170, 231, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1061, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Selecciona el algoritmo:", None))
        self.b_ejecutar.setText(QCoreApplication.translate("MainWindow", u"Ejecutar", None))
        self.b_cargar_datos.setText(QCoreApplication.translate("MainWindow", u"Cargar Archivo", None))
        self.b_reestablecer.setText(QCoreApplication.translate("MainWindow", u"Reestablecer Memoria", None))
    # retranslateUi

