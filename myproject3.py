

#Dna transcribed to mrna sequence

def transcribe_dna_sequence_to_rna(dna_sequence):
    dict = {'A': 'U', 'G':'C', 'C':'G','T':'A'}
    transcribed_sequence = (dict[base] for base in dna_sequence)
    return''.join(transcribed_sequence)

my_dna_sequence = "ATGGCTTACCGTAGGTACCGTAGGCTTACCGTAGGCTTAC"
rna_sequence = transcribe_dna_sequence_to_rna(my_dna_sequence)
print(rna_sequence)

# length of rna sequence
def find_length_of_rna(rna_sequence):
    return(len(rna_sequence))

length_rna_sequence = find_length_of_rna("UACCGAAUGGCAUCCAUGGCAUCCGAAUGGCAUCCGAAUG")
print(length_rna_sequence)

# position of start and stop codon of rna sequence 

def find_start_codon(sequence, start_codon):
    index = sequence.find(start_codon)
    return index

rna_sequence = "UACCGAAUGGCAUCCAUGGCAUCCGAAUGGCAUCCGAAUG"
start_codon = "AUG"
result = find_start_codon(rna_sequence, start_codon)
print(result)

def find_stop_codon(sequence, stop_codon):
    index = sequence.find(stop_codon)
    return index

rna_sequence = "UACCGAAUGGCAUCCAUGGCAUCCGAAUGGCAUCCGAAUG"
stop_codon = "UAG"
result = find_stop_codon(rna_sequence, stop_codon)
print(result)

def find_stop_codon(sequence, stop_codon):
    index = sequence.find(stop_codon)
    return index

rna_sequence = "UACCGAAUGGCAUCCAUGGCAUCCGAAUGGCAUCCGAAUG"
stop_codon = "UAA"
result = find_stop_codon(rna_sequence, stop_codon)
print(result)

def find_stop_codon(sequence, stop_codon):
    index = sequence.find(stop_codon)
    return index

rna_sequence = "UACCGAAUGGCAUCCAUGGCAUCCGAAUGGCAUCCGAAUG"
stop_codon = "UGA"
result = find_stop_codon(rna_sequence, stop_codon)
print(result)




    

