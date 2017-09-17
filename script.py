import json
from time import sleep
from difflib import get_close_matches

data = json.load(open("data.json"))

def out(w):
    print("%s:" %w.capitalize())
    for i in range(len(data[w])):
        print("%d.%s" %(i+1,data[w][i]))

def suggest(matches):
    if len(matches) > 0:
        yn=input("Did you mean %s instead?(Y/N): "%matches[0].capitalize())
        if yn == "Y":
            out(matches[0])
            return
        elif yn == "N":
            matches.pop(0)
            suggest(matches)
    else:
        print("Ran out of Options! Please double check your word.")

def meaning(w):
    matches=get_close_matches(w,data.keys(),cutoff=0.8)
    if w in data.keys():
        out(w)
    elif len(matches) > 0:
        suggest(matches)
    else:
        print("The word doesn't make sense, please double check it.")

def read_inp(inp):
    if inp=="Y":
        meaning(input("Enter a word: ").lower())
        read_inp(input("\nWould you like to try again?(Y/N): "))
    elif inp=="N":
        print("\n\t\t\tTHANK YOU!\n")
        sleep(1)
        exit()
    else:
        read_inp(input("Please enter 'Y' for yes and 'N' for no: "))

print("\n\n\t\tCOMMAND-LINE WORDBOOK - by Lezend\n")
read_inp("Y")
