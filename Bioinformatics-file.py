Nucleotides = ["A", "C", "G", "T"]

# checking the sequence to ensure it is a DNA string

def validateSeq(dna_seq):
    tnpseq = dna_seq.upper()
    for nuc in tnpseq:
        if nuc not in Nucleotides:
            return False
    return tnpseq

#to test out this function
#the ".upper()" function changes any lowercased letter in the string to uppercase and prints it out
#as long as it is in the original dictonary of Nucleotides as given above

random_DNAstrg1 = "ACCGTAGTGACGGTGT"

random_DNAstrg2 = "CCTGCTAcctactg"

print(validateSeq(random_DNAstrg1))
print(validateSeq(random_DNAstrg2))


