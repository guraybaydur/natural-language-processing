import conllu
from conllu import parse

data_dir = '../../../datasets/ud-treebanks-v2.7/UD_Turkish-BOUN/'
train_data = 'tr_boun-ud-train.conllu'

general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"

corpus = set()
corpus2 = []

i = 0
#document_limit = 1000
with open(data_dir + train_data, 'r', encoding='utf8') as f:
    for tokenlist in conllu.parse_incr(f):
        for token in tokenlist:
            if token["upos"] != "PUNCT":
                i += 1
                corpus.add(token["form"])
                corpus2.append(token["form"])

#print(corpus)
print("num of words: " + str(i))
print("num of unique words: " + str(len(corpus)))
print("len of all wordslist: " + str(len(corpus2)))


output_file_name = general_folder_path + "corpora/unique_words_for_stopwords_elimination.txt"
f2 = open(output_file_name, "a")

for word in corpus:
    f2.write(word + "\n")
f2.close()

output_file_name2 = general_folder_path + "corpora/all_words_for_stopwords_elimination.txt"
f3 = open(output_file_name2, "a")

for word in corpus2:
    f3.write(word + "\n")
f3.close()


# f2.write(token["form"] + "\n")
# f2.close()

# text = tokenlist.metadata['text']  # get the sentence
# print(text)
