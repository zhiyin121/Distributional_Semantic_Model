Toolkit: DISSECT

A01_extract_from_xml.py
The xml file downloaded from ukWaC is decomposed into a paragraph by folder.
(url: http://ota.ox.ac.uk/desc/2554)
output: a series of (1).txt files containing paragraphs (utf-8)


A02_build_space.py
Use the python package Spacy to do dependency parsing on all tokens. Paths of length is 1. Then add them to a dictionary. The token and its head, and the syntactic relationship between them as the key, the frequency of occurrence as the value. The syntactic relationship has a weighting distinction that affects the number of value.
output: a series of (2).txt files containing "target words, syntactic elements, syntactic relationship, frequency" (bytes)


A03_delete_blank.py
Delete the line whose target word and syntax element are empty in the file.


A04_combine_space.py
Put all the (2).txt files into a dictionary. The key is "target words, syntactic elements, syntactic relationship", and the value is the cumulative sum of the frequencies of the same key.
output: baseline_sm.txt


B01_reduce_word.py
Extract all the words (rows & cols) from basic space (space_sm.txt)  to a dictionary as key and the frequency of them as value. Filter out the words with a frequency lower than 3, keep words that appear more frequently than twice.
Output: remain_word.txt


B02_reduce_remain_word.py
Retain only words whose Part-of-Speech are Nouns, Verbs, Adjectives and Adverbs
output: reduce_remain_word.txt


CELEX
Upload 'reduce_remain_word.txt' to the corpus and extract the stem of the word. Remove words whose word form are consistent with stem. Keep words with at least one affix.
output: stem_affix.txt


B03_stem_affix.py
Turn the data form into "Affix, stem, pos of stem, original word, pos of original word"
output: stem_affix_format.txt


B04_extract_row_cols.py
Reduce the original space 'baseline_sm.txt'. Extract the word list from 'reduce_remain_word.txt' and verify that both the target word and syntactic element of each line in the space are in the list. If not, delete the entire line.
output: space_row.txt, space_cols.txt, space_sm.txt


B05_affix_pair.py
Turn file 'stem_affix_format.txt' into .pkl format