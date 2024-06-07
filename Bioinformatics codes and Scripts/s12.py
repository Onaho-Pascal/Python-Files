# >seq_1
# ATGCGACTGGCA
# >seq_2
# ATGCGACTGGCAT
# >seq_3
# ATGCGACTGGCATA
# >seq_4
# ATGCGACTGGCATAA
nuC = input('Input your sequence: ')
nucLen = len(nuC)
print('The number of extra nucleotides:', nucLen%3)