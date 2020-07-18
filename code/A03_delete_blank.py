import os
path = os.getcwd()

new = ''
with open(path + '/A_sm.txt', "r", encoding="utf-8") as f:
    for line in f.readlines():
        if len(line.split(' ')) < 4:
             pass
        else:
            new += line
    f.close()

    
new = str.encode(new)        
a = os.open(path + '/A_sm_new.txt', os.O_RDWR|os.O_CREAT)
os.write(a, new)
os.close(a)                
