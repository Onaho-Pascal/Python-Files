strA = '''>NC_000012.12:c102481839-102395874 Homo sapiens chromosome 12, GRCh38.p14 Primary Assembly
AAGCAGAACTGTGTTTTCAGTTGATGTGTCAGTCCCCTGAGAGTCATGTGGAAAAAAAAAAAAAGAAAAA
ATTCAAGGTCCAGGTTATTTCCACCACTCCTGGGAAACCAGGCCTGGAGAGCTCTCTAGGGAAAGAGGTA
TGTCTGCTCTGGGCTTTTGCAACCTTATTTTATAATTCACTTTCTTATCTACTGCTTCACAAAACCAAAG
GGAAATAGGTACAAACTGTATCGACAAAAGATCAGAACTGAATTCTCAATGGCAAAGGCAAGTGTACATT
ATAAATAGCAAAACAGCTGGCTTGGACCATGTTGCCGGCCAGTCACCCAGTTGAGGGATTTGAATGACAT
CATAACCCTCGAGAGGGTATTGCTAGCCAGCTGGTGTTATTTAGAATACACAAAAATCAGAGAAAGAAAA
CACACTCTGGCACACAGACTCCCTCTGTCATACACACACACACACACACACACACACACACACACACACA'''
#print(strA.split(':'))
#print(strA.splitlines())
#print(strA.splitlines()[0])
print(''.join(strA.splitlines()[1:]))

