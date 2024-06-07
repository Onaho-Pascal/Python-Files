# gCal
def gCal(sequencE):
    sequencE = sequencE.upper()
    print('Inside', sequencE)
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
    return ('GC content = {GC} %'.format(GC=(countCG/sequenceLength)*100))

#Calling Function:
sequencE = input('Input your sequence: ')
print('Before', sequencE)
gCal(sequencE)
print('After',sequencE)
