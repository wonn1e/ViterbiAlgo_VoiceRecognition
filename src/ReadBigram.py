f = open('bigram.txt') 

lines = map(lambda x: x.strip(), f.readlines())

bigram = []                       # bigram = 12*12  // bigram information
for x in range(12):
    bigram.append([0.0]*12)
    
def index(n):
    return{
        'oh' : 0,
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
        'zero' : 10,
        '<s>' : 11
    }[n]
    
for line in lines:
    arr = line.split()
    bigram[index(arr[0])][index(arr[1])] = arr[2]