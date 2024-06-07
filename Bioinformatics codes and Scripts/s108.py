# ecoriSearch
'''def ecoriSearch(seq):
    ecoRI = 'GAATTC'
    print(ecoRI in seq)
    return seq.find(ecoRI)'''

#sequencE = input('Input your sequence: ').upper()
#ecoriSearch(sequencE)

ecoriSearch = lambda seq, ecoRI = 'GAATTC': print(ecoRI in seq)

sequencE = input('Input your sequence: ').upper()
ecoriSearch(sequencE)
