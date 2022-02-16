import os
import sys

def subSort(copyFold, originFold):
    listFold = os.listdir(originFold)
    for file in listFold:
            if os.path.isdir(originFold + "/" + file):
                os.makedirs(copyFold + "/" + file)
                subSort(copyFold + "/" + file, originFold + "/" + file)
            else:
                archive = open(copyFold + "/" + file, 'w')
                archive.close()
                os.rename(originFold + "/" + file, copyFold + "/" + file)
    os.rmdir(originFold) 


def Sort(letter, Dir, nameProg):
    listDir = os.listdir(Dir)
    for file in listDir:
        if ((file[0]==letter or file[0]==letter.upper()) and 
            file!=nameProg and file!=letter.upper()):
            if not(os.path.isdir(Dir+"/"+letter.upper())):
                print(f"Creating folder {letter}..")
                os.makedirs(Dir+"/"+letter.upper())
                print(f"Folder {letter} created")
            if os.path.isdir(Dir+"/"+file):
                os.makedirs(Dir + "/" + letter.upper() + "/" + file)
                subSort(Dir + "/" + letter.upper() + "/" + file, Dir + "/" + file)
            else:
                archive = open(Dir + "/" + letter.upper() + "/" + file, 'w')
                archive.close()
                os.rename(Dir + "/" + file, Dir + "/" + letter.upper() + "/" + file)

print("Running..")
argv = sys.argv
if (len(argv)<2):
    sys.exit("[ERROR] No directories to sort")

while 1:
    if (os.path.isdir(f"Escritorio") or os.path.isdir(f"Desktop")):
        break
    elif(os.getcwd()=="/"):
        sys.exit("[ERROR] Desktop not found")
    os.chdir("../")

Dir = os.getcwd()
ListAlphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
nameProg = os.path.basename(__file__)

for i in range(1,len(argv)):
    if not(os.path.isdir(argv[i])):
        sys.exit(f"[ERROR] Does not exist the Directory: {argv[i]}")
    print(f"[Sorting]: {argv[i]}")
    for letter in ListAlphabet:
        print(f"Sorting folders and/or files with the letter {letter}..")
        Sort(letter,Dir+"/"+argv[i], nameProg)
print("[Finalized]")