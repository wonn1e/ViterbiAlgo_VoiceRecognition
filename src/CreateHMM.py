import copy
from DictionaryWordHMM import dictionaryHMM
from ReadBigram import bigram
from ReadUnigram import unigram
"""
create one huge HMM for viterbi algorithm
oh 1 2 3 4 5 6 7 8 9 0 0 sil
"""
def initialize(HMM, startStates):
    HMM[0][1] = float(unigram[4].uni)  #oh ow +1
    startStates[0] = 1
    HMM[0][5] = float(unigram[5].uni)  #one w ah n +1
    startStates[1] = 5
    HMM[0][15] = float(unigram[9].uni) #two t uw + 1
    startStates[2] = 15
    HMM[0][22] = float(unigram[8].uni) #three th r iy +1
    startStates[3] = 22
    HMM[0][32] = float(unigram[2].uni) #four f ao r +1
    startStates[4] = 32
    HMM[0][42] = float(unigram[1].uni) #five f ay v +1
    startStates[5] = 42
    HMM[0][52] = float(unigram[7].uni) #six s ih k s +1
    startStates[6] = 52
    HMM[0][65] = float(unigram[6].uni) #seven s eh v ah n +1
    startStates[7] = 65
    HMM[0][81] = float(unigram[0].uni) #eight ey t + 1
    startStates[8] = 81
    HMM[0][88] = float(unigram[3].uni) #nine n ay n +1
    startStates[9] = 88
    HMM[0][98] = float(unigram[10].uni) #zero z ih r ow +1
    startStates[10] = 98
    HMM[0][111] = float(unigram[10].uni) #zero z iy r ow +1
    startStates[11] = 111
    startStates[12] = 124         #sil 3
    
def setA(HMM, startStates, dicIdx):
    for l in range(13):
        i = 1
        j = 1

        for i_oh in range(startStates[l], startStates[l]+ dictionaryHMM.dicHMM[dicIdx[l]].stateNum):
            for j_oh in range(startStates[l], startStates[l]+ dictionaryHMM.dicHMM[dicIdx[l]].stateNum):
                HMM[i_oh][j_oh] = dictionaryHMM.dicHMM[dicIdx[l]].wordHMM[i][j]
                j = j+1
            j = 1
            i = i+1

def setBigramRelation(HMM, startStates, dicHMMIndex):
    for i in range(11):  #to first zero(row) & second zero(column)
        s_i = startStates[i+1]-1
        d_i = dicHMMIndex[i]
        d_len = dictionaryHMM.dicHMM[d_i].wordHMM.__len__() #word's HMM's length
        for j in range(12):
            s_j = startStates[j]
            if(j != 11):
                HMM[s_i-1][s_j] = dictionaryHMM.dicHMM[d_i].wordHMM[d_len-3][d_len-1] * float(bigram[i][j])
                HMM[s_i][s_j] = dictionaryHMM.dicHMM[d_i].wordHMM[d_len-2][d_len-1] * float(bigram[i][j])
            else: #second zero column
                HMM[s_i-1][s_j] = dictionaryHMM.dicHMM[d_i].wordHMM[d_len-3][d_len-1] * float(bigram[i][10])
                HMM[s_i][s_j] = dictionaryHMM.dicHMM[d_i].wordHMM[d_len-2][d_len-1] * float(bigram[i][10])
            
    #zero1-zero2 //row
    r_zero2 = startStates[12]-1
    dic_zero2 = dicHMMIndex[11]
    d_hmm_len = dictionaryHMM.dicHMM[dic_zero2].wordHMM.__len__()
    for k in range(12):
        k_j = startStates[k]
        if(k != 10 or k!=11):
            HMM[r_zero2-1][k_j] = dictionaryHMM.dicHMM[dic_zero2].wordHMM[d_hmm_len-3][d_hmm_len-1] * float(bigram[10][k])
            HMM[r_zero2][k_j] = dictionaryHMM.dicHMM[dic_zero2].wordHMM[d_hmm_len-2][d_hmm_len-1] * float(bigram[10][k])
        else:
            HMM[r_zero2-1][k_j] = dictionaryHMM.dicHMM[dic_zero2].wordHMM[d_hmm_len-3][d_hmm_len-1] * float(bigram[10][10])
            HMM[r_zero2][k_j] = dictionaryHMM.dicHMM[dic_zero2].wordHMM[d_hmm_len-2][d_hmm_len-1] * float(bigram[10][10])
            
    #sil(row)
    r_sil = HMM.__len__()-2
    for m in range(12):
        m_j = startStates[m]
        if(m != 11):
            HMM[r_sil][m_j] = dictionaryHMM.dicHMM[0].wordHMM[3][4] * float(bigram[11][m])
        else:
            HMM[r_sil][m_j] = dictionaryHMM.dicHMM[0].wordHMM[3][4] * float(bigram[11][10])
            
    #sil(column)
    c_sil = startStates[12]
    for l in range(12):
        d_i = dicHMMIndex[l]
        dlen = dictionaryHMM.dicHMM[d_i].wordHMM.__len__()
        row_i = startStates[l+1]-1
        if(l != 11):
            HMM[row_i][c_sil] = dictionaryHMM.dicHMM[d_i].wordHMM[dlen-3][dlen-1] * float(bigram[l][11])
            HMM[row_i][c_sil] = dictionaryHMM.dicHMM[d_i].wordHMM[dlen-2][dlen-1] * float(bigram[l][11])
        else:
            HMM[row_i][c_sil] = dictionaryHMM.dicHMM[d_i].wordHMM[dlen-3][dlen-1] * float(bigram[10][11])
            HMM[row_i][c_sil] = dictionaryHMM.dicHMM[d_i].wordHMM[dlen-2][dlen-1] * float(bigram[10][11])
        
    
def setEndProb(HMM, startStates, dicHMMIndex): 
    col = HMM.__len__() - 1
    #sil 
    HMM[col-1][col] = dictionaryHMM.dicHMM[0].wordHMM[3][4]
    for r in range(12):
        r_idx = startStates[r+1]-1
        r_dic = dicHMMIndex[r]
        r_dic_len = dictionaryHMM.dicHMM[r_dic].wordHMM.__len__()
        
        HMM[r_idx-1][col] = dictionaryHMM.dicHMM[r_dic].wordHMM[r_dic_len-3][r_dic_len-1]
        HMM[r_idx][col] = dictionaryHMM.dicHMM[r_dic].wordHMM[r_dic_len-2][r_dic_len-1]     #sp
        
        

module = copy.deepcopy(dictionaryHMM.dicHMM)

realStateAmount = 0
for eachM in module:
    realStateAmount = realStateAmount + eachM.stateNum

startStates = [0]*13
dicHMMIndex = [5, 6, 10, 9, 3, 2, 8, 7, 1, 4, 11, 12, 0]
moduleSound = [0]*13
for i in range(13):
    moduleSound[i] = dictionaryHMM.dicHMM[dicHMMIndex[i]].word
    
HMM = {}            #initialize whole HMM
for idx in range(realStateAmount+2):
    HMM[idx] = [0.0]* (realStateAmount+2)

initialize(HMM, startStates)

setA(HMM, startStates, dicHMMIndex)
setBigramRelation(HMM, startStates, dicHMMIndex)
setEndProb(HMM, startStates, dicHMMIndex)
