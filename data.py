import sys, os

class Data:
    def __init__(self):
        self.__noSort = [os.path.basename(__file__)]
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