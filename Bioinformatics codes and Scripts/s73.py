dicT = {'A':'Adenine',
'C':'Cytosine',
'G':'Guanine',
'T':'Thymine'}
#'U' ='Uracil'
#print(dicT.get('U', 'not found'))
#print(dicT.setdefault('U'))
print(dicT.setdefault('U', 'Uracil'))
print(dicT)