import os
import spacy
import string
from string import punctuation

loop = ['K']

punct_list = ['’', '‘', '—', '…', '-PRON-', '\'s', ' ', ';', ':', ''] + list(punctuation)
grammatical_relations = {'nsubj':5, 'csubj':5, 'obj':4, 'dobj':4, 'pobj':4,
                         'agent':3, 'advmod':2, 'amod':2, 'nounmod':2,
                         'npmod':2, 'nummod':2, 'quantmod':2 }
sm = {}
rule = {}
for letter in loop:
    sm_file = ''
    print(letter)
    index = 0
    path = os.getcwd()
    with open(path + '/' + letter + '.txt', "r", encoding="utf-8") as f:
        # each .xml file as a paragraph   
        for line in f.readlines():
            #print(line[0])
            nlp = spacy.load('en_core_web_sm')
            nlp.max_length = len(line)
            sent = nlp(line)
            for token in sent:
                syntax = "{0} {1} {2}".format(token.lemma_, token.head.lemma_,token.dep_)      
                list = syntax.split(' ')
                #print(list)
                if list[0] not in punct_list:
                    if list[1] not in punct_list:
                        if len(list) == 3:
                            if list[2] != 'ROOT':
                                #print(syntax)
                                # extract sm items 
                                k = syntax
                                if k in sm:
                                    if grammatical_relations.__contains__(list[2]) is True:
                                        sm[k] += grammatical_relations.get(list[2])
                                    else:
                                        sm[k] += 1     
                                else:
                                    if grammatical_relations.__contains__(list[2]) is True:
                                        sm[k] = grammatical_relations.get(list[2])
                                    else:
                                        sm[k] = 1
            index += 1
            print(index)
            #if index > 6:
            #    break
            #print(len(sm))
                                
            
                        # Frequency of statistical dependencies
                        #if list[4] not in rule:
                        #    rule[list[4]] = 1
                        #else:
                        #    rule[list[4]] += 1
        
        
    #print(rule)
    #print(sm)


    for key, value in sm.items():
        sm_file += key + ' ' + str(value) + '\n'
   
    sm_file_bytes = str.encode(sm_file)        
    a = os.open(path + '/' + letter + '_sm.txt', os.O_RDWR|os.O_CREAT)
    os.write(a, sm_file_bytes)
    os.close(a)

    '''
    fd = os.open(path + '/A_sm.txt',os.O_RDWR)
    ret = os.read(fd,16)
    print(ret)
    os.close(fd)
    print('finish close')
    '''


