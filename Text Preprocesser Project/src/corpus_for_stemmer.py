from TurkishStemmer import TurkishStemmer
stemmer = TurkishStemmer()

corpus_dir2 = "../../../datasets/42bin_haber_v3/news/corpora/"
corpus_file2 = "all_words_for_stemmer.txt"

f2 = open(corpus_dir2 + corpus_file2, "r")
document = f2.readlines()


suffix_list = set()

for word in document:
    stripped_word = word.strip()
    print("word: " + stripped_word + " \nstem: " + stemmer.stem(stripped_word))
    suffix_list.add(stripped_word[len(stemmer.stem(stripped_word)):len(stripped_word)])
    print("\n")

new_suffix_list=set()
for item in suffix_list:
    for iter in suffix_list:
        if iter != item and item in iter:
            print("item: " + item + " in iter: " + iter)
            new_suffix_list.add(item)


new_suffix_list2=set()
for item in new_suffix_list:
    for iter in new_suffix_list:
        if iter != item and item in iter:
            print("item: " + item + " in iter: " + iter)
            new_suffix_list2.add(item)


new_suffix_list3=set()
for item in new_suffix_list2:
    for iter in new_suffix_list2:
        if iter != item and item in iter:
            print("item: " + item + " in iter: " + iter)
            new_suffix_list3.add(item)


new_suffix_list4=set()
for item in new_suffix_list3:
    for iter in new_suffix_list3:
        if iter != item and item in iter:
            print("item: " + item + " in iter: " + iter)
            new_suffix_list4.add(item)





print(suffix_list)
print(str(len(suffix_list)))
print(new_suffix_list)
print(len(new_suffix_list))
print(new_suffix_list2)
print(len(new_suffix_list2))
print(new_suffix_list3)
print(len(new_suffix_list3))
print(new_suffix_list4)
print(len(new_suffix_list4))