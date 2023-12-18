import time

class DogDoor():
    def __init__(self):
        self.open = False
        self.AllowedBarks = []
    
    def getAllowedBark(self):
        return self.AllowedBarks
    
    def addAllowedBark(self,bark):
        self.AllowedBarks.append(bark)

    def Open(self):
        # print("Open")
        self.open = True
        time.sleep(5)
        self.Close()

    def Close(self):
        # print("Close")
        self.open = False
    def IsOpen(self):
        # print("door open",self.open)
        return self.open        
