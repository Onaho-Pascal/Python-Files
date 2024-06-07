filesList = ['/home/ahmed/C4/z-e1.fasta',
             '/home/ahmed/C4/z-e1-method1.fasta',
             '/home/ahmed/C4/z-e1-method2.fasta']

for i in filesList:
    print(i)
    opR = open(r'%s'%(i), 'r')
    rE = opR.read(); #print(rE)
    opR.close()


    opW = open(r'z-e1-all.fasta', 'a')
    opW.write('%s\n'%(rE))
    opW.close()
