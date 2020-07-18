import os
import re


list = []

new_line = ''

path = os.getcwd()
f = open(path + "/data/in/stem_affix/stem_affix.txt", encoding="utf-8")
j = open(path + "/data/in/stem_affix/stem_affix_format.txt", "w", encoding="utf-8")

remain_word = open(path + "/data/in/remain_word.txt", "r", encoding="utf-8")
read_remain_word = remain_word.read()
print(read_remain_word)


for line in f.readlines():
    line = line.replace('\n', '')
    pair = line.split('	')
    #print(pair)

    if len(pair[2]) > 1:
        if pair[2][0] == 'x':
            #print(pair)
            stem = pair[1].split('+')
            #print(stem)
            if stem[1] in read_remain_word:
                new_line +=  stem[0] + '-' + '\t' + stem[1] + '\t'\
                           + pair[2][1] + '\t' + pair[0] + '\t'\
                           + pair[3] + '\n'
            

       
        elif pair[2][1] == 'x':
            stem = pair[1].split('+')
            #print(stem)
            if stem[0] in read_remain_word:
                new_line += '-'+ stem[1] +'\t' + stem[0] + '\t'\
                           + pair[2][0] + '\t' + pair[0] + '\t'\
                           + pair[3] + '\n'

        else:
            #Combined word
            pass
print(new_line)
j.write(new_line)
   
    
