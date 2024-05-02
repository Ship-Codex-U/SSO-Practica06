class DataFile:
    def __init__(self):
        self.__dataText = []
        
    @property
    def dataText(self):
        return self.__dataText
    
    @dataText.setter
    def dataText(self, dataText):
        self.__dataText = dataText
    
    def open(self, path):
        self.__dataText = []
        try:
            with open(path, 'r') as file:
                for line in file:
                    self.__dataText.append(line.strip())               
            return 1
        except:
            return 0
    
    def save(self, path):
        try:
            with open(path, 'w') as file:
                file.writelines(self.__dataText)
            return 1
        except:
            return 0