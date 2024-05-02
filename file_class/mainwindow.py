from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QMessageBox, QFileDialog
from PySide6.QtCore import Signal, Slot, QObject
from file_class.window01_ui import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from file_class.datafile import DataFile
from file_class.memorymanagement import MemoryManagement


class MainWindow(QMainWindow):
    update_gui = Signal(list) 
    
    def __init__(self) -> None:
        super().__init__()
        
        # Configurar la interfaz de usuario
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.data = DataFile()
        self.memoryManagement = MemoryManagement(7500, [1000, 1400, 3200, 3900, 4800, 6000, 7500], ["1000kb", "400kb", "1800kb", "700kb", "900kb", "1200kb", "1500kb"])
        
        #layout
        self.layout = QVBoxLayout(self.ui.w_memory)
        
        self.ui.cb_seleccionar_algoritmo.addItem("Seleccione Uno")
        self.ui.cb_seleccionar_algoritmo.addItem("Primer Ajuste")
        self.ui.cb_seleccionar_algoritmo.addItem("Mejor Ajuste")
        
        self.ui.b_cargar_datos.clicked.connect(self.action_openFile)
        self.ui.b_ejecutar.clicked.connect(self.action_ejecutarAlgoritmo)
        self.ui.b_reestablecer.clicked.connect(self.action_reestablecer)
        
        self.showGrafic(self.memoryManagement.getMemoryStructure())
        
        
        
    
    def showGrafic(self, canvas):
        # Primero, verifica si el layout ya tiene widgets y elimínalos
        if self.layout.count() > 0:
            # Elimina todos los widgets del layout
            while self.layout.count():
                item = self.layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
        
        # Ahora, agrega el nuevo FigureCanvas al layout
        self.layout.addWidget(canvas)
    
    @Slot( )
    def action_reestablecer(self):
        self.memoryManagement.memoryReset(7500, [1000, 1400, 3200, 3900, 4800, 6000, 7500], ["1000kb", "400kb", "1800kb", "700kb", "900kb", "1200kb", "1500kb"])
        self.showGrafic(self.memoryManagement.getMemoryStructure())
    
    @Slot( )
    def action_openFile(self):
        mensaje1 = QMessageBox(self)
        mensaje1.setWindowTitle("Alerta.")
        mensaje1.setText("El archivo no se pudo abrir correctamente")
        mensaje1.setStandardButtons(QMessageBox.Ok)
        mensaje1.setDefaultButton(QMessageBox.Ok)
        mensaje1.setIcon(QMessageBox.Critical)
        
        mensaje2 = QMessageBox(self)
        mensaje2.setWindowTitle("Notificacion.")
        mensaje2.setText("Archivo cargado exitosamente")
        mensaje2.setStandardButtons(QMessageBox.Ok)
        mensaje2.setDefaultButton(QMessageBox.Ok)
        mensaje2.setIcon(QMessageBox.Information)
        
        path = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'TXT (*.txt)'
        )[0]
        
        if self.data.open(path):            
            for line in self.data.dataText:
                self.ui.pt_editar_texto.appendPlainText(line)
        else: 
            mensaje1.exec_()

    @Slot( )
    def action_ejecutarAlgoritmo(self):
        data = self.ui.pt_editar_texto.toPlainText()
        lines = data.splitlines()
        algoritmoSeleccionado = self.ui.cb_seleccionar_algoritmo.currentText()
        
        values = []
        label = []
        
        for line in lines:
                parts = line.split(",")
                parts[1] = parts[1].strip().rstrip('kb')
                parts[1] = int(parts[1])
                
                values.append(parts[1])
                label.append(parts[0])
        
        if(algoritmoSeleccionado == "Primer Ajuste"):
            self.memoryManagement.firstFitAlgorithm(values, label)
            
        elif(algoritmoSeleccionado == "Mejor Ajuste"):
            self.memoryManagement.bestFitAlgorithm(values, label)
        
        self.showGrafic(self.memoryManagement.getMemoryStructure())