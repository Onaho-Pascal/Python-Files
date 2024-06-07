# isDNA
def isDNA(seQ):
    if 'T' in seQ:
        return 'Your sequence is DNA.'
    else:
        return 'Your sequence is RNA.'

# extNuc
def extNuc(seQ):
    moD = len(seQ) % 3
    if seQ:
        if len(seQ) >= 3:
            if moD == 1:
                return 'The sequence contains an extra nucleotide.'
            elif moD == 2:
                return 'The sequence contains two extra nucleotides.'
            else:
                return 'The sequence does not contain extra nucleotides.'
        else:
            return 'Error, the length of the sequence is less than 3 nucleotides.'
    else:
        return 'No sequence entered'

#Calling Function(s)
print('__name__ =', __name__)
if __name__ == '__main__':
    seQ = input('Input your sequence: ').upper()
    print('s110', isDNA(seQ))
    print('s110', extNuc(seQ))