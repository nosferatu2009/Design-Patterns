from guitar import *

class Inventory():
    InstrumentList  = []
    
    def __init__(self):
          self.InstrumentList = []
    def addInstrument(self, serialNumber,price,specs):
         instrument = Instrument(serialNumber,price,specs)
         self.InstrumentList.append(instrument)
        #  print("Added" ,instrument.serialNumber)
    
    def showInstrument(self):
        for i in range(len(self.InstrumentList)) :
            print(self.InstrumentList[i].serialNumber)
    
    def search(self, specs):
        matchList = []
        for i in range(len(self.InstrumentList)) :
            if specs.equals(self.InstrumentList[i].specs) :
                matchList.append(self.InstrumentList[i])
        return matchList    
 


