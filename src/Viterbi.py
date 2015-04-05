import math
import os
import copy
from CreateHMM import HMM
from ReadHMM import sylList
from CreateHMM import moduleSound   # array of words' word oh, one, two...
from CreateHMM import startStates

class stateJ:
    def __init__(self):
        self.syl = {}
        self.state = {}
    def setStateJ(self, syl, state):
        self.syl = syl
        self.state = state

def eln(x):
    if(x == 0):
        return -1111111000000
    elif(x > 0):
        return math.log(x)
    
def elnproduct(eln_x, eln_y):
    if eln_x == -1111111000000 or eln_y ==-1111111000000:
        return -1111111000000 
    return eln_x + eln_y
     
def identifyWord(s, e, seq):
    if((s == 1 and e == 3) or (s == 1 and e == 4)):
        if(any(x for x in seq if x == 1) and any(x for x in seq if x == 2) and any(x for x in seq if x == 3)):
            return 'o'
    elif((s == 5 and e == 13) or (s == 5 and e == 14)):
        if(any(x for x in seq if x == 5) and any(x for x in seq if x == 6) and any(x for x in seq if x == 7) and any(x for x in seq if x == 8) and any(x for x in seq if x == 9) and any(x for x in seq if x == 10) and any(x for x in seq if x ==11) and any(x for x in seq if x == 12) and any(x for x in seq if x == 13)):
            return '1'
    elif((s == 15 and e == 20) or (s == 15 and e == 21)):
        if(any(x for x in seq if x == 15) and any(x for x in seq if x == 16) and any(x for x in seq if x == 17) and any(x for x in seq if x == 18) and any(x for x in seq if x == 19) and any(x for x in seq if x == 20)):
            return '2'
    elif((s == 22 and e == 30) or (s == 22 and e == 31)):
        if(any(x for x in seq if x == 22) and any(x for x in seq if x == 23) and any(x for x in seq if x == 24) and any(x for x in seq if x == 25) and any(x for x in seq if x == 26) and any(x for x in seq if x == 27) and any(x for x in seq if x == 28) and any(x for x in seq if x == 29) and any(x for x in seq if x == 30)):
            return '3'
    elif((s == 32 and e == 40) or (s == 32 and e == 41)):
        if(any(x for x in seq if x == 32) and any(x for x in seq if x == 33) and any(x for x in seq if x == 34) and any(x for x in seq if x == 35) and any(x for x in seq if x == 36) and any(x for x in seq if x == 37) and any(x for x in seq if x == 38) and any(x for x in seq if x == 39) and any(x for x in seq if x == 40)):
            return '4'
    elif((s == 42 and e == 50) or (s == 42 and e == 51)):
        if(any(x for x in seq if x == 42) and any(x for x in seq if x == 43) and any(x for x in seq if x == 44) and any(x for x in seq if x == 45) and any(x for x in seq if x == 46) and any(x for x in seq if x == 47) and any(x for x in seq if x == 48) and any(x for x in seq if x == 49) and any(x for x in seq if x == 50)):
            return '5'
    elif((s == 52 and e == 63) or (s == 52 and e == 64)):
        if(any(x for x in seq if x == 52) and any(x for x in seq if x == 53) and any(x for x in seq if x == 54) and any(x for x in seq if x == 55) and any(x for x in seq if x == 56) and any(x for x in seq if x == 57) and any(x for x in seq if x == 58) and any(x for x in seq if x == 59) and any(x for x in seq if x == 60) and any(x for x in seq if x == 61) and any(x for x in seq if x == 62) and any(x for x in seq if x == 63)):
            return '6'
    elif((s == 65 and e == 79) or (s == 65 and e == 80)):
        if(any(x for x in seq if x == 65) and any(x for x in seq if x == 66) and any(x for x in seq if x == 67) and any(x for x in seq if x == 68) and any(x for x in seq if x == 69) and any(x for x in seq if x == 70) and any(x for x in seq if x == 71) and any(x for x in seq if x == 72) and any(x for x in seq if x == 73) and any(x for x in seq if x == 74) and any(x for x in seq if x == 75) and any(x for x in seq if x == 76) and any(x for x in seq if x == 77) and any(x for x in seq if x == 78) and any(x for x in seq if x == 79)):
            return '7'
    elif((s == 81 and e == 86) or (s == 81 and e == 87)):
        if(any(x for x in seq if x == 81) and any(x for x in seq if x == 82) and any(x for x in seq if x == 83) and any(x for x in seq if x == 84) and any(x for x in seq if x == 85) and any(x for x in seq if x == 86)):
            return '8'
    elif((s == 88 and e == 96) or (s == 88 and e == 97)):
        if(any(x for x in seq if x == 88) and any(x for x in seq if x == 89) and any(x for x in seq if x == 90) and any(x for x in seq if x == 91) and any(x for x in seq if x == 92) and any(x for x in seq if x == 93) and any(x for x in seq if x == 94) and any(x for x in seq if x == 95) and any(x for x in seq if x == 96)):
            return '9'
    elif((s == 98 and e == 109) or (s == 98 and e == 110)):
        if(any(x for x in seq if x == 98) and any(x for x in seq if x == 99) and any(x for x in seq if x == 100) and any(x for x in seq if x == 101) and any(x for x in seq if x == 102) and any(x for x in seq if x == 103) and any(x for x in seq if x == 104) and any(x for x in seq if x == 105) and any(x for x in seq if x == 106) and any(x for x in seq if x == 107) and any(x for x in seq if x == 108) and any(x for x in seq if x == 109)):
            return 'z'
    elif((s == 111 and e == 122) or (s == 111 and e == 123)):
        if(any(x for x in seq if x == 111) and any(x for x in seq if x == 112) and any(x for x in seq if x == 113) and any(x for x in seq if x == 114) and any(x for x in seq if x == 115) and any(x for x in seq if x == 116) and any(x for x in seq if x == 117) and any(x for x in seq if x == 118) and any(x for x in seq if x == 119) and any(x for x in seq if x == 120) and any(x for x in seq if x == 121) and any(x for x in seq if x == 122)):
            return 'z'
    elif((s == 124 and e == 126)):
        return ''
    else: 
        return ''
    
def maxDelta(logdelta):
    sortlogdelta = {}
    for i in range(states_n):
        logdelta[i] = elnproduct(logdelta[i], eln(HMM[i+1][states_n+1]))
    sortlogdelta = copy.deepcopy(logdelta)
    sortlogdelta.sort()
    return sortlogdelta[states_n-1]   
        
def findMaxIdx(pList, sortedList):
    for maxi in range(sortedList.__len__()):
        if(pList[maxi] == sortedList[sortedList.__len__()-1]):
            return maxi 
    
def result_seq(seq, T):
    result = ''

    idx = 0
    sArr = {}
    idxArr = {}
    for i in range(T):
        for startS in range(13):
            if(seq[i] == startStates[startS]):
                if(i == 0):
                    sArr[idx] = seq[i]
                    idx = idx + 1
                if(i != 0 and seq[i] != seq[i-1]):
                    sArr[idx] = seq[i]
                    idxArr[idx] = i
                    idx = idx + 1
    
    idxArr[idx] = seq[T-1]
    for s in range(1, idx):
        result = result + str(identifyWord(sArr[s], seq[idxArr[s+1]-1], seq[idxArr[s]: idxArr[s+1]]))
    return result

def sylResult(seq):
    seqArr = list(seq)
    result = ''
    for i in seqArr:
        if(i == '1'):
            result = result+'one\n'
        elif(i == '2'):
            result = result+'two\n'
        elif(i == '3'):
            result = result+'three\n'
        elif(i == '4'):
            result = result+'four\n'
        elif(i == '5'):
            result = result+'five\n'
        elif(i == '6'):
            result = result+'six\n'
        elif(i == '7'):
            result = result + 'seven\n'
        elif(i == '8'):
            result = result+'eight\n'
        elif(i == '9'):
            result =  result +'nine\n'
        elif(i == 'z'):
            result = result+'zero\n'
        elif(i == 'o'):
            result = result+'oh\n'
    return result

sylIndex = 0
states_n = HMM.__len__()-2
sylB = [0] * (states_n)                      #each index has StateJ
for module in moduleSound:                   #has arr of syllables for each dictionary word
    for w in module:
        for syl in sylList:
            if(w == syl.sound and syl.sound != 'sp'):   #3 states per sound
                for i in range(sylIndex, sylIndex + 3):
                    state = stateJ()
                    state.setStateJ(syl, syl.states[i-sylIndex])
                    sylB[i] = state                  
                sylIndex = sylIndex + 3
                break
            elif(w == syl.sound and syl.sound == 'sp'):
                state = stateJ()
                state.setStateJ(syl, syl.states[0])
                sylB[sylIndex] = state
                sylIndex = sylIndex + 1
                break 

f1 = open("recognized.txt", "w")
f1.write("#!MLF!#\n")
f2 = open("result.txt", "w")
success = 0
total = 0

for root, dirs, files in os.walk("./tst", topdown = False):
    for name in files:
        f = open(os.path.join(root,name))
        s = f.name
        realVal = name[0: -4]
        print "processing %s" % f
        
        inputArr = map(lambda x: x.strip(), f.readlines())
        txtInfo = map(int, inputArr[0].split())
        T = txtInfo[0]  #T is input length
        
        logdelta = [0.0]*T
        for delta_i in range(T):
            logdelta[delta_i] = [0.0] * states_n
        sai = [0]*(T)                 #sai[t][j]//input[t] - states
        identified_idx = 0
        final_q = [0]*T
        
        for sai_t in range(T):
            sai[sai_t] = [0]*states_n
            
        input1 = map(float, inputArr[1].split())
        for j in range(states_n):
            logdelta[0][j] = elnproduct(eln(HMM[1][j+1]), sylB[j].state.functionB(input1))
        
        for x in range(1, T):
            inputX = map(float, inputArr[x+1].split())
            
            for j in range(states_n):
                logdelta[x][j] = -1111111000000
                for i in range(states_n):
                    if(logdelta[x][j] < elnproduct(logdelta[x-1][i], eln(HMM[i+1][j+1]))):
                        logdelta[x][j] = elnproduct(logdelta[x-1][i], eln(HMM[i+1][j+1]))
                        sai[x][j] = i+1
                logdelta[x][j] = elnproduct(logdelta[x][j], sylB[j].state.functionB(inputX))
            
        finaldelta = {}
        finaldelta[T-1] = maxDelta(logdelta[T-1])
        sortfinal = {}
        sortfinal = copy.deepcopy(logdelta[T-1])
        sortfinal.sort()
        final_q[T-1] = findMaxIdx(logdelta[T-1], sortfinal)   #index of max in HMM real-state idx
        for t in range(T-2, -1, -1):
            final_q[t] = sai[t+1][final_q[t+1]-1]
        
        result = result_seq(final_q, T)
        if realVal == result:
            booleanR = 'O'
            success = success + 1
        else:
            booleanR = 'X'
        total = total + 1 
        
        f2.write(realVal + "    " + result +"    "+ booleanR + '\n')
        f1.write('"'+s[2:-3] +'txt"\n')
        f1.write(str(sylResult(result)))
        f1.write('.\n')
        
        
f1.close()  
f2.close()
print "success: "+ str(success) + "      total: "+str(total)
