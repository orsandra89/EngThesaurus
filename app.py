import json
from difflib import get_close_matches

data = json.load(open("EngThesaurus\data.json"))

def translator(word):
    """Func that return information of words"""
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter the Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else: 
            return "We didn't understand your entry."
    else:
        return "Word doesn't exist. Please double check it."

word = input("Enter word: ")

output = translator(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)