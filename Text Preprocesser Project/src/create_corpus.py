import re
import os

general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"
punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"', "\'", ".", ",", "$", "/", "`"]
corpus = set()

for folder_name in os.listdir(general_folder_path):
    if folder_name not in [".DS_Store", "corpora"]:
        # i = 0
        print(folder_name)
        for file in os.listdir(general_folder_path + folder_name):
            regex = r'^[0-9]+_tokenized.txt$'
            if re.search(regex, file):
                f = open(general_folder_path + folder_name + "/" + file, "r")
                document = f.readlines()
                for line in document:
                    stripped_token = line.strip()
                    if stripped_token not in punctuations:
                        corpus.add(stripped_token)
            #     i += 1
            # if i == 1:
            #     break
output_file_name = general_folder_path + "corpora/corpus_for_stopword_elimination.txt"
f2 = open(output_file_name, "a")

for word in corpus:
    f2.write(word + "\n")
f2.close()

print(len(corpus))

