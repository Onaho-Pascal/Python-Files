Nucleotides = ["A", "C", "G", "T"]

# checking the sequence to ensure it is a DNA string

def validateSeq(dna_seq):
    tnpseq = dna_seq.upper()
    for nuc in tnpseq:
        if nuc not in Nucleotides:
            return False
    return tnpseq

#to test out this function
#the "upper.()" function allows python to convert the given string into uppercase letters,
#then checks to see if they are among the given sting or dictonary in the firstline
random_DNAstrg1 = "CGGTAAATGCAACG"
random_DNAstrg2 = "CcgtGacGTGCacatTacG"
random_DNAstrg3 = "SHGBTACGTCAAGCTACTCTGA"



print(validateSeq(random_DNAstrg1))
print(validateSeq(random_DNAstrg2))
print(validateSeq(random_DNAstrg3))



