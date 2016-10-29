tokenNames = ['string', 'int', 'const', 'entry_point', 'array', 'char', 'while', 'if', 'else', 'read', 'write',
              '+', '-', '++', '--', '/', '*', '%', '=', '==', '!', '>', '<', '=>', '<=', '!=', '[', ']', '(', ')',
              '{', '}', ':', ';', ',', ';'
              ]


def populateTokenTable(listTokenNames):
    TokenTable = [{'name': 'identifier', 'token_key': 0}, {'name': 'const', 'token_key': 1}]

    for i in range(0, len(listTokenNames)):
        TokenTable.append({'name': listTokenNames[i], 'token_key': i+2})
    return TokenTable


def getTokenKeyByName(token, tokenTable):
    for t in tokenTable:
        if t['name'] == token:
            return t['token_key']
    return None