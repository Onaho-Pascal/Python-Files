seQ = input('Input your sequence: ')
moD = len(seQ) % 3
if moD == 1:
    print('The sequence contains an extra nucleotide.')
elif moD == 2:
    print('The sequence contains two extra nucleotides.')
    '''elif moD == 0:
    print('The sequence does not contain extra nucleotides.')'''
else:
    print('The sequence does not contain extra nucleotides.')


