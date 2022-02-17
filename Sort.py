import os
import sys

class Data:
    def __init__(self):
        self.__noSort = [os.path.basename(__file__), "README.md"]
        self.__ListAlphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
        self.__argvs = sys.argv

    def getNoSort(self):
        return self.__noSort
    
    def getListAlphabet(self):
        return self.__ListAlphabet

    def getArgv(self):
        return self.__argvs

    def isNoSort(self,file):
        for elem in self.__noSort:
            if elem==file:
                return True
        for elem in self.__ListAlphabet:
            if elem==file:
                return True
        return False

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


def Sort(letter, Dir, data):
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

def run(data):
    print("Running..")
    while 1:
        if (os.path.isdir(f"Escritorio") or os.path.isdir(f"Desktop")):
            break
        elif(os.getcwd()=="/"):
            sys.exit("[ERROR] Desktop not found")
        os.chdir("../")

    Dir = os.getcwd()

    for i in range(1,len(data.getArgv())):
        if not(os.path.isdir(data.getArgv()[i])):
            sys.exit(f"[ERROR] Does not exist the Directory: {data.getArgv()[i]}")
        print(f"[SORTING]: {data.getArgv()[i]}")
        for letter in data.getListAlphabet():
            print(f"Sorting folders and/or files with the letter {letter}..")
            Sort(letter,Dir + "/" + data.getArgv()[i], data)
    print("[FINALIZED]")

def help():
    print("Running mode:\n"
            "[STANDARD]:\n"
            "   python3 Sort.py \"<directory1>\" \"<directory2>\" ... \"<directoryN>\"\n"
            "Commands:\n"
            "[HELP]:\n"
            "   python3 Sort.py --help\n"
            "   python3 Sort.py\n")

data = Data()

if len(data.getArgv())<=2:
    if len(data.getArgv())<=1 or data.getArgv()[1]=='--help':
        help()
    elif data.getArgv()[1]!='--help':
        run(data)
    else:
        sys.exit("[ERROR] Invalid arguments")
else:
    run(data)
