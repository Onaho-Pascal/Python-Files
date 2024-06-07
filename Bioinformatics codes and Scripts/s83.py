opR = open(r'/home/ahmed/C4/z-escape_characters.tab', 'r')
#print(opR)
'''print(opR.name)
print(opR.mode)
print(opR.closed)'''
rE = opR.read(); print(rE[:180])
opR.close()
#print(opR.closed)

