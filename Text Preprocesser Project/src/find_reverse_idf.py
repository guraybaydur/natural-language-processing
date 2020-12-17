import math
import re
import os

general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"
punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"', "\'", ".", ",", "$", "/", "`"]
corpus = set()
number_of_documents = 0

for folder_name in os.listdir(general_folder_path):
    if folder_name not in [".DS_Store", "corpora"]:
        # i = 0
        print(folder_name)
        for file in os.listdir(general_folder_path + folder_name):
            regex = r'^[0-9]+_tokenized.txt$'
            if re.search(regex, file):
                number_of_documents += 1
                f = open(general_folder_path + folder_name + "/" + file, "r")
                document = f.readlines()
                for line in document:
                    stripped_token = line.strip()
                    if stripped_token not in punctuations:
                        corpus.add(stripped_token)
            #     i += 1
            # if i == 1:
            #     break
# output_file_name = general_folder_path + "corpora/corpus_for_stopword_elimination.txt"
# f2 = open(output_file_name, "a")
#
# for word in corpus:
#     f2.write(word + "\n")
# f2.close()
print(corpus)
print(len(corpus))
print("Number of documents: " + str(number_of_documents))

reverse_idf_scores = {}
for word in corpus:
    #if word in ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']:
    if word == "yapılan":
        document_frequency = 0
        for folder_name in os.listdir(general_folder_path):
            if folder_name not in [".DS_Store", "corpora"]:
                print(folder_name)
                for file in os.listdir(general_folder_path + folder_name):
                    regex = r'^[0-9]+_tokenized.txt$'
                    if re.search(regex, file):
                        f = open(general_folder_path + folder_name + "/" + file, "r")
                        document = f.readlines()
                        for line in document:
                            stripped_token = line.strip()
                            if word == stripped_token:
                                print("Word: " + word + " found in document: " + general_folder_path + folder_name + "/" + file)
                                document_frequency += 1
                                break
        reverse_idf_scores[word] = round(math.log(document_frequency / number_of_documents, 10), 5)
print(reverse_idf_scores)