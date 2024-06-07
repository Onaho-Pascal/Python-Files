'''a = 10 # non-zero (True)
b = 0 # zero (False)
c = 'python' # non-null (True)
d = '' # null (False)

if d:
    print('ok')
else:
    print('zero or null')'''


# ============================

seQ = input('Input your sequence: ')
moD = len(seQ) % 3
if seQ:
    if moD == 1:
        print('The sequence contains an extra nucleotide.')
    elif moD == 2:
        print('The sequence contains two extra nucleotides.')
    #elif moD == 0:
        #print('The sequence does not contain extra nucleotides.')
    else:
        print('The sequence does not contain extra nucleotides.')
else:
    print('No sequence entered')
