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

def sortStandar(letter, Dir, data):
    listDir = os.listdir(Dir)
    for file in listDir:
        if ((file[0]==letter or file[0]==letter.upper()) and 
            not(data.isNoSort(file))):
            if not(os.path.isdir(Dir + "/" + letter.upper())):
                print(f"Creating folder {letter}..")
                os.makedirs(Dir+ "/" + letter.upper())
                print(f"Folder {letter} created")
            if os.path.isdir(Dir + "/" + file):
                os.makedirs(Dir + "/" + letter.upper() + "/" + file)
                subSort(Dir + "/" + letter.upper() + "/" + file, Dir + "/" + file)
            else:
                archive = open(Dir + "/" + letter.upper() + "/" + file, 'w')
                archive.close()
                os.rename(Dir + "/" + file, Dir + "/" + letter.upper() + "/" + file)

def sortMono(folderName, Dir, data):
    listDir = os.listdir(Dir)
    for file in listDir:
        if (file[0:(len(data.getArgv()[3]))]==data.getArgv()[3] and
            not(data.isNoSort(file)) and file!=folderName):
                if not(os.path.isdir(Dir + "/" + folderName)):
                    print(f"Creating folder {folderName}..")
                    os.makedirs(Dir+ "/" + folderName)
                    print(f"Folder {folderName} created")
                if os.path.isdir(Dir + "/" + file):
                    os.makedirs(Dir + "/" + folderName + "/" + file)
                    subSort(Dir + "/" + folderName + "/" + file, Dir + "/" + file)
                else:
                    archive = open(Dir + "/" + folderName + "/" + file, 'w')
                    archive.close()
                    os.rename(Dir + "/" + file, Dir + "/" + folderName + "/" + file)

def standar(data, Dir, i):

    for i in range(i,len(data.getArgv())):
        if not(os.path.isdir(data.getArgv()[i])):
            sys.exit(f"[ERROR] Does not exist the Directory: {data.getArgv()[i]}")
        print(f"[SORTING]: {data.getArgv()[i]}")
        for letter in data.getListAlphabet():
            print(f"Sorting folders and/or files with the letter {letter}..")
            sortStandar(letter,Dir + "/" + data.getArgv()[i], data)
    print("[FINALIZED]")

def mono(data, Dir, i):
    if not(os.path.isdir(data.getArgv()[i])):
        sys.exit(f"[ERROR] Does not exist the Directory: {data.getArgv()[i]}")
    print(f"[SORTING]: {data.getArgv()[i]}")
    print(f"Sorting folders and/or files with {data.getArgv()[2]}..")
    sortMono(data.getArgv()[2],Dir + "/" + data.getArgv()[i], data)
    return 0


def run(data, i):
    while 1:
        if (os.path.isdir(f"Escritorio") or os.path.isdir(f"Desktop")):
            break
        elif(os.getcwd()=="/"):
            sys.exit("[ERROR] Desktop not found")
        os.chdir("../")

    Dir = os.getcwd()

    print("Running..")
    if i==1:
        standar(data, Dir, i)
    elif i==4:
        mono(data, Dir, i)
    else:
        sys.exit("[ERROR]")

def help():
    print("Running mode:\n\n"
            "[STANDARD] Sort folders and files in the directories given as argument. For running:\n"
            "   python3 Sort.py \"<directory1>\" \"<directory2>\" ... \"<directoryN>\"\n\n"
            "[MONO] Sort folders and files on the <nameFolder> that meets a <condition>\n"
            "       (that condition is a word found in the names of the folders and files\n"
            "       to sort) on the directories given as argument. For running:\n"
            "   python3 Sort.py -l <nameFolder> <condition> <directory>\n\n"
            "[HELP] For run:\n"
            "   python3 Sort.py --help\n"
            "   python3 Sort.py\n")

