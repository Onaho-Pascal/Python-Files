'''filE = '/home/ahmed/C4/z-e1-all.fasta'
opR = open(r'%s'%(filE), 'r')
rLs = opR.readlines()
print(rLs)'''
rLs = ['ATG\n', 'GGG\n', 'CCC\n', 'TAA\n']
opW = open(r'/home/ahmed/C4/z-e1-all-writelines.fasta', 'w')
opW.writelines(rLs)