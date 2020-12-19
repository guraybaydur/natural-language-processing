import conllu
from conllu import parse

data_dir = '../../../datasets/parseme_corpus_tr-master/source/'
train_data = 'train.conllu'

general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"
output_file_name = general_folder_path + "corpora/corpus_for_stopword_elimination.txt"
# f2 = open(output_file_name, "a")

corpus = set()
i = 0
#document_limit = 1000
with open(data_dir + train_data, 'r', encoding='utf8') as f:
    for tokenlist in conllu.parse_incr(f):
        for token in tokenlist:
            if token["upos"] != "PUNCT":
                i += 1
                corpus.add(token["form"])

#print(corpus)
print("num of words: " + str(i))
print("num of unique words: " + str(len(corpus)))


output_file_name = general_folder_path + "corpora/corpus_for_stopword_elimination.txt"
f2 = open(output_file_name, "a")

for word in corpus:
    f2.write(word + "\n")
f2.close()


# f2.write(token["form"] + "\n")
# f2.close()

# text = tokenlist.metadata['text']  # get the sentence
# print(text)
