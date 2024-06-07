#======================================
# GC content calculator
#======================================
# >example_sequence (10 bases)
# AAATTTCCGG
#======================================
sequencE = input('Input your sequence: ')
countGC = 0
sequenceLength = len(sequencE)
indeX = 0
if sequencE:
    while indeX < sequenceLength:
        nuC = sequencE[indeX]
        #print('Index:', indeX, nuC)
        if nuC == 'C' or nuC == 'G':
            countGC += 1
        indeX += 1
    '''else:
        print('GC content = ', (countGC/sequenceLength)*100, '%')'''
else:
    print('No sequence entered')

print('GC content = ', (countGC/sequenceLength)*100, '%')
