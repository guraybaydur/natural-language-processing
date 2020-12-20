import re
import os

import conllu


def check_suffixes(word,vocab):
    suffix_list = ['casına', 'çasına', 'cesine', 'çesine', 'sınız', 'siniz', 'sunuz', 'sünüz',
            'muş', 'miş', 'müş', 'mış', 'ken', 'sın', 'sin', 'sun', 'sün', 'lar', 'ler', 'nız', 'niz', 'nuz', 'nüz',
            'tır', 'tir', 'tur', 'tür', 'dır', 'dir', 'dur', 'dür', 'ız', 'iz', 'uz', 'üz', 'ım', 'im', 'um', 'üm',
            'dı', 'di', 'du', 'dü', 'tı', 'ti', 'tu', 'tü', 'sa', 'se', 'm', 'n', 'k', 'ndan', 'ntan', 'nden', 'nten',
            'ları', 'leri', 'mız', 'miz', 'muz', 'müz', 'nız', 'niz', 'nuz', 'nüz', 'lar', 'ler', 'nta', 'nte','nda',
            'nde', 'dan', 'tan', 'den', 'ten', 'la', 'le', 'ın', 'in', 'un', 'ün', 'ca', 'ce', 'nı', 'ni', 'nu', 'nü',
            'na', 'ne', 'da', 'de', 'ta', 'te', 'ki', 'sı', 'si', 'su', 'sü', 'yı', 'yi', 'yu', 'yü', 'ya', 'ye',
                   'y','lı', 'li', 'lu', 'lü']
    if word in vocab:
        return word

    for suffix in suffix_list:

        result = re.sub(suffix+"$", "", word)

        if word != result:
            print(result)
            return result
    return word


def greedy_stemming(word, vocab):
    suffix_list = ['casına', 'çasına', 'cesine', 'çesine', 'sınız', 'siniz', 'sunuz', 'sünüz', 'acak', 'ecek',
            'muş', 'miş', 'müş', 'mış', 'ken', 'sın', 'sin', 'sun', 'sün', 'lar', 'ler', 'nız', 'niz', 'nuz', 'nüz',
            'tır', 'tir', 'tur', 'tür', 'dır', 'dir', 'dur', 'dür', 'ız', 'iz', 'uz', 'üz', 'ım', 'im', 'um', 'üm',
            'dı', 'di', 'du', 'dü', 'tı', 'ti', 'tu', 'tü', 'sa', 'se', 'm', 'n', 'k', 'ndan', 'ntan', 'nden', 'nten',
            'ları', 'leri', 'mız', 'miz', 'muz', 'müz', 'nız', 'niz', 'nuz', 'nüz', 'lar', 'ler', 'nta', 'nte','nda',
            'nde', 'dan', 'tan', 'den', 'ten', 'la', 'le', 'ın', 'in', 'un', 'ün', 'ca', 'ce', 'nı', 'ni', 'nu', 'nü',
            'na', 'ne', 'da', 'de', 'ta', 'te', 'ki', 'sı', 'si', 'su', 'sü', 'yı', 'yi', 'yu', 'yü', 'ya', 'ye',
                   'y','lı', 'li', 'lu', 'lü']
    temp_word = None
    invocab = word in vocab
    for i in range(len(word)):
        if word[i:] in suffix_list:
            temp_word = word[:i]
            break
    if invocab and temp_word in vocab:
        return temp_word
    elif invocab and temp_word not in vocab:
        return word
    else:
        return temp_word




def generate_vocab(data_dir, filename):
    vocab = []
    with open(data_dir + filename, 'r', encoding='utf8') as f:
        for tokenlist in conllu.parse_incr(f):
            for i in tokenlist:
                if i['upos'] != 'AUX' and i['upos'] != 'PUNCT':
                    lemma = i['lemma']
                    if lemma not in vocab and lemma != '_':
                        vocab.append(lemma)
    vocab_dir = '../vocabulary/'
    name = 'lemma_vocab.txt'
    with open(vocab_dir + name, 'w', encoding='utf8') as f:
        for i in vocab:
            f.write('%s\n' % i)


def load_vocab(data_dir, labelled_data):
    if not (os.path.exists('../vocabulary/lemma_vocab.txt')):
        generate_vocab(data_dir, labelled_data)
    vocab = []
    with open('../vocabulary/lemma_vocab.txt', 'r', encoding='utf8') as f:
        for i in f.readlines():
            vocab.append(i.rstrip('\n'))
    return vocab


if __name__ == '__main__':

    data_dir = '../../../UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'

    vocab = load_vocab(data_dir, labelled_data)



    word = "alacaklılardandı"
    temp_word = ""

    while True:
        temp_word = greedy_stemming(word, vocab)
        if temp_word == word:
            break
        else:
            word = temp_word


    print(temp_word)