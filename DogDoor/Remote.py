class Remote():
    def __init__(self,door):
        self.door = door 

    def PressButton(self):
        if self.door.IsOpen() :
            self.door.Close()
        else :
            self.door.Open()   

class Bark():
    def __init__(self,bark):
        self.bark = bark  
    def getSound(self):
        return self.bark
    def equals(self,otherBark) :
        return self.bark == otherBark.bark
    
class BarkRecognizer():
    def __init__(self,door):
        self.door = door

    def recognize(self,bark):
        allowedbarks  = self.door.AllowedBarks
        for i in range(len(allowedbarks)):
            if bark.equals(allowedbarks[i]) :
                self.door.Open()
                return True   
        print("Not Owner Dog")
        return False    