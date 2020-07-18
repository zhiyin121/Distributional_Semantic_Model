import os
import spacy

lines = ''
pos_list = ['ADJ', 'NOUN', 'VERB', 'ADV']
dict_remain = {}
str_remain = ''

path = os.getcwd()
f = open(path + "/data/in/remain_word.txt", encoding="utf-8")


nlp = spacy.load('en_core_web_sm')
for line in f.readlines():
    line = line.replace('\n', '')

    doc = nlp(line)
    for token in doc:
        pos = token.pos_
        if pos in pos_list:
            dict_remain[token.text] = token.pos_
            #print(dict_remain)
print(len(dict_remain))


j = open(path + "/data/in/reduce_remain_word.txt", "w", encoding="utf-8")
remain_word = ''
for key in dict_remain:
    str_remain += key + '\n'
    #print(str_remain)
j.write(str_remain)

