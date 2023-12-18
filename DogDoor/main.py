from DogDoor import DogDoor
from Remote import *
import time

if __name__ == "__main__" :
    bark1 = Bark("Woof")
    bark2 = Bark("Roof")
    door = DogDoor()

    door.addAllowedBark(bark1)
    door.addAllowedBark(bark2)

    remote = Remote(door)
    barkrecognizer = BarkRecognizer(door)

    print("Fido barks!!")
    bark3 = Bark("Roof")
    val = barkrecognizer.recognize(bark3)
    if val : 
        print("Fido goes outside")
        # print("Gina Press button")
        # remote.PressButton()
        print("Fido Finishes")
        if door.IsOpen():
            print("Fido gets inside")
        else :    
            print("Fido barks")
            bark4 = Bark("Woof")
            barkrecognizer.recognize(bark4)
            print("Fido gets inside")

    # if door.IsOpen():
    #     print("Fido gets inside")
    # else :
    #     print("Fido Barks")
    #     print("Gina Press remote")
    #     remote.PressButton()
    #     print("Fido is inside")
