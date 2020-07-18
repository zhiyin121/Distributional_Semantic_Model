import os
import spacy

loop = ['D', 'B', 'E', 'J', 'G', 'F', 'C', 'H', 'K']

baseline = ''

path = os.getcwd()

#add other sm into baseline
dict_exit = {}
with open (path + '/A_sm.txt', "r", encoding="utf-8") as j:
    for line_exit in j.readlines():
        line_exit = line_exit.replace('\n', '')
        list_exit = line_exit.split(' ')
        if len(list_exit) != 4:
            #print(list_exit)
            pass
        else:
            key = list_exit[0] + ' ' + list_exit[1]
            value = int(list_exit[3])
            dict_exit[key] = value
    print(len(dict_exit))
    j.close()


for letter in loop:           
    with open(path + '/' + letter + '_sm.txt', "r", encoding="utf-8") as f:
        for line_new in f.readlines():
            line_new = line_new.replace('\n', '')            
            list_new = line_new.split(' ')
            if len(list_new) != 4:
                pass
            else:
                key_new = list_new[0] + ' ' + list_new[1]
                value_new = int(list_new[3])
                if key_new in dict_exit:
                    dict_exit[key_new] += value_new
                else:
                    dict_exit[key_new] = value_new
    print(letter)
    print(len(dict_exit))
    f.close()

#print(dict_exit)

    
num_word = {}
remain_word = {}
dict_new = {}
sm_baseline = ''
row_baseline = ''
cols_baseline = ''

'''
#reduce items by the frequency of co-occurrence
for k in dict_exit:
    if dict_exit[k] > 10:
        dict_new[k] = dict_exit[k]
    else:
        pass
                
print(len(dict_new))
'''
dict_new = dict_exit

for key, value in dict_new.items():
    sm_baseline += key + ' ' + str(value) + '\n'
    row_baseline += key.split(' ')[0] + '\n'
    cols_baseline += key.split(' ')[1] + '\n'
         
sm_baseline = str.encode(sm_baseline)        
s = os.open(path + '/baseline_sm.txt', os.O_RDWR|os.O_CREAT)
os.write(s, sm_baseline)
os.close(s)

row_baseline = str.encode(row_baseline)        
r = os.open(path + '/baseline_row.txt', os.O_RDWR|os.O_CREAT)
os.write(r, row_baseline)
os.close(r)

cols_baseline = str.encode(cols_baseline)        
c = os.open(path + '/baseline_cols.txt', os.O_RDWR|os.O_CREAT)
os.write(c, cols_baseline)
os.close(c)

