import os

def ordenary(letter, Dir, nameProgram):
    listDir = os.listdir(Dir)
    for file in listDir:
        bletter = (file[0] == letter or file[0] == letter.upper()) and file != nameProgram
        if bletter and not(os.path.isdir(Dir+"/"+letter.upper()) and file == letter.upper()):
            try:
                print(f"Creating folder {letter}..")
                os.makedirs(letter.upper(), exist_ok=True)
                print(f"Folder {letter} created")
            except:
                None
            archive = open(Dir + "/" + letter.upper() + "/" + file)
            archive.close()
            os.rename(Dir + "/" + file, Dir + "/" + letter.upper() + "/" + file)


print("Running..")
Dir = os.getcwd()
ListAlphabet = [chr(i) for i in range(ord('a'),ord('z')+1)]
nameProgram = os.path.basename(__file__)
for letter in ListAlphabet:
    print(f"Sorting folders and/or files with the letter {letter}..")
    ordenary(letter,Dir, nameProgram)