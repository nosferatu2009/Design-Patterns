from enum import Enum

class Builder(Enum):
    ABC=1,
    RMD=2,
    WER=3,
    RST=4


class Wood(Enum):
    BROWN=1,
    BLACK=2,
    ORANGE=3,
    YELLOW=4

class InstrumentType(Enum):
    GUITAR = 1,
    VIOLIN = 2,
    BANJO = 3

class Instrument() :
    def __init__(self,serialNumber,price,specs):
        self.serialNumber = serialNumber
        self.price = price
        self.specs = specs
    
    def getSerialNumber(self):
        return self.serialNumber
    
    def getPrice(self):
        return self.price        
    

class InstrumentSpec():
    def __init__(self,properties):
         self.properties = properties

    def getproperties(self):
        return self.builder
    
    def getproperty(self,key):
        return self.properties[key] 
    
    def equals(self,secondspecs):
       
        match = True
        if self.getproperty("Builder") != secondspecs.getproperty("Builder"):
            match = False
        if self.getproperty("Wood") != secondspecs.getproperty("Wood") :
            match = False
        
        return match
