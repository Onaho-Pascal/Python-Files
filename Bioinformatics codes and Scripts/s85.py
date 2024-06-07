inP = '/home/ahmed/C4/z-e1.fasta'#input('Input a FASTA file: ')
#print(inP)
opR = open(r'%s'%(inP), 'r')
rE = opR.read(); #print(rE)
opR.close()

# Method 2
rLines = rE.splitlines(); #print(rLines)
filE = ''
slicE = []
for iD, i in enumerate(rLines):
    #print(iD,i, sep='\n')
    if i.startswith('>'):
        slicE.append(iD)
        if len(slicE) == 2:
            starT = slicE[0] + 1
            enD = slicE[1]
            #print(slicE, starT, enD)
            #print(''.join(rLines[starT:enD]))
            filE += '%s\n'%(rLines[slicE[0]])
            filE += '%s\n'%(''.join(rLines[starT:enD]))
            del slicE[0]
else:
    #print(slicE)
    starT = slicE[0] + 1
    #print(''.join(rLines[starT:]))
    filE += '%s\n'%(rLines[slicE[0]])
    filE += '%s'%(''.join(rLines[starT:]))

#print(slicE)
print(filE)

opW = open(r'z-e1-method2.fasta', 'w')
opW.write(filE)
opW.close()