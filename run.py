import sys, Sort
from data import Data

def commands(data):
    if(len(data.getArgv())>1):
        if(len(data.getArgv())==2 and data.getArgv()[1] == '--help'):
            Sort.help()
        elif(len(data.getArgv())==5 and data.getArgv()[1] == '-l'):
            Sort.run(data, 4)
        elif(data.getArgv()[1]!='--help' and data.getArgv()[1]!='-l'):            
            Sort.run(data, 1)
        else:
            sys.exit("[ERROR] Invalid arguments")    
    else:
        Sort.help()

data = Data()
commands(data)
