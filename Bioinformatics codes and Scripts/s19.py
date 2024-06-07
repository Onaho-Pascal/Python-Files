# EcoRI 5` GAATTC 3`
# HindIII 5` AAGCTT 3`
# >seq
# ATGCGATCGAATTCCGCTACGACTAAGCTTG
# ATGCGATCGAATTCCGCTACGACTAAGCTG

ecoRI = 'GAATTC'
HindIII = 'AAGCTT'
seq = input('Input your sequence: ')
#print(ecoRI in seq and HindIII in seq)
print(ecoRI in seq or HindIII in seq)
