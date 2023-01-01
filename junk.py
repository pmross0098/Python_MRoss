# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:59:23 2022

@author: pmros
"""

import os
filenames = os.listdir(os.getcwd())

print(os.getcwd())

fasta = Bio.SeqIO.FastaIO.SimpleFastaParser(open("../dna.example.fasta"))

# with open("../dna.example.fasta") as handle:
#     for values in Bio.SeqIO.FastaIO.SimpleFastaParser(handle):
#         print(values)
#         print('-------------')

seq = fin_list[0][1]
frame = 0

x = findORF(fin_list[0][1], 0)
y = max([i[1] for i in x])
z = [i[1] for i in x].index(y)
                    
y = comp_repseqs([x,x,x])
z=x
length=4

x = rpt_seq(seq, 5)

######## SCRIPT

# seq = 'ATGACAGCTCCGTTCAGGGGGAGGGGGTAAGTTCGCCAGGCCGAATCGTTGGTAGCCAAGCGGCAACGACTCGAATATAGAGAGCCGATTGGAATTCCGTAA'
handle = open("dna.example.fasta")
fin_dict = dict_fst(handle)

# len(fin_list)

lens = len_records(fin_dict, 'max')

max(lens)
lens.count(max(lens))

min(lens)
lens.count(min(lens))

lens

mm = 'max'
fasta = fin_list[2]
len('ATGGCCTCCAGCGCACCGATCGGATCAAAGCCGCTGAAGCCTTCGCGCATCAGGCGGCCATAG')

m=max(lens) if mm=='max' else min(lens)



lngst = ['',[0,0], '']
for sq in seq_dict:
    for frm in range(3):
        orfs = MRBio.MRBio_Crs1.findORF(sq, seq_dict, frm)
        locmx = MRBio.MRBio_Crs1.maxORF(orfs, 'max')
        lngst = [sq, locmx, seq_dict[sq][0][locmx[0]:locmx[0]+locmx[1]]] if locmx[1] > lngst[1][1] else lngst

sq = 'gi|142022655|gb|EQ086233.1|160 marine metagenome JCVI_SCAF_1096627390048 genomic scaffold, whole genome shotgun sequence'

MRBio.MRBio_Crs1.rpt_seq()

frm = 0
length = 3
rept_dict = {}

    seq = seq_dict[sq][0]
    all_sqs = [seq[i:i+length] for i in range((len(seq)-length+1))]
    rept_dict = dict((x, all_sqs.count(x)) for x in set(all_sqs))

rept_dict['ATG']

bigORF_f2[0].split()[0]
