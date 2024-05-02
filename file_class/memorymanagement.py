from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

class MemoryManagement:
    def __init__(self, size, values, textLabel) -> None:
        self.__size = size
        self.__values = values
        self.__textLabel = textLabel
        self.__newDataModification = False
        self.__sizeNewData = []
        self.__pointStart = []
        
        self.__available = []
        for i in range(len(self.__values)):
            self.__available.append(True)
    
    def memoryReset(self, size, values, textLabel):
        self.__size = size
        self.__values = values
        self.__textLabel = textLabel
        self.__newDataModification = False
        self.__sizeNewData = []
        self.__pointStart = []
        
        self.__available = []
        for i in range(len(self.__values)):
            self.__available.append(True)
        
    
    def getMemoryStructure(self):
        # Limpia la figura actual antes de crear una nueva gráfica
        plt.clf()   
        # Crear una gráfica de barras con un solo valor
        data = [self.__size]  # Valor único para la barra
        labels = ['Memoria']  # Etiqueta para la barra
        
        # Crear un gráfico de barras horizontal con color verde
        plt.barh(labels, data, color='forestgreen')

        # Agregar líneas verticales en los puntos de corte especificados
        cortes = self.__values
        
        for corte in cortes:
            plt.axvline(x=corte, color='black', linestyle='--', linewidth=2)
        
        if self.__newDataModification:
            for value, start in zip(self.__sizeNewData, self.__pointStart):
                plt.barh(labels, value, left=start, color='red')

        # Agregar etiquetas a los cortes
        # Inicializa el bucle desde el primer corte (índice 0)
        for i in range(len(cortes)):
            if i == 0:
                # La primera iteración se maneja para agregar la etiqueta con el valor de 1000
                centro = cortes[i] / 2  # Centro desde el inicio hasta el primer corte
                plt.text(centro, 0, str(self.__textLabel[0]), rotation=90, ha='center', va='center', fontsize=10, color='white', bbox=dict(facecolor='none', alpha=0, edgecolor='none'))
            else:
                # Las iteraciones subsiguientes calculan el centro y la diferencia de cada sección
                centro = (cortes[i - 1] + cortes[i]) / 2
                plt.text(centro, 0, str(self.__textLabel[i]), rotation=90, ha='center', va='center', fontsize=10, color='white', bbox=dict(facecolor='none', alpha=0, edgecolor='none'))

        self.__newDataModification = False
        
        # Mostrar la gráfica en el widget QGraphicsView
        return FigureCanvas(plt.gcf())
    
    def firstFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            pos = 0
            flag = True
            while flag:
                if(pos < len(self.__values)):
                    if pos == 0:
                        if(self.__available[0] == True and value <= self.__values[pos]):
                            self.__values.insert(0, value)
                            self.__textLabel.insert(0, label)
                            
                            newValor = self.__values[pos + 1] - value
                            newLabel = str(newValor) + 'kb'                        
                            self.__textLabel[pos + 1] = newLabel
                            
                            self.__pointStart.append(0)
                            self.__sizeNewData.append(value)
                            
                            self.__available.insert(0, False)
                            
                            flag = False
                    else:
                        sizeAvailable = self.__values[pos] - self.__values[pos - 1]
                        
                        if(self.__available[pos] == True and value <= sizeAvailable):
                            self.__values.insert(pos, self.__values[pos - 1] + value)
                            self.__textLabel.insert(pos, label)
                            
                            newValor = self.__values[pos + 1] - self.__values[pos] 
                            newLabel = str(newValor) + 'kb'                        
                            self.__textLabel[pos + 1] = newLabel
                            
                            self.__pointStart.append(self.__values[pos - 1])
                            self.__sizeNewData.append(value)
                            
                            self.__available.insert(pos, False)
                            
                            flag = False
                else:
                    flag = False  
                    
                pos += 1


    def bestFitAlgorithm(self, values, label):
        self.__newDataModification = True
        
        for value, label in zip(values, label):
            pos = 0
            flag = True
            bestFit = 9999999
            bestFitPos = -1
            
            
            for value_d in self.__values:
                if(pos < len(self.__values) and self.__available[pos]):
                    if pos == 0:
                        sizeAvailable = self.__values[0]
                    else:
                        sizeAvailable = self.__values[pos] - self.__values[pos - 1]
                    
                    if(sizeAvailable - value < bestFit and sizeAvailable - value >= 0):
                        bestFit = sizeAvailable - value
                        bestFitPos = pos
                
                pos += 1
                    
            if bestFitPos == 0:
                self.__values.insert(0, value)
                self.__textLabel.insert(0, label)
                
                newValor = self.__values[bestFitPos + 1] - value
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[bestFitPos + 1] = newLabel
                
                self.__pointStart.append(0)
                self.__sizeNewData.append(value)
                
                self.__available.insert(0, False)

            elif bestFitPos != -1:
                self.__values.insert(bestFitPos, self.__values[bestFitPos - 1] + value)
                self.__textLabel.insert(bestFitPos, label)
                
                newValor = self.__values[bestFitPos + 1] - self.__values[bestFitPos] 
                newLabel = str(newValor) + 'kb'                        
                self.__textLabel[bestFitPos + 1] = newLabel
                
                self.__pointStart.append(self.__values[bestFitPos - 1])
                self.__sizeNewData.append(value)
                
                self.__available.insert(bestFitPos, False)      
        
    
    def setData(self, data):
        self.__data = data
        
        