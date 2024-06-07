a = 10 # 00001010
b = 20 # 00010100
'''
print('a', bin(a))
print('b', bin(b))
print('a', int('00001010', 2))
print('b', int('00010100', 2))
'''
# 1 = True , 0 = False
#print('bitwise operation:', a & b)
#print('bitwise operation:', a | b)
#print('bitwise operation:', a ^ b)
#print('bitwise operation:', ~a, ~b)
print('manual operation:', '000010')
#print('bitwise operation:', a << 3)
print('bitwise operation:', a >> 2)
print('manual operation conversion:', int('000010', 2))

