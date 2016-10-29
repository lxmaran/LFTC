def ReadProgram(file):
    _file = open(file, 'r')
    program = _file.read()
    _file.close()
    return program
