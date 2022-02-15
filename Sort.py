import os
import sys

def subSort(copyFold, originFold):
    listFold = os.listdir(originFold)
    for file in listFold:
            if os.path.isdir(originFold+"/"+file):
                os.makedirs(copyFold + "/" + file)
                subSort(copyFold + "/" + file, originFold + "/" + file)
            else:
                archive = open(copyFold + "/" + file, 'w')
                archive.close()
                os.rename(originFold + "/" + file, copyFold + "/" + file)


def Sort(letter, Dir, nameProgram):
    listDir = os.listdir(Dir)
    for file in listDir:
        bletter = (file[0] == letter or file[0] == letter.upper()) and file != nameProgram
        if bletter and file != letter.upper():
            print(f"Creating folder {letter}..")
            os.makedirs(letter.upper(), exist_ok=True)
            print(f"Folder {letter} created")
            
            if os.path.isdir(Dir+"/"+file):
                os.makedirs(Dir + "/" + letter.upper() + "/" + file)
                subSort(Dir + "/" + letter.upper() + "/" + file, Dir + "/" + file)
            else:
                archive = open(Dir + "/" + letter.upper() + "/" + file, 'w')
                archive.close()
                os.rename(Dir + "/" + file, Dir + "/" + letter.upper() + "/" + file)


print("Running..")
Dir = os.getcwd()
ListAlphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
nameProgram = os.path.basename(__file__)
for letter in ListAlphabet:
    print(f"Sorting folders and/or files with the letter {letter}..")
    Sort(letter,Dir, nameProgram)