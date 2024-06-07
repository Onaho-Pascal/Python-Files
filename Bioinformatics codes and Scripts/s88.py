# Python for Biologists
filE = '/home/ahmed/C4/z-e2.txt'
opW = open(r'%s'%(filE), 'w+')
opW.write('Hello, world')
print(opW.tell())
opW.seek(0)
print(opW.tell())
rE = opW.read(); print(rE)
opW.close()