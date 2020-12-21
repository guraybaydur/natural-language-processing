# import math
# print(round(math.log(4000/41992,10),5))
# #print(round(math.log(3213/41992), 2))
# emptySet = set(['guray'])
# print(emptySet)
# emptySet.add('ali')
# print(emptySet)
# emptySet.add('Ali')
# print(emptySet)
# print('\'')
#
# list = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu', 'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep', 'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl', 'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz', 'şu', 'tüm', 've', 'veya', 'ya', 'yani']
# print(str(len(list)))
#
# new_list = ['aynı', 'üç', 'tek', 'bütün', 'karşı', 'yer', 'kendi', 'yıl', 'bile', 'önce', 'ki', 'şey', 'yeni', 'hiç', '1', 'iyi', 'ya', 'ilk', 'iki', 'gün', 'ama', 'zaman', 'büyük', 'diye', 'ne', 'sonra', 'kadar', 'her', 'o', 'en', 'ile', 'daha', 'gibi', 'çok', 'için', 'da', 'de', 'bu', 've', 'bir']
# count = 0
# for elem in new_list:
#     if elem in list:
#         count+=1
#
# print(count)
#
#
# # general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haber_v3/news/"
# # f = open(general_folder_path + "dunya/168_tokenized.txt", "r")
# # document = f.readlines()
# #
# # punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"', "\'", ".", ",", "$", "/", "`"]
# #
# # corpus = set()
# #
# # i=0
# #
# # for line in document:
# #     stripped_token = line.strip()
# #     if stripped_token not in punctuations:
# #         i+=1
# #         corpus.add(stripped_token)
# #         print(len(corpus))
# #         print(stripped_token)
#
#
#
import conllu

if __name__ == '__main__':

    data_dir = '../../../datasets/parseme_corpus_tr-master/'
    filename_begin = "train_00"
    filename_end = ".cupt"

    filename = "train_001.cupt"

    mwe_lexicon = set()

    for j in range(1, 5):
        print(filename_begin + str(j) + filename_end)

        with open(data_dir + filename_begin + str(j) + filename_end, 'r', encoding='utf8') as f:
            for tokenlist in conllu.parse_incr(f):
                for i in range(0, len(tokenlist)):
                    mwe = ""
                    # dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'parseme:mwe'])
                    if 'LVC.full' in tokenlist[i]['parseme:mwe']:
                        # print(tokenlist[i]['parseme:mwe'])
                        mwe = tokenlist[i]['form'] + " "
                        if i + 1 < len(tokenlist):
                            mwe += tokenlist[i + 1]['form']
                        # print(mwe + "\n")
                        mwe_lexicon.add(mwe)

        with open(data_dir + "dev.cupt", 'r', encoding='utf8') as f:
            for tokenlist in conllu.parse_incr(f):
                for i in range(0, len(tokenlist)):
                    mwe = ""
                    # dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'parseme:mwe'])
                    if 'LVC.full' in tokenlist[i]['parseme:mwe']:
                        # print(tokenlist[i]['parseme:mwe'])
                        mwe = tokenlist[i]['form'] + " "
                        if i + 1 < len(tokenlist):
                            mwe += tokenlist[i + 1]['form']
                        # print(mwe + "\n")
                        mwe_lexicon.add(mwe)

        with open(data_dir + "test.cupt", 'r', encoding='utf8') as f:
            for tokenlist in conllu.parse_incr(f):
                for i in range(0, len(tokenlist)):
                    mwe = ""
                    # dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'parseme:mwe'])
                    if 'LVC.full' in tokenlist[i]['parseme:mwe']:
                        # print(tokenlist[i]['parseme:mwe'])
                        mwe = tokenlist[i]['form'] + " "
                        if i + 1 < len(tokenlist) and tokenlist[i + 1]['form'] not in ["\"", "", " ", ","]:
                            mwe += tokenlist[i + 1]['form']
                        # print(mwe + "\n")
                            mwe_lexicon.add(mwe)

    print(mwe_lexicon)
    print(len(mwe_lexicon))
