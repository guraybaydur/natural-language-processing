import conllu
import math
import time

start_time = time.time()

corpus_dir = "../../../datasets/42bin_haber_v3/news/corpora/"
corpus_file = "unique_words_for_stopwords_elimination.txt"

corpus_dir2 = "../../../datasets/42bin_haber_v3/news/corpora/"
corpus_file2 = "all_words_for_stopwords_elimination.txt"

# data_dir = '../../../datasets/ud-treebanks-v2.7/UD_Turkish-BOUN/'
# train_data = 'tr_boun-ud-train.txt'

f2 = open(corpus_dir + corpus_file, "r")
document = f2.readlines()

unique_words = []

for word in document:
    stripped_word = word.strip()
    unique_words.append(stripped_word)

print(unique_words)
print(str(len(unique_words)))

all_words = []

f = open(corpus_dir2 + corpus_file2, "r")
document = f.readlines()

for word in document:
    stripped_word = word.strip()
    all_words.append(stripped_word)

print(unique_words)
print(str(len(unique_words)))
print(str(len(all_words)))

reverse_tf_scores = {}

for unique_word in unique_words:
    if unique_word == "acaba":
        term_frequency = all_words.count(unique_word)
        print("unique word: " + unique_word + "'s count is: " + str(term_frequency))
        reverse_tf_score = (1 / (1 + round(math.log(term_frequency, 10), 5)))
        reverse_tf_scores[unique_word] = reverse_tf_score

print(reverse_tf_scores)

# reverse_tf_scores = 0

# for unique_word in unique_words:
#    term_frequency=0

#   (1 / (1 + round(math.log(term_frequency, 10), 5)))
#
# reverse_tf_idf_scores = {}
# i = 0
# for word in document:
#     count = 0
#     i += 1
#     document_frequency = 0
#     stripped_token = word.strip()
#     number_of_documents = 0
#     term_frequency = 0
#     with open(data_dir + train_data, 'r', encoding='utf8') as f:
#         for tokenlist in conllu.parse_incr(f):
#             text = tokenlist.metadata['text']
#             print(text)
#             count += text.count(word)
#             print("word: " + word)
#             print("word count: " + str(count))
#             # document_frequency_updated = False
#             # number_of_documents += 1
#             # for token in tokenlist:
#             #     if token["upos"] != "PUNCT":
#             #         if token["form"] == stripped_token:
#             #             if not document_frequency_updated:
#             #                 document_frequency_updated = True
#             #                 document_frequency += 1
#             #             term_frequency += 1
#
#     # print("word: " + word)
#     # print("math.log(term_frequency, 10): " + str(math.log(term_frequency, 10)))
#     # print("term_frequency: " + str(term_frequency))
#     # print("round(math.log(term_frequency, 10), 5): " + str(round(math.log(term_frequency, 10), 5)))
#     # print("document_frequency: " + str(document_frequency))
#     # print("number_of_documents: " + str(number_of_documents))
#     # print("round(math.log(document_frequency / number_of_documents, 10), 5): " + str(
#     #     round(math.log(document_frequency / number_of_documents, 10), 5)))
#     # reverse_tf_idf_scores[word] = (1 / (1 + round(math.log(term_frequency, 10), 5))) * round(
#     #     math.log(document_frequency / number_of_documents, 10), 5)
#     if i == 1:
#         break

print("--- %s seconds ---" % (time.time() - start_time))
