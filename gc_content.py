seq = 'CGATCGATGCTGCAGTCTAGTGGTCATCGCGATCAGATCGTAGG'

# Initialize the GC counter
n_gc = 0

# Loop through the sequence and count G's and C's
for base in seq:
    if base in 'GCgc':
        n_gc += 1

print(n_gc / len(seq))
