import io
import os
import re
import spacy
import string



file_name = []


letter = list(string.ascii_uppercase)
num = [0,1,2,3,4,5,6,7,8,9]
combine = num + letter

'''
for j in range(len(combine)):
    file_name.append(letter[0]+str(combine[j]))
'''
path_a = os.getcwd()
a = open(path_a + '/K.txt','a', encoding="utf-8")
print(path_a + '/K.txt')
index = 0
for k in combine:
    article = ''
    for j in combine:
        path = os.getcwd()
        path = str(path+"/ukWaC/2554/download/Texts/K/K"+ str(k) + '/' + 'K' + str(k) + str(j) + ".xml")
        #print("C/C"+ str(k) + '/' + 'C' + str(k) + str(j) + ".xml")
        try:
            f = open(path, encoding="utf-8")
            for line in f.readlines():
                if line[0:5] == "<s n=":
                    word = re.compile(r'[>](.*?)[<]', re.S)
                    sentence = re.findall(word, line)
                    sentence = ''.join(sentence)
                    article += sentence + ' '
            article += '\n'
            index += 1
            print(index)
        except FileNotFoundError:
            pass
    a.write(article)
#print(article)


'''
for k in combine:
    path = os.getcwd()
    path = str(path+"/ukWaC/2554/download/Texts/A/A0/" + "A0" + str(k) +".xml")
    print("A0/" + "A0" + str(k) +".xml")
    try:
        f = open(path, encoding="utf-8")
        for line in f.readlines():
            if line[0:5] == "<s n=":
                word = re.compile(r'[>](.*?)[<]', re.S)
                sentence = re.findall(word, line)
                sentence = ''.join(sentence)
                article += sentence + ' '
        article += '\n'
    except FileNotFoundError:
        pass
print(article)
'''

