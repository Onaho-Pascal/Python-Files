#%c %s %i %f | .format()
listA = ['ATG', 'CGC', 'CTT', 'TAA']
a = 'AA123'
num = 1
floaT = 1.5

#print('%chmed'%a)
#print('%shmed'%a)
#print('%ihmed'%num)
#print('%fhmed'%floaT)

for index, i in enumerate(listA):
    #print('The codon number %i is %s' %(index+1, i))
    print('The codon number {arg1} is {arg2}'.format(arg2=i, arg1 = index+1))

