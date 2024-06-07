inP = '/home/ahmed/C4/z-e1.fasta'#input('Input a FASTA file: ')
#print(inP)
opR = open(r'%s'%(inP), 'r')
rE = opR.read(); #print(rE)
opR.close()
# Method 1
'''rLines = rE.splitlines(); #print(rLines)
filE = ''
sequences = ''
for i in rLines:
    #print(i)
    if i.startswith('>'):
        if i == rLines[0]:
            filE += '%s\n'%(i)
        else:
            filE += '%s\n'%(sequences)
            sequences = ''
            filE += '%s\n'%(i)
    else:
        sequences += i
else:
    filE += '%s'%(sequences)
print(filE)
#print(sequences)
opW = open(r'z-e1-method1.fasta', 'w')
opW.write(filE)
opW.close()'''