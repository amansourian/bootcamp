start_codon = 'AUG'
stop_codons = ('UAA', 'UAG', 'UGA')

#codon = 'UAG'

#if codon == start_codon:
#    print('This codon is the start codon.')
#elif codon in stop_codons:
#    print('This codon is a stop codon.')
#else:
#    print('This codon is not the start or stop codon.')

seq = 'ACGUACGUGUCGUAGAUCAGUCGUCUCGAUCAUCGACAUAGCGUAUC'

# Initialize sequence index
i = 0

# Scan the sequence until start codon
while seq[i:i+3] != start_codon and i < len(seq):
    i += 1

if i == len(seq):
    print('Start codon not found.')

else:
    print('start codon at index', i)
