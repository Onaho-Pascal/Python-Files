#======================================
# GC content calculator
#======================================
# >example_sequence (10 bases)
# AAATTTCCGG
#======================================
sequencE = input('Input your sequence: ')
countGC = 0
sequenceLength = len(sequencE)
if sequencE:
    for nuC in sequencE:
        #print(nuC)
        if nuC == 'C' or nuC == 'G':
            countGC += 1
    else:
        print('GC content = ', (countGC/sequenceLength)*100, '%')
else:
    print('No sequence entered')

#print('GC content = ', (countGC/sequenceLength)*100, '%')
