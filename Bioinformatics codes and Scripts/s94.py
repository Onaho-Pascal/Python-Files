filE = '/home/ahmed/C4/z-geneID_3667.gb'
with open(r'%s'%(filE), 'r') as opR:
    rLs = opR.readlines()
    print(opR.closed)

#print(rLs)
print(opR.closed)

with open(r'/home/ahmed/C4/z-e4.txt', 'w') as opW:
    opW.writelines(rLs)
print(opW.closed)
