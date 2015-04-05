import copy
from ReadHMM import sylList


class Word:
    def __init__(self):
        self.word = ''
        self.hmm = []
    def setAttribute(self, line):
        arr = line.split()
        self.word = arr[0]
        self.hmm = arr[1:]
    
class Dictionary:
    def __init__(self):
        self.words = []
    def addWord(self, word, hmm):
        self.words.append(word)
        self.words.append(hmm)


class SylHMM:
    def ___init__(self, hmm):
        self.word = ''
        self.hmm = []
            
    def setHMM(self, word, hmm):                #HMM syllable
        self.word = word
        self.hmm = hmm
        self.hmmLen = hmm.__len__()
        
        self.wordHMM = []                       
        if(self.hmmLen != 1):                   #one big vector for whole word hmm
            for index in range((3*self.hmmLen)):
                self.wordHMM.append([0.0]*((3*self.hmmLen)))
        else:                                   #<s>
            for index in range(5):
                self.wordHMM.append([0.0]*5)
                
        self.sylFromHMM = [0]*(hmm.__len__())
        for i in range(hmm.__len__()):
            for j in sylList:
                if(hmm[i] == j.sound):
                    saveSyl = copy.deepcopy(j)
                    self.sylFromHMM[i] = saveSyl
                    
        
class OneWord:
    def __init__(self):
        self.word = ''
        self.wordSylIdx = []
        self.wordHMM = []    
    def setHMM(self, word, wordHMM):
        self.word = word
        self.wordHMM = wordHMM
        self.stateNum = wordHMM.__len__() - 2

class DictionaryHMM:
    def __init__(self):
        self.dicHMM = [0]*13       #list of OneWord
        

def createWholeHMM(wordHmm, sylFromhmm):
    len = sylFromhmm.__len__()
    cnt = 1
    k = 0
    if(len != 1):
        wordHmm[0][1] = (sylFromhmm[0].getPi())[0]
        for i in range(0, (len-1) * 3):
            for j in range(3):
                if(i/3 == 0):  
                    wordHmm[i+1][(i*(k/3))+(j+1)] = (sylFromhmm[i/3].getAArr())[cnt-1][j]
                elif i/3 >= 1:
                    wordHmm[i+1][(i/3)*3 + (j+1)] = (sylFromhmm[i/3].getAArr())[cnt-1][j]
            cnt = cnt + 1
            k = k+1
                
            if(cnt == 4):
                wordHmm[i+1][3*((i+1)/3)+1] = (sylFromhmm[i/3].getAArr())[2][3] 
                cnt = 1
        # sp --> last state for all words in dictionary
        l = ((len-1) * 3)
        for j in range(0, 2):
            wordHmm[l][(l/3) *3 + (j+1)] = (sylFromhmm[(l/3)-1].getAArr())[2][3] * (sylFromhmm[l/3].getPi())[j]
            wordHmm[l+1][((l+1)/3) *3 + (j+1)] = (sylFromhmm[(l)/3].getAArr())[cnt-1][j]
            
            
    else:
        wordHmm[0][1] = 1
        for i in range(1, 4):
            for j in range(4):
                wordHmm[i][j+1] = (sylFromhmm[0].getAArr())[i-1][j]
    return wordHmm 
            
f = open('dictionary.txt')
lines = map(lambda x: x.strip(), f.readlines())

dictionaryHMM = DictionaryHMM()                         # all HMM for each word is saved in .dicHMM
dic = Dictionary()         
        
i = 0      
for line in lines:
    w = Word()
    w.setAttribute(line)
    dic.addWord(w.word, w.hmm)
    dicWord = SylHMM()                   #SylHMM create
    dicWord.setHMM(w.word, w.hmm)
    
    dictionaryWord = OneWord()
    dictionaryWord.setHMM(w.hmm, createWholeHMM(dicWord.wordHMM, dicWord.sylFromHMM))
    dictionaryHMM.dicHMM[i] = dictionaryWord
    i = i+1
