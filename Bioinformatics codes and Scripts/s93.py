filE = '/home/ahmed/C4/z-geneID_3667.gb'
opR = open(r'%s'%(filE), 'r')
for i in opR:
    #print(i, end='')
    if i.startswith('ACCESSION'):
        print(i)
        #break
    if i.startswith('     mRNA            '):
        print(i)
    if i.startswith('                     /product'):
        print(i)
'''opR.seek(0)
rLs = opR.readlines()
print(rLs)'''