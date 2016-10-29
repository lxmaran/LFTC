from BinaryTree import *
from TokenTable import *
from FileReader import *

# from compiler.ast import flatten

constantsSymbolTbl = Tree()
identifiersSymbolTbl = Tree()
tokenTable = populateTokenTable(tokenNames)
program_text = ReadProgram('program.txt')
PIF = []


#
# separators = ['[', ']', '(', ')', '{', '}', ':', ';', ',', ';']
# def removeSeparator(listOfStrings, separator):
#     rez = []
#     for s in listOfStrings:
#         rez.append(str.split(s, separator))
#     rez = flatten(rez)
#     for s in rez:
#         if s is '':
#             rez.remove(s)
#     return rez
#
#
# def removeAllSeparators(listOfStrings, separators):
#     for separator in separators:
#         listOfStrings = removeSeparator(listOfStrings, separator)
#     return listOfStrings
#

def removeWhiteSpaces(listOfStrings):
    rez = []
    for s in listOfStrings:
        rez.extend(str.split(s, ' '))
    return rez


def formatProgramString(program):
    listOfStrings = str.split(program.replace("  ", ""), "\n")
    for s in range(0, len(listOfStrings)):
        listOfStrings[s] = listOfStrings[s].strip()

    rez = removeWhiteSpaces(listOfStrings)
    # rez = removeAllSeparators(rez, separators)
    return rez


def scanner(program_text):
    prog = formatProgramString(program_text)
    for i in range(0, len(prog)):

        if addTokenToPIF(PIF, prog[i]) is False:

            if checkIfTokenIsConstant(prog[i]) is True:
                if constantsSymbolTbl.addNode(constantsSymbolTbl.root, i, prog[i]) is False:
                    PIF.append({'token_code': 0, 'symbol_tbl_key': constantsSymbolTbl.search(prog[i]).key})
                else:
                    PIF.append({'token_code': 0, 'symbol_tbl_key': i})
            else:
                if identifiersSymbolTbl.addNode(identifiersSymbolTbl.root, i, prog[i]) is False:
                    PIF.append({'token_code': 1, 'symbol_tbl_key': identifiersSymbolTbl.search(prog[i]).key})
                else:
                    PIF.append({'token_code': 1, 'symbol_tbl_key': i})


def checkIfTokenIsConstant(token):
    if token[0] is "'" and token[len(token) - 1] is "'":
        return True
    if '0' <= token <= '9':
        return True
    return False


def addTokenToPIF(PIF, token):
    tk = getTokenKeyByName(token, tokenTable)
    if tk is not None:
        PIF.append({'token_code': tk, 'symbol_tbl_key': 0})
        return
    return False


if __name__ == '__main__':
    scanner(program_text)
    print PIF
    identifiersSymbolTbl.printInorder(identifiersSymbolTbl.root)
    print("---")
    constantsSymbolTbl.printInorder(constantsSymbolTbl.root)
