def dna_finder(sequence):
    empty = []
    useless = []
    for seq in sequence:
        if seq == "A" or seq == "C" or seq == "T" or seq == "G":
            empty += seq
        else:
            useless += seq
    return (useless, empty)
