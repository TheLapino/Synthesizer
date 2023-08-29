class Note:
    def __init__(self, name, freq) -> None:
        self.name = name
        self.freq = freq

    def getName(self):
        return self.name
    
    def getFreq(self):
        return self.freq