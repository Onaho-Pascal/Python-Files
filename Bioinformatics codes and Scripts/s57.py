strA = '''>NC_000012.12:c102481839-102395874 Homo sapiens chromosome 12, GRCh38.p14 Primary Assembly
AAGCAGAACTGTGTTTTCAGTTGATGTGTCAGTCCCCTGAGAGTCATGTGGAAAAAAAAAAAAAGAAAAA
ATTCAAGGTCCAGGTTATTTCCACCACTCCTGGGAAACCAGGCCTGGAGAGCTCTCTAGGGAAAGAGGTA
TGTCTGCTCTGGGCTTTTGCAACCTTATTTTATAATTCACTTTCTTATCTACTGCTTCACAAAACCAAAG
GGAAATAGGTACAAACTGTATCGACAAAAGATCAGAACTGAATTCTCAATGGCAAAGGCAAGTGTACATT
ATAAATAGCAAAACAGCTGGCTTGGACCATGTTGCCGGCCAGTCACCCAGTTGAGGGATTTGAATGACAT
CATAACCCTCGAGAGGGTATTGCTAGCCAGCTGGTGTTATTTAGAATACACAAAAATCAGAGAAAGAAAA
CACACTCTGGCACACAGACTCCCTCTGTCATACACACACACACACACACACACACACACACACACACACA'''
listA = strA.splitlines(); #print(listA)
print(listA[1:])
listA[0] = '>NC_000012.12'; print(listA)
del listA[0]; print(listA)
