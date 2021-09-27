import os
import sys

"""
Program for parseing file in fasta and fastq:
"""

def fasta(fa):
    parsed = {}
    fasta_file = open(fa, "r")
    l = fasta_file.read().split(">")[1:]
    for element in l:
        todic = element.split("\n")
        id = todic[0]
        seq = ''.join(todic[1:])
        parsed[id] = seq
    
    return parsed


def fastq(fq):
    parsed = {}
    fastq_file = open(fq, "r")
    # l = fastq_file.readlines()
    l = fastq_file.read().split("@")[1:]
    for element in l:
        todic = element.split("\n")
        id = todic[0]
        seq = todic[1]
        qual = todic[3]
        parsed[id] = [seq,qual]
    
    return parsed
