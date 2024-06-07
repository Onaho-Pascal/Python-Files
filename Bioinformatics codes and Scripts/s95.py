import os
'''cwD = os.getcwd().split('/')
print(cwD)'''

#print(os.listdir())
cwD = os.getcwd()
#os.chdir('%s/%s'%(cwD, 'z-tRNA-rRNA_methyltransferase'))
os.chdir('z-tRNA-rRNA_methyltransferase')

print(os.listdir())