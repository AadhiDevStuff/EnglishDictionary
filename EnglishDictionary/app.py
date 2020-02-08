import json
from difflib import get_close_matches

# loading the json data file.
data = json.load(open("data.json"))

def translate(w):
    # converting all the input to lower case.
    w = w.lower()

    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]    
   
    elif len(get_close_matches(w,data.keys())) > 0:
         # returning the first closest word to the entered word    
        yn = input("Did you mean'%s' instead ? if yes enter 'y' if no enter 'n' :" % get_close_matches(w,data.keys())[0])

        #checking if the user meant the recommended word
        if yn == "y":
            return data[get_close_matches(w,data.keys())[0]]

        elif yn == "n":
            return "The word doesn't exist please double check the word."  

        else:
            return "we didn't understand your option.chosse the right option."      

    else:
        return "The word does not exist please check it once more:"

word = input("Enter word:")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)        