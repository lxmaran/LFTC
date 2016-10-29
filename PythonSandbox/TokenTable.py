tokenNames = ['string', 'int', 'const', 'entry_point', 'array', 'char', 'while', 'if', 'else', 'read', 'write',
              '+', '-', '++', '--', '/', '*', '%', '=', '==', '!', '>', '<', '=>', '<=', '!=', '[', ']', '(', ')',
              '{', '}', ':', ';', ',', ';'
              ]


def populateTokenTable(listTokenNames):
    TokenTable = [{'name': 'identifier', 'token': 0}, {'name': 'const', 'token': 1}]

    for i in range(2, len(listTokenNames)):
        TokenTable.append({'name': listTokenNames[i], 'token': i})
    return TokenTable


print populateTokenTable(tokenNames)
