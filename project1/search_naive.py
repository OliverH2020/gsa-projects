#! /usr/bin/python
import os
from parsers import fasta, fastq
import sys

def exact(string, pattern):
    matched = []
    j,i = 0,0 
    while j < len(string)-len(pattern)+1:
        if i == len(pattern):
            matched.append(j)
            j += 1
            i = 0
        else:
            if string[j+i] == pattern[i]:
                i += 1
            else:
                j += 1
                i = 0
    return matched

def naive_program(strings, patterns):
    #these should be 
    all_res = []
    for key1 in patterns:
        pat = patterns[key1][0]
        qual = patterns[key1][1]
        for key in strings:
            string = strings[key]
            res = exact(string, pat)
            printing_sam(key1, pat,"0", key, res, qual)
            all_res.append(res)
    return all_res

def printing_sam(name, pat, number, nameseq, res, quality):
    for i in res:
        print(name+"\t"+number+"\t"+nameseq+"\t"+str(i+1)+"\t"+number+"\t"+str(len(pat))+"M"+"\t"+"*"+"\t"+number+"\t"+number+"\t"+pat+"\t"+quality)


if __name__ == '__main__':
    fa_file = sys.argv[1]
    fq_file = sys.argv[2]
    parsed_fa = fasta(fa_file)
    parsed_fq = fastq(fq_file)
    res = naive_program(parsed_fa, parsed_fq)
    # print(res)

    # fa_file = sys.argv[1]
    # fq_file = sys.argv[2]
    # # parsed_fa = fasta(fa_file)
    # # parsed_fq = fastq(fq_file)
    # res = exact(fa_file, fq_file)
    # print(res)


