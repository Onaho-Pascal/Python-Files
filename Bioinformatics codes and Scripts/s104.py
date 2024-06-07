dicT = {'A':['A'],
'C':['C'],
'G':['G'],
'T':['T'],
'R':['A','G'],
'Y':['C','T'],
'S':['C','G'],
'W':['A','T'],
'K':['G','T'],
'M':['A','C'],
'B':['C','G','T'],
'D':['A','G','T'],
'H':['A','C','T'],
'V':['A','C','G'],
'N':['A','C','G','T']}

# ambToNuc
def ambToNuc():
    inP = input('Input IUPAC nucleotide code: ').upper()
    print(dicT[inP])

# nuc2Amb
def nuc2Amb():
    inP2 = input('Input nucleotide code(s): ')
    if len(inP2) <= 4 and len(inP2) >= 1:
        if inP2.isalpha() and 'U' not in inP2.upper():
            uPlist = list(inP2.upper())
            uPlist.sort()
            vaL = list(dicT.values()).index(uPlist)
            print(list(dicT.keys())[vaL])
        else:
            print('Please, input DNA letters only!')
    else:
        print('Please, check your input!')
        print('From 1 to 4 characters only!')

# ecoriSearch
def ecoriSearch():
    ecoRI = 'GAATTC'
    seq = input('Input your sequence: ').upper()
    print(ecoRI in seq)

# isDNA
def isDNA():
    seQ = input('Input your sequence: ').upper()
    if 'T' in seQ:
        print('Your sequence is DNA.')
    else:
        print('Your sequence is RNA.')

# extNuc
def extNuc():
    seQ = input('Input your sequence: ')
    moD = len(seQ) % 3
    if seQ:
        if len(seQ) >= 3:
            if moD == 1:
                print('The sequence contains an extra nucleotide.')
            elif moD == 2:
                print('The sequence contains two extra nucleotides.')
            else:
                print('The sequence does not contain extra nucleotides.')
        else:
            print('Error')
            print('The length of the sequence is less than 3 nucleotides.')
    else:
        print('No sequence entered')

# gCal
def gCal():
    sequencE = input('Input your sequence: ').upper()
    countCG = 0
    sequenceLength = len(sequencE)
    indeX = 0
    if sequencE:
        while indeX < sequenceLength:
            nuC = sequencE[indeX]
            if nuC == 'C' or nuC == 'G':
                countCG += 1
            indeX += 1
        else:
            print('GC content = ', ((countCG/sequenceLength)*100), '%')
    else:
        print('No sequence entered')
    #return ('GC content = {GC} %'.format(GC=(countCG/sequenceLength)*100))

#ambToNuc()
#nuc2Amb()
#ecoriSearch()
#isDNA()
#extNuc()
#aFun = gCal(); print(aFun)
#leN = len('ATG'); print(leN)