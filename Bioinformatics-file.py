Nucleotides = ["A", "C", "G", "T"]

# checking the sequence to ensure it is a DNA string

def validateSeq(dna_seq):
    tnpseq = dna_seq.upper()
    for nuc in tnpseq:
        if nuc not in Nucleotides:
            return False
    return tnpseq

#to test out this function

random_DNAstrg = "CGGTAAATGCAACG"

print(validateSeq(random_DNAstrg))

