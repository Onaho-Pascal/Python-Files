filE = '/home/ahmed/C4/z-e1-all.fasta'
opR = open(r'%s'%(filE), 'r')
'''opR.readline()
print(opR.readline())
print(opR.readline())'''
'''print(next(opR))
print(next(opR))
print(next(opR))'''

counter = 1
while counter <= 180:
    print(counter)
    #print(opR.readline())
    print(next(opR))
    counter += 1