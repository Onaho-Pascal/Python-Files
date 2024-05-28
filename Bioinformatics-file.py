Nucleotides = ["A", "C", "G", "T"]

# checking the sequence to ensure it is a DNA string

def validateSeq(dna_seq):
    tnpseq = dna_seq.upper()
    for nuc in tnpseq:
        if nuc not in Nucleotides:
            return False
    return tnpseq

#now, to generate a random sequence

import random

rndDNAstring = "".join([random.choice(Nucleotides)
                        for nuc in range(20)])

print(validateSeq(rndDNAstring))


#to test out this function
<<<<<<< HEAD
#the ".upper()" function changes any lowercased letter in the string to uppercase and prints it out
#as long as it is in the original dictonary of Nucleotides as given above

random_DNAstrg1 = "ACCGTAGTGACGGTGT"

random_DNAstrg2 = "CCTGCTAcctactg"

print(validateSeq(random_DNAstrg1))
print(validateSeq(random_DNAstrg2))

=======
#the "upper.()" function allows python to convert the given string into uppercase letters,
#then checks to see if they are among the given sting or dictonary in the firstline
random_DNAstrg1 = "CGGTAAATGCAACG"
random_DNAstrg2 = "CcgtGacGTGCacatTacG"
random_DNAstrg3 = "SHGBTACGTCAAGCTACTCTGA"



#print(validateSeq(random_DNAstrg1))
#print(validateSeq(random_DNAstrg2))
#print(validateSeq(random_DNAstrg3))


# now to create a random DNA sequence for testing and counting

def countnucfrequency(seq):
    tmpfreqdict = {"A": 0, "C": 0, "G": 0, "T":0}
    for nuc in seq:
        tmpfreqdict[nuc] += 1
    return tmpfreqdict

print(countnucfrequency(rndDNAstring))
>>>>>>> main

