import conllu

if __name__ == '__main__':

    data_dir = '../../../datasets/parseme_corpus_tr-master/'
    filename_begin = "train_00"
    filename_end = ".cupt"

    mwe_lexicon = set()

    for j in range(1, 5):
        print(filename_begin + str(j) + filename_end)
        with open(data_dir + filename_begin + str(j) + filename_end, 'r', encoding='utf8') as f:
            for tokenlist in conllu.parse_incr(f):
                visited_ids = []
                for i in range(0, len(tokenlist)):
                    # dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'parseme:mwe'])
                    parseme_column = tokenlist[i]['parseme:mwe']
                    token_id = tokenlist[i]['id']
                    if 'LVC.full' in parseme_column and token_id not in visited_ids:
                        visited_ids.append(token_id)
                        mwe = [tokenlist[i]['form']]
                        search_nums = [parseme_column.split(':')[0]]
                        while i+1 != len(tokenlist) and search_nums[0] not in tokenlist[i + 1]['parseme:mwe']:
                            if str(int(search_nums[0]) + 1) in tokenlist[i + 1]['parseme:mwe']:
                                mwe.append(tokenlist[i + 1]['form'])
                                visited_ids.append(tokenlist[i + 1]['id'])
                            i += 1
                        if len(mwe) > 1:
                            mwe[1] += " " + tokenlist[i + 1]['form']
                        if i+1 != len(tokenlist):
                            mwe[0] += " " + tokenlist[i + 1]['form']
                        mwe_lexicon.update(mwe)

    for j in range(1, 5):
        print(filename_begin + str(j) + filename_end)
        with open(data_dir + filename_begin + str(j) + filename_end, 'r', encoding='utf8') as f:
            for tokenlist in conllu.parse_incr(f):
                visited_ids = []
                for i in range(0, len(tokenlist)):
                    # dict_keys(['id', 'form', 'lemma', 'upos', 'xpos', 'feats', 'head', 'deprel', 'deps', 'misc', 'parseme:mwe'])
                    parseme_column = tokenlist[i]['parseme:mwe']
                    token_id = tokenlist[i]['id']
                    if ':VID' in parseme_column and token_id not in visited_ids:
                        visited_ids.append(token_id)
                        mwe = [tokenlist[i]['form']]
                        search_nums = [parseme_column.split(':')[0]]
                        while i+1 != len(tokenlist) and search_nums[0] not in tokenlist[i + 1]['parseme:mwe']:
                            if str(int(search_nums[0]) + 1) in tokenlist[i + 1]['parseme:mwe']:
                                mwe.append(tokenlist[i + 1]['form'])
                                visited_ids.append(tokenlist[i + 1]['id'])
                            i += 1
                        if len(mwe) > 1:
                            mwe[1] += " " + tokenlist[i + 1]['form']
                        if i+1 != len(tokenlist):
                            mwe[0] += " " + tokenlist[i + 1]['form']
                        mwe_lexicon.update(mwe)

    mwe_lexicon_copy=mwe_lexicon.copy()
    for elem in mwe_lexicon_copy:
        if " " not in elem:
            mwe_lexicon.remove(elem)
        for suffix in [" lı"," li"," lu"," lü"]:
            if suffix in elem:
                #print("suffix: " + suffix + " removed from " + elem )
                mwe_lexicon.remove(elem)

    output_file_name = "../vocabulary/verbal_mwe_lexicon.txt"
    f = open(output_file_name, "a")
    for mwe in mwe_lexicon:
        f.write(mwe + "\n")
    f.close()



    print(mwe_lexicon)
    print(len(mwe_lexicon))
