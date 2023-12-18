from Inventory import *
from guitar import *

if __name__ == "__main__" :
    try :    
        prop1 = { "InstrumentType" : InstrumentType.GUITAR ,
                "Wood" : Wood.BLACK,
                "Builder" : Builder.ABC
            }

        prop2 = { "InstrumentType" : InstrumentType.VIOLIN ,
            "Wood" : Wood.BLACK,
            "Builder" : Builder.ABC
                    }
        inventory = Inventory()
        inventory.addInstrument(1,100,InstrumentSpec(prop1))
        inventory.addInstrument(2,200,InstrumentSpec(prop2))
        prop = {"Builder" : Builder.ABC,"Wood" : Wood.BLACK}
        clientSpecs = InstrumentSpec(prop)

        # inventory.showInstrument()

        matchList = inventory.search(clientSpecs)
        
        if len(matchList) == 0 :
            print("No mathces found for this filter")
        else :   
            print("matches found")
            # for i in range(len(matchList)):
                # print("serial Number  {0}, Price {1}, Model {2},Wood {3},Builder {4} ".format(matchList[i].serialNumber,matchList[i].price,matchList[i].guitarspecs.model,matchList[i].guitarspecs.wood,matchList[i].guitarspecs.builder))               
    except Exception as e:
        print("Error occured {0}".format(e.args))