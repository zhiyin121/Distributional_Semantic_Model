import pickle
import os
path = os.getcwd()

pair = []
s = set()
with open(path + '/data/in/stem_affix/stem_affix_format.txt') as file:
    line = file.readline()
    while line:
        split = line.split('\t')
        #print(pair)
        pair.append((split[0], split[1], split[3]))
        #print(pair)
        if split[3] in s:
            print(split)
        else:
            s.add(split[3])
        line = file.readline()
        
f = open(path + '/data/out/dpair.pkl', 'wb')
pickle.dump(pair, f)
