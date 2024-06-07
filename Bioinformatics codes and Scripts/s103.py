dicT = {'A':['A'],
'C':['C'],
'G':['G'],
'T':['T'],
'R':['A', 'G'],
'Y':['C', 'T'],
'S':['C', 'G'],
'W':['A', 'T'],
'K':['G', 'T'],
'M':['A', 'C'],
'B':['C', 'G', 'T'],
'D':['A', 'G', 'T'],
'H':['A', 'C', 'T'],
'V':['A', 'C', 'G'],
'N':['A', 'C', 'G', 'T']}

# nuc2Amb
inP2 = input('Input IUPAC nucleotide code(s): ')
if len(inP2) <= 4 and len(inP2) >= 1:
    if inP2.isalpha() and 'U' not in inP2 and 'u' not in inP2:
        uPlist = list(inP2.upper()); #print(uPlist)
        uPlist.sort(); #print(uPlist)
        vaL = list(dicT.values()).index(uPlist)
        keY = list(dicT.keys())[vaL]
        print(keY)
    else:
        print('Please, input DNA letters only!')
else:
    print('Please, check your input!')
    print('Please, from 1 to 4 characters only!')
