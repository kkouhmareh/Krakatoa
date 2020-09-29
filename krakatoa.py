# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 15:01:09 2020

@author: Kourosh Kouhmareh
"""
def readFile():
    file = open('test.fasta')
    readFA = file.read()
    return readFA
    
readFile()
seq=readFile()

def fastA_Clean():
    sequences = []
    with open('test.fasta', 'r') as data:
        sequence = ''
        for line in data:
            if line.startswith('>'):
                sequences.append(sequence)
                sequence = ''
            else:
                sequence += line.strip()
    return(sequence)

cleanSEQ=fastA_Clean()

def GC_Count():
    numG=[]
    numC=[]
    length=len(cleanSEQ)
    for i in cleanSEQ:
        if i == 'G':
            numG.append(i)
    for j in cleanSEQ:
        if j == 'C':
            numC.append(j)
    GC = len(numC) + len(numG)
    GCalc = GC / length
    GCalc = str(GCalc)
    print('GC content for this sequence is ' + GCalc + '%.')

GC_Count()

def Nuc_Count():
    A = []
    C = []
    G = []
    T = []
    for i in cleanSEQ:
        if i == 'A':
            A.append(i)
        if i == 'C':
            C.append(i)
        if i == 'T':
            T.append(i)
        if i == 'G':
            G.append(i)
    A = len(A)
    C = len(C)
    T = len(T)
    G = len(G)
    A = str(A)
    C = str(C)
    T = str(T)
    G = str(G)
    print('Nucleotide composition: ' + 'A = ' + A + ' C = ' + C + ' G = ' + G + ' T = ' + T + '.')

Nuc_Count()


