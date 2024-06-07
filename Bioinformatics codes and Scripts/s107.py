#(HindIII=AAGCTT, BamHI=GGATCC)

'''# ecoriSearch
def ecoriSearch(seq, ecoRI = 'GAATTC'):
    #ecoRI = 'GAATTC'
    print(ecoRI in seq)
    return seq.find(ecoRI)

sequencE = input('Input your sequence: ').upper()
#rE = ecoriSearch(ecoRI='AAGCTT', seq=sequencE); print(rE + 1)
rE = ecoriSearch(sequencE, 'AAGCTT'); print(rE + 1)'''

# ecoriSearch
def ecoriSearch(seq, *ecoRI):
    for i in ecoRI:
        #ecoRI = 'GAATTC'
        print(i , i in seq)
        #return seq.find(ecoRI)

sequencE = input('Input your sequence: ').upper()
rE = ecoriSearch(sequencE, 'AAGCTT', 'GGATCC', 'GAATTC'); #print(rE + 1)