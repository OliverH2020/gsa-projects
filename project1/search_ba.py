#! /usr/bin/python
import os
from parsers import fasta, fastq
import sys

def border_array(x):
    ba = [0]*len(x)
    for i in range(1,len(x)):
        b = ba[i-1]
        while x[b] != x[i] and b > 0:
            b = ba[b-1]
        if x[i] == x[b]:
            ba[i] = b + 1
    
    return ba

def ba_search(string, pattern):
    pba = border_array(pattern)
    matched = []
    b = 0 
    for i in range(len(string)):
        while b > 0 and string[i] != pattern[b]: 
            b = pba[b-1]
        if string[i] == pattern[b]:
            b += 1 
            if b == len(pattern):
                matched.append(i-len(pattern)+1)
                b = pba[len(pattern)-1]

    return matched

def border_program(strings, patterns):
    #these should be 
    all_res = []
    for key1 in patterns:
        pat = patterns[key1][0]
        qual = patterns[key1][1]
        for key in strings:
            string = strings[key]
            res = ba_search(string, pat)
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
    res = border_program(parsed_fa, parsed_fq)

    # fa_file = sys.argv[1]
    # fq_file = sys.argv[2]
    # # parsed_fa = fasta(fa_file)
    # # parsed_fq = fastq(fq_file)
    # res = ba_search(fa_file, fq_file)
    # print(res)


