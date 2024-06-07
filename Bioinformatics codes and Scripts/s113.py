# gCal
def gCal(sequencE):
    countCG = 0
    sequenceLength = len(sequencE)
    indeX = 0
    #print(locals())
    #print(globals())
    if sequencE:
        while indeX < sequenceLength:
            nuC = sequencE[indeX]
            if nuC == 'C' or nuC == 'G':
                countCG += 1
            indeX += 1
        else:
            return ('GC content = {GC} %'.format(GC=(countCG/sequenceLength)*100))
    else:
        return 'No sequence entered'

#Calling Function:
if __name__ == '__main__':
    seQ = input('Input your sequence: ')
    fuN = gCal(sequencE=seQ); print(fuN)
    #print(gCal(sequencE=seQ))
    '''print(globals())
    print(locals())'''