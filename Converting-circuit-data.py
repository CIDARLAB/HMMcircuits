
# coding: utf-8

# In[1]:

goodCircuits = [["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBM3R1","RiboJ10","S2","SrpR","ECK120019600","pBAD","pHlyIIR","SarJ","B3","BM3R1","L3S3P11","pTet","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pTac","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pBetI","RiboJ53","P3","PhlF","ECK120033737","pBAD","pTet","RiboJ10","S2","SrpR","ECK120019600","pPhlF","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pAmtR","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTet","RiboJ54","F1","AmeR","L3S3P31","pTac","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pBetI","RiboJ53","P3","PhlF","ECK120033737","pTac","pTet","RiboJ10","S3","SrpR","ECK120019600","pPhlF","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pAmtR","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTet","RiboJ54","F1","AmeR","L3S3P31","pTac","pAmtR","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","S1","SrpR","ECK120019600","pSrpR","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pPhlF","pAmtR","RiboJ57","E1","BetI","L3S3P11","pBetI","RiboJ51","H1","HlyIIR","ECK120033736","pTet","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pBetI","RiboJ53","P3","PhlF","ECK120033737","pTac","pTet","RiboJ10","S3","SrpR","ECK120019600","pHlyIIR","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTet","RiboJ54","F1","AmeR","L3S3P31","pTac","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBAD","pHlyIIR","RiboJ10","S4","SrpR","ECK120019600","pTet","pAmtR","RiboJ57","E1","BetI","L3S3P11","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pSrpR","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pTac","RiboJ10","S3","SrpR","ECK120019600","pTet","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","pHlyIIR","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pTac","RiboJ10","S3","SrpR","ECK120019600","pTet","pHlyIIR","SarJ","B3","BM3R1","L3S3P11","pPhlF","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pBAD","pAmtR","RiboJ53","P2","PhlF","ECK120033737","pAmtR","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","pHlyIIR","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pPhlF","pTet","RiboJ10","S3","SrpR","ECK120019600","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pTet","pAmtR","RiboJ57","E1","BetI","L3S3P11","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pBAD","RiboJ10","S2","SrpR","ECK120019600","pTac","RiboJ51","H1","HlyIIR","ECK120033736","pTet","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pBetI","RiboJ53","P3","PhlF","ECK120033737","pBAD","RiboJ10","S2","SrpR","ECK120019600","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","pHlyIIR","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pBAD","pTet","RiboJ10","S3","SrpR","ECK120019600","pTac","pTet","RiboJ57","E1","BetI","L3S3P11","pTac","pAmtR","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBM3R1","pTet","RiboJ10","S3","SrpR","ECK120019600","pBAD","SarJ","B1","BM3R1","L3S3P11","pSrpR","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pBetI","RiboJ53","P3","PhlF","ECK120033737","pAmtR","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTet","RiboJ54","F1","AmeR","L3S3P31","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pBAD","pTet","RiboJ10","S4","SrpR","ECK120019600","pTac","pAmtR","RiboJ51","H1","HlyIIR","ECK120033736","pTet","BydvJ","A1","AmtR","L3S2P55"],
["pTac","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","S2","SrpR","ECK120019600","pSrpR","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pPhlF","pTet","RiboJ51","H1","HlyIIR","ECK120033736"],
["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pTac","RiboJ10","S3","SrpR","ECK120019600","pPhlF","SarJ","B2","BM3R1","L3S3P11","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pBAD","pTet","SarJ","B3","BM3R1","L3S3P11","pBM3R1","BydvJ","A1","AmtR","L3S2P55"],
["pBAD","pTet","RiboJ10","S3","SrpR","ECK120019600","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736"],
["pTac","pTet","RiboJ53","P3","PhlF","ECK120033737","pBAD","pTet","RiboJ10","S3","SrpR","ECK120019600","pPhlF","pAmtR","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pTet","pAmtR","RiboJ57","E1","BetI","L3S3P11","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pTac","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pTet","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","S1","SrpR","ECK120019600","pPhlF","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pTet","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","S2","SrpR","ECK120019600","pTac","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pBAD","pTet","RiboJ10","S3","SrpR","ECK120019600","pSrpR","BydvJ","A1","AmtR","L3S2P55"],
["pBAD","pTet","RiboJ10","S3","SrpR","ECK120019600","pTac","BydvJ","A1","AmtR","L3S2P55"],
["pBAD","pHlyIIR","SarJ","B2","BM3R1","L3S3P11","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736"],
["pBetI","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pTac","pAmeR","RiboJ57","E1","BetI","L3S3P11","pTac","pTet","RiboJ54","F1","AmeR","L3S3P31","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","pHlyIIR","BydvJ","A1","AmtR","L3S2P55"],
["pSrpR","pHlyIIR","RiboJ53","P3","PhlF","ECK120033737","pBAD","RiboJ10","S2","SrpR","ECK120019600","pTac","pTet","RiboJ51","H1","HlyIIR","ECK120033736"],
["pSrpR","pAmtR","RiboJ53","P3","PhlF","ECK120033737","pTac","RiboJ10","S3","SrpR","ECK120019600","pBAD","BydvJ","A1","AmtR","L3S2P55"],
["pTac","BydvJ","A1","AmtR","L3S2P55","RiboJ53","P3","PhlF","ECK120033737","pTet","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pBAD","pTet","RiboJ51","H1","HlyIIR","ECK120033736","pBAD","pHlyIIR","BydvJ","A1","AmtR","L3S2P55"],
["pTac","pTet","RiboJ53","P2","PhlF","ECK120033737","pBAD","RiboJ10","SrpR","ECK120019600","pSrpR","pAmtR","SarJ","B2","BM3R1","L3S3P11","pTet","pHlyIIR","RiboJ57","E1","BetI","L3S3P11","pTac","RiboJ51","H1","HlyIIR","ECK120033736","pPhlF","BydvJ","A1","AmtR","L3S2P55"]]


# In[2]:

#import regex - regular expressions
import re

#iterating through the list of lists that is the good circuits text file
for sublist in goodCircuits:
    for substring in sublist:
        if type(substring)==str:
            #series of if statements and regex to check which transcriptional unit (?) it is and make a dict with label
            if re.findall(r"[p]\S", substring):
                goodCircuits[goodCircuits.index(sublist)][sublist.index(substring)] = {substring:"promoter"}
            elif re.findall(r"[Ribo]\S", substring):
                goodCircuits[goodCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribosome"}
            elif re.findall(r"\b[A-Z][\d]{1}", substring):
                goodCircuits[goodCircuits.index(sublist)][sublist.index(substring)] = {substring:"ribosyme binding site"}
            elif re.findall(r"\b[A-Z][a-zA-Z]+$", substring):
                goodCircuits[goodCircuits.index(sublist)][sublist.index(substring)] = {substring:"coding sequence"}
            elif re.findall(r"[ECK][\d]+$", substring):
                goodCircuits[goodCircuits.index(sublist)][sublist.index(substring)] = {substring:"terminator"}
print goodCircuits


# In[ ]:

promoterTerminatorSets=[]
#making sublists
for sublist in goodCircuits:
    i=0
    while i<len(sublist):
        substring = sublist[i]
        #nested if statements. It can either be promoter-promoter-ribosome-ribosyme binding site-coding sequence-terminator
        #OR promoter-ribosome-ribosyme binding site-coding sequence-terminator (either 1 or 2 promoters), right?
        if substring.values()[0]=='promoter':
            if sublist[i+1].values()[0]=='promoter':
                if sublist[i+2].values()[0]=='ribosome':
                    if sublist[i+3].values()[0]=='ribosyme binding site':
                        if sublist[i+4].values()[0]=='coding sequence':
                            if sublist[i+5].values()[0]=='terminator':
                                promoterTerminatorSets.append([sublist[i+j] for j in range(0,5)])
                                i=i+5
                                print [sublist[i+j] for j in range(0,5)]
            
            elif sublist[sublist.index(substring)+1].values()[0]=='ribosome':
                    if sublist[sublist.index(substring)+2].values()[0]=='ribosyme binding site':
                        if sublist[sublist.index(substring)+3].values()[0]=='coding sequence':
                            if sublist[sublist.index(substring)+4].values()[0]=='terminator':
                                promoterTerminatorSets.append([sublist[i+j] for j in range(0,4)])
                                i=i+4
                                print [sublist[i+j] for j in range(0,4)]
            else:
                i=i+1

print promoterTerminatorSets


# In[ ]:



