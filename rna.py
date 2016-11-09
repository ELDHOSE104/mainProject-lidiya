from __future__ import division
seq = "ACTNGTGCTYGATRGTAGC"
allowed_bases = ["A", "T", "G", "C", "Y", "R"]
total_dna_bases = 0
for base in allowed_bases:
    total_dna_bases = total_dna_bases + seq.count(base)
dna_fraction = total_dna_bases / len(seq)
print(dna_fraction * 100)