
def main():
    brackets = {("(",")") : 0, ("[", "]") : 0, ("{", "}") : 0, ("<", ">") : 0}
    openers = ["(", "[", "{", "<"]
    closers = [")", "]", "}", ">"]
    #TODO: TREAT THE INPUT AND PUT THE INFO ON A LIST OF STRINGS (ONE STRING PER LINE)
    listInput = TreatInput()
    #TODO: WE NEED TO FIND THE ERROR FOR THAT WE NEED TO TAKE A COUPLE OF STEPS:
        #RUN THROUGH EACH STRING
        #WHILE THAT WE CHECK EACH CHAR IF IT IS IN THE BRACKETS DICTIONARY (IF IT ISN'T THERE'S AN ERROR SOMEWHERE)
            #WE CHECK IF IT IS IN THE OPPENERS OR CLOSERS LIST
                #IF OPPENER WE ADD +1 ON THE CORRECT DICTIONARY KEY
                #IF CLOSER WE SUBRACT 1 AND CHECK IF VALUE ON DICT IS < 0
                    #IF VALUE IS < 0 IT MEANS THAT WE FOUND AN ERROR
    FindError()


def TreatInput():
    ...

def FindError (listInputs, brackets, openers, closers):
    ...

if __name__ == "__main__":
    main()