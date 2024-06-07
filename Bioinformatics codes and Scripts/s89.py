# Python for Biologists
filE = '/home/ahmed/C4/z-e2.txt'
opW = open(r'%s'%(filE), 'a+')
opW.seek(0)
rE = opW.read(); print(rE)
opW.write('Hello, world')
opW.close()