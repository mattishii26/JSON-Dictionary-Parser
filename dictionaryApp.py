import json as j
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches


def getJSONFile(path):
    return j.load(open(path))
    
def searchData(jData, uInput):
    if uInput in jData:
        return jData[uInput] #handle raw input
    elif uInput.title() in jData:
        return jData[uInput.title()] # title() function converts first letter to uppercase, everything else lowercase
    elif uInput.upper() in jData:
        return jData[uInput.upper()] #handle all uppercase cases
    elif len(get_close_matches(uInput, jData.keys())) > 0:
        userCheck = input("Did you mean %s instead? Enter Y if yes, or N if no." % get_close_matches(uInput, jData.keys())[0]).lower()

        #while not (userCheck == 'y') or not (userCheck == 'n'):
        #    userCheck = input("Enter Y if yes, or N if no.").lower()
        #    print(userCheck)
        
        if userCheck == "y":
            return jData[get_close_matches(uInput, jData.keys())[0]]
        elif userCheck == "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "Wrong key pressed"
    else:
        return "The word doesn't exist. Please double check it."
def main():
    definitions = searchData(getJSONFile("data.json"), input("Enter a word you want to know a definiton of: ").lower())
    if(type(definitions) == list):
        for item in definitions:
            print(item)

if __name__ == "__main__":
    main()