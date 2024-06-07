sequencE = 'ATGCGGCGCCCTGCTTAA'
var1 = 'ATGC'
var2 = 'TACG'
comP = str.maketrans(var1, var2); #print(comP)
print(sequencE)
print(sequencE.translate(comP))