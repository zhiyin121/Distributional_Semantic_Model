from composes.semantic_space.space import Space
from composes.utils import io_utils
from composes.transformation.scaling.ppmi_weighting import PpmiWeighting
from composes.transformation.dim_reduction.svd import Svd
from composes.composition.lexical_function import LexicalFunction
from composes.similarity.cos import CosSimilarity
import pickle
from composes.utils import scoring_utils

import os
path = os.getcwd()


print("Building space...")
# create a space from co-occurrence counts in sparse format

try:
    my_space = io_utils.load("my_space.pkl")
except FileNotFoundError:

    my_space = Space.build(data="./data/in/spacew.sm",
                               rows="./data/in/spacew.rows",
                               cols="./data/in/spacew.cols",
                               format="sm")

    print("Applying PPMI...")
    my_space = my_space.apply(PpmiWeighting())

    print("Applying SVD...")
    my_space = my_space.apply(Svd(350))
    io_utils.save(my_space, "my_space.pkl")

print("Loading pairs...")
with open('./data/out/dpair.pkl', 'rb') as f:
    pair_data = pickle.load(f)

train_data = []
vocab = set(my_space.id2row)
for tup in pair_data:
    if tup[1] in vocab and tup[2] in vocab:
        train_data.append(tup)
'''
try:
    with open('temp_func.pkl', 'rb') as file:
        print("Loading model...")
        my_comp = pickle.load(file)
except FileNotFoundError:
'''
print("Training LexicalFunction...")
my_comp = LexicalFunction()
my_comp.train(train_data, my_space, my_space)
with open('temp_func.pkl', 'wb') as file:
    pickle.dump(my_comp, file)

print("Building composed space...")
composed_space = my_comp.compose(train_data, my_space)
# print(composed_space.id2row)
# print(composed_space.cooccurrence_matrix)

# compute similarity between two words in the space

cos_sim = {}
for pair in train_data:
    cos = my_space.get_sim(pair[1], pair[2], CosSimilarity(), space2=composed_space)
    if pair[0] in cos_sim:
        cos_sim[pair[0]].append(cos)
    else:
        cos_sim[pair[0]] = [cos]

import numpy
f = open("./data/out/sim_test_word.txt", 'w')
for key, value in cos_sim.items():
    f.write(key + '\t' + str(numpy.mean(value)) + '\n')
f.close()


#Evaluation of similarity scores


fname = "./data/in/stem_affix/gold_affix.txt"
gold = io_utils.read_list(fname, field=3)
print(gold)
print("Spearman")
print(scoring_utils.score(gold, cos_sim, "spearman"))
print("Pearson")
print(scoring_utils.score(gold, cos_sim, "pearson"))








