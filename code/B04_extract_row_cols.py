import os
path = os.getcwd()


dict_remain_word = {}
with open (path + '/data/in/reduce_remain_word.txt', "r", encoding="utf-8") as f:
    for line in f.readlines():
        line = line.replace('\n', '')
        dict_remain_word[line] = 0
print(len(dict_remain_word))


#remain only NOUN, VERB, ADV, ADJ from 'reduce_remain_word.txt' in row
dict_new_sm = {}
dict_new_row = {}
dict_new_cols = {}
with open (path + '/Material/baseline_sm.txt', "r", encoding="utf-8") as j:
    for line in j.readlines():    
        line = line.replace('\n', '')
        list = line.split(' ')
        key = list[0] + ' ' + list[1]
        value = int(list[2])

        if list[0] in dict_remain_word:
            if list[1] in dict_remain_word:
                dict_new_row[list[0]] = 0
                dict_new_cols[list[1]] = 0
                dict_new_sm[key] = value
                
print(len(dict_new_row))
print(len(dict_new_cols))
print(len(dict_new_sm))

'''
#01_new row
str_new_row = ''
for key in dict_new_row:
    str_new_row += key + '\n'
    
str_new_row = str.encode(str_new_row)        
r = os.open(path + '/data/in/space_row.txt', os.O_RDWR|os.O_CREAT)
os.write(r, str_new_row)
os.close(r)
print('space_row.txt implementing finished')


#02_new cols
str_new_cols = ''
for key in dict_new_cols:
    str_new_cols += key + '\n'
    
str_new_cols = str.encode(str_new_cols)        
c = os.open(path + '/data/in/space_cols.txt', os.O_RDWR|os.O_CREAT)
os.write(c, str_new_cols)
os.close(c) 
print('space_cols.txt implementing finished')
'''

#03_new sm
str_new_sm = ''
for key in dict_new_sm:
    str_new_sm += key + ' ' + str(dict_new_sm[key]) + '\n'
    
str_new_sm = str.encode(str_new_sm)        
s = os.open(path + '/data/in/space_sm.txt', os.O_RDWR|os.O_CREAT)
os.write(s, str_new_sm)
os.close(s)
print('space_sm.txt implementing finished')
