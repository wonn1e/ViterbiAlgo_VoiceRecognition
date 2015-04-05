f = open('result.txt')
lines = map(lambda x: x.strip(), f.readlines())
total = lines.__len__()
success = 0
f1 = open('failure.txt', 'w')
for line in lines:
    arr = line.split()
    if(arr.__len__() == 3):
        if(arr[2] == 'O'):
            success = success+1
        else:
            f1.write(line+'\n')
    else:
        f1.write(line+'\n')
    
f1.close()    
print success
print total