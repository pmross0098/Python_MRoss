#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:59:23 2022

@author: pmros

Module contains numerous DNA sequence manipulation functions written in 
preparation for the final of the Coursera class, 'Python for Genomic Sciences'
"""

# import Bio.SeqIO
import os
import sys
sys.path
sys.path.append('C:/Programming/Python')
sys.path

import MRBio.MRoss_PfDDS
# filenames = os.listdir(os.getcwd())

print(os.getcwd())

######## SCRIPT ##########

fs_handle = open('dna2.fasta')

# Q1
# How many records are in the file? 
seq_dict = MRBio.MRoss_PfDDS.dict_fst(fs_handle)

# Q2
# What are the lengths of the sequences in the file? 
# What is the longest sequence and what is the shortest sequence? 
# Is there more than one longest or shortest sequence? 
# What are their identifiers?
max_len = MRBio.MRoss_PfDDS.len_records(seq_dict, 'max')
max_len
min_len = MRBio.MRoss_PfDDS.len_records(seq_dict, 'min')
min_len

# seq = seq_dict[list(seq_dict.keys())[1]]
# Q3
# What is the length of the longest ORF in the file?
# What is the identifier of the sequence containing the longest ORF?
bigORF_f2 = MRBio.MRoss_PfDDS.maxORF_file_frame(seq_dict, 1)
bigORF_f2

bigORF_f3 = MRBio.MRoss_PfDDS.maxORF_file_frame(seq_dict, 2)
bigORF_f3

bigORF_full = MRBio.MRoss_PfDDS.maxORF_file(seq_dict)
bigORF_full

# For a given sequence identifier, what is the longest ORF contained in the 
# sequence represented by that identifier? 
# What is the starting position of the longest ORF in the sequence that contains it?
sq = 'gi|142022655|gb|EQ086233.1|16'
spec_seq = MRBio.MRoss_PfDDS.maxORF_seq(sq, seq_dict)
spec_seq

# seqs = list(seq_dict.keys())
# sq = seqs[1]
# bigORF_se = MRBio.MRoss_PfDDS.maxORF_seq(sq, seq_dict)
# bigORF_se

# Q4
# Given a length n, your program should be able to identify all repeats of 
# length n in all sequences in the FASTA file.
allrpts6 = MRBio.MRoss_PfDDS.rpt_seq_fl(seq_dict, length = 6)
combrpt_dict6 = MRBio.MRoss_PfDDS.comb_repseqs(allrpts6)
max_rpt6 = MRBio.MRoss_PfDDS.freq_rep(combrpt_dict6)

# Q9
allrpts12 = MRBio.MRoss_PfDDS.rpt_seq_fl(seq_dict, length = 12)
combrpt_dict12 = MRBio.MRoss_PfDDS.comb_repseqs(allrpts12)
max_rpt12 = MRBio.MRoss_PfDDS.freq_rep(combrpt_dict12)

ct = 0
for rpt in combrpt_dict12:
    if combrpt_dict12[rpt] == 10:
        ct+=1
        print (rpt, combrpt_dict12[rpt])
ct

# Q10
allrpts7 = MRBio.MRoss_PfDDS.rpt_seq_fl(seq_dict, length = 7)
combrpt_dict7 = MRBio.MRoss_PfDDS.comb_repseqs(allrpts7)
combrpt_dict7['AATGGCA']
combrpt_dict7['CATCGCC']
combrpt_dict7['TGCGCGC']
combrpt_dict7['CGCGCCG']

    
