from BinaryTree import *
from TokenTable import *

identifiersSymbolTbl = Tree()
constantsSymbolTbl = Tree()
tokenTable = populateTokenTable(tokenNames)


def main():
    print tokenTable
