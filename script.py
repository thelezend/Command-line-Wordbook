"""
Command-line Workbook - by Lezend
"""
import json, sys, time
from difflib import get_close_matches

def print_slow(output):
    for letter in output:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

def out(w):
    print_slow(w+"\n")
    for i in range(len(data[w])):
        print_slow("%d. %s\n" %(i+1,data[w][i]))

def suggest(matches):
    if len(matches) > 0:
        print_slow("Did you mean %s instead?(Y/N): "%matches[0]())
        yn=input().upper()
        if yn == "Y":
            out(matches[0])
            return
        elif yn == "N":
            matches.pop(0)
            suggest(matches)
        else:
            print_slow("Please enter 'Y' for yes and 'N' for no\n")
            suggest(matches)
    else:
        print_slow("Ran out of Options! Please double check your word.\n")

def meaning(w):
    matches=get_close_matches(w,data.keys(),cutoff=0.8)
    if w in data.keys():
        out(w)
    elif w.capitalize() in data.keys():
        out(w.capitalize())
    elif w.upper() in data.keys():
        out(w.upper())
    elif len(matches) > 0:
        suggest(matches)
    else:
        print_slow("The word doesn't exist in the English language.")

def read_inp(inp):
    if inp=="Y":
        print_slow("Enter a word: ")
        meaning(input().lower())
        print_slow("\nWould you like to try again?(Y/N): ")
        read_inp(input().upper())
    elif inp=="N":
        print_slow("\n\t\t\tT H A N K  Y O U !\n\n")
        time.sleep(1)
        exit()
    else:
        print_slow("Please enter 'Y' for yes and 'N' for no: ")
        read_inp(input().upper())

data = json.load(open("data.json"))

print("\n\n\t\t", end='')
for letter in "COMMAND LINE WORDBOOK\n\t\t\t BY LEZEND":
    print(letter + " ", end='')
print("\n")
time.sleep(1)

read_inp("Y")
