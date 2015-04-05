import math
import copy

def changeKey(states, newIdx):
    i = 0
    newKey = {}
    for key in states.keys():
        newKey[key] = newIdx+i
        i = i+1
    
    temp = copy.deepcopy(states)
    changed = {}
    for key, value in temp.items():
        changed[newKey[key]] = value
    return changed

def eexp(x):
    if(x == -1111111000000): #x == 0
        return 0
    else:
        return math.exp(x)
    
def eln(x):
    if(x == 0):
        return -1111111000000
    elif(x > 0):
        return math.log(x)
    
def elnsum(eln_x, eln_y):
    if eln_x == -1111111000000 or eln_y == -1111111000000:
        if(eln_x == -1111111000000):
            return eln_y
        else:
            return eln_x
    else:
        if(eln_x > eln_y):
            return eln_x + eln(1 + eexp(eln_y - eln_x))
        else:
            return eln_y + eln(1 + eexp(eln_x - eln_y))

def calNorDis(x, mean, var):
    result = 0
    for i in range(39):
        result = result + ((x[i]-mean[i])**2)/var[i] 
    result = -(result/2)
    return result

class Mixture:
    def __init__(self, weight, stateNum, mixNum):
        self.meanVec = []
        self.varVec = []
        self.sdVec = [0.0]*39
        self.stateNum = stateNum
        self.mixNum = mixNum
        self.weight = weight
        self.bResult = 0
        
    def setMixData(self, meanVec, varVec):
        self.meanVec = meanVec
        self.varVec = varVec
        for i in range(0, 39):
            self.sdVec[i] = math.sqrt(varVec[i])
        
class State:
    def __init__(self):
        self.mixtures = []
        self.stateIdx = -1
        
    def setIdx(self, stateIdx):
        self.stateIdx = stateIdx
        
    def functionB(self, inputX):        #input is [39]vector
        mixLen = self.mixtures.__len__()
        self.cal = 1
        temp = {}
        if(mixLen != 0):
            for g in range(mixLen):        
                for sd in self.mixtures[g].sdVec:
                    self.cal = self.cal * sd            
                temp[g] = eln((eexp(calNorDis(inputX, self.mixtures[g].meanVec, self.mixtures[g].varVec)) * (self.mixtures[g].weight) )/(math.sqrt(2*math.pi) *self.cal))                       
                self.cal = 1
        result = -1111111000000
        for g in range(mixLen):
            result = elnsum(result, temp[g])
        return result
            
class Syllable:
    def __init__(self, snd):
        self.sylIdx = 0
        self.states = []
        self.sound = snd
    def setSylIdx(self, idx):
        self.sylIdx = idx
    def aArr_Pi(self, aArr, pi):
        self.aArr = aArr
        self.pi = pi
    """     
    def setStartState(self, stateIdx):
        self.states = changeKey(self.states, stateIdx)    
    """  
    def functionB(self, stateNum, inputX):        #input is [39]vector
        return self.states[stateNum].functionB(inputX)
   
    def getPi(self):
        return self.pi
    def getAArr(self):
        return self.aArr
