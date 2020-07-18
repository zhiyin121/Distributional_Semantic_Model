import os

dict_token = {}
path = os.getcwd()
new_text = ''
f = open(path + "/data/in/space_sm.txt", encoding="utf-8")

# extract all the words from rows and cols to a dictionary
for line in f.readlines():
    line = line.replace('_', ' ')
    line = line.replace('\n', '')
    pair = line.split(' ')
    #print(pair)
    if pair[0] in dict_token:
        dict_token[pair[0]] += 1
    else:
        dict_token[pair[0]] = 1
    #print(dict_token)


# reduce words whose frequency < 3
j = open(path + "/data/in/remain_word.txt", "w", encoding="utf-8")
remain_word = ''
for key, value in dict_token.items():
    if value > 2:
        remain_word += key + '\n'
j.write(remain_word)






        
        
