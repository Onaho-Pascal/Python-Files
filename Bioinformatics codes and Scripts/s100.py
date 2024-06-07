import time

inP = '/media/ahmed/Disk/C4Py4LS/scripts/z-e1.fasta'
with open(r'%s'%(inP),'r') as opR:
    rE = opR.read()
    rLines = rE.splitlines()

# Method 1
m1T1 = time.time()
filE = ''
sequences = ''
for i in rLines:
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
m1T2 = time.time()

m1T = m1T2-m1T1


# Method 2
m2T1 = time.time()
filE = ''
slicE = []
for iD, i in enumerate(rLines):
    if i.startswith('>'):
        slicE.append(iD)
        if len(slicE) == 2:
            starT = slicE[0] + 1
            enD = slicE[1]
            filE += '%s\n'%(rLines[slicE[0]])
            filE += '%s\n'%(''.join(rLines[starT:enD]))
            del slicE[0]
else:
    starT = slicE[0] + 1
    filE += '%s\n'%(rLines[slicE[0]])
    filE += '%s'%(''.join(rLines[starT:]))
m2T2 = time.time()

m2T = m2T2-m2T1

diff = m1T-m2T

if diff < 0:
    print('The method 1 (%f) is faster than the method 2 (%f)'%(m1T, m2T))
else:
    print('The method 2 (%f) is faster than the method 1 (%f)'%(m2T, m1T))