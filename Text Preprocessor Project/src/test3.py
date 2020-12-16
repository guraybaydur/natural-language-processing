# import math
#
# print(round(math.log(14), 2))
#
# emptySet = set(['guray'])
# print(emptySet)
# emptySet.add('ali')
# print(emptySet)
# emptySet.add('Ali')
# print(emptySet)
#
# print('\'')

general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"
f = open(general_folder_path + "dunya/168_tokenized.txt", "r")
document = f.readlines()

punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"', "\'", ".", ",", "$", "/", "`"]

corpus = set()

i=0

for line in document:
    stripped_token = line.strip()
    if stripped_token not in punctuations:
        i+=1
        corpus.add(stripped_token)
        print(len(corpus))
        print(stripped_token)



