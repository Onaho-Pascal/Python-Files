# isDNA
def isDNA(seQ):
    seQ = input('Input your sequence: ').upper()
    if 'T' in seQ:
        print('Your sequence is DNA.')
    else:
        print('Your sequence is RNA.')

# extNuc
def extNuc(seQ):
    #seQ = input('Input your sequence: ')
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

#Calling Function(s)
'''seQ = input('Input your sequence: ').upper()
isDNA(seQ)
extNuc(seQ)'''