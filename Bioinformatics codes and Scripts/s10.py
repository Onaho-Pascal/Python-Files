dicT = {'A':'Adenine',
'C':'Cytosine',
'G':'Guanine',
'T':'Thymine',
'U':'Uracil',
'R':'A or G',
'Y':'C or T',
'S':'G or C',
'W':'A or T',
'K':'G or T',
'M':'A or C',
'B':'C or G or T',
'D':'A or G or T',
'H':'A or C or T',
'V':'A or C or G',
'N':'any base',
'.':'gap',
'-':'gap'}

"""inP = input('Input an IUPAC nucleotide code (UPPERCASE LETTER): ')
print(dicT[inP])"""

# A or C
inP2 = input('Input IUPAC nucleotide code(s): ')
vaL = list(dicT.values()).index(inP2)
keY = list(dicT.keys())[vaL]
print(keY)