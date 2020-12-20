import numpy as np
import conllu
import os
from spelling_correction import create_predictions
import re
import itertools

def generate_vocab(data_dir, filename):
    vocab = []
    with open(data_dir + filename, 'r', encoding='utf8') as f:
        for tokenlist in conllu.parse_incr(f):
            for i in tokenlist:
                if i['upos'] != 'AUX' and i['upos'] != 'PUNCT':
                    word = i['form'].casefold()
                    lemma = i['lemma']
                    if word not in vocab:
                        vocab.append(word)
                    if lemma not in vocab and lemma != '_':
                        vocab.append(lemma)
    vocab_dir = '../vocabulary/'
    name = 'normalization_vocab.txt'
    with open(vocab_dir + name, 'w', encoding='utf8') as f:
        for i in vocab:
            f.write('%s\n' % i)


def load_vocab(data_dir, labelled_data):
    if not (os.path.exists('../vocabulary/normalization_vocab.txt')):
        generate_vocab(data_dir, labelled_data)
    vocab = []
    with open('../vocabulary/normalization_vocab.txt', 'r', encoding='utf8') as f:
        for i in f.readlines():
            vocab.append(i.rstrip('\n'))
    return vocab


def generate_word_probabilities(corpus, vocab):
    corpus = corpus.split()
    size = len(corpus)
    probs = np.zeros([len(vocab)])
    for i in range(len(vocab)):
        count = corpus.count(vocab[i])
        probs[i] = np.log((count+1)/size)
    np.save('../vocabulary/word_probs.npy', probs)


def load_word_probabilites(corpus, vocab):
    if not (os.path.exists('../vocabulary/word_probs.npy')):
        generate_word_probabilities(corpus, vocab)

    word_prob = np.load('../vocabulary/word_probs.npy')
    return word_prob


def generate_all_possible_words(vocab):
    all_poss = []
    for i in vocab:
        pos = create_predictions(i)
        all_poss.append(pos)
    with open('../vocabulary/all_possible_words.txt', 'w', encoding='utf8') as f:
        for i in all_poss:
            for j in i:
                f.write('%s ' % j)
            f.write('\n')


def load_all_possible_words(vocab):
    all_pos = []
    if not (os.path.exists('../vocabulary/all_possible_words.txt')):
        generate_all_possible_words(vocab)
    with open('../vocabulary/all_possible_words.txt', 'r', encoding='utf8') as f:
        for i in f.readlines():
            all_pos.append(i.split())
    return all_pos


def search_error(word, vocab, all_pos, word_prob):  # spelling error correction
    if word in vocab:
        return word
    else:
        indices = []
        for i in range(len(all_pos)):
            if word in all_pos[i]:
                indices.append(i)
        if len(indices) == 0:  # no candidate in the data
            print('No candidate for word ' + word)
            return word
        else: # candidates found
            word_probs = np.argsort(word_prob[indices])
            max_prob_word = vocab[indices[word_probs[-1]]]
            return max_prob_word


def string_normalize(text, vocab, all_pos, word_prob):
    pattern_subs = {'ıcam$':'acağım', 'cam$':'acağım', 'icem$':'eceğim', 'cem$':'eceğim', 'om$':'orum', 'ucaz$':'acağız',
                    'icez$':'eceğiz', 'am$':'ayım', 'em$':'eyim', 'mişin$':'mişsin', 'muşun$':'muşsun', 'oz$':'oruz'}

    ascii_pairs = {'i':'ı', 'u':'ü', 'o':'ö', 'g':'ğ', 'c':'ç', 's': 'ş'}
    words = text.split()  # apply true tokenization instead of just splitting
    corrected_words = []
    for i in words:  # check if it is only punctuation
        temp_word = letter_case_transformation(i)
        temp_word = accent_normalization(temp_word, pattern_subs)
        temp_word = search_error(temp_word, vocab, all_pos, word_prob)
        if temp_word not in vocab: # apply de-asciification
            temp_word = deascification(temp_word, vocab, ascii_pairs)
        corrected_words.append(temp_word)
    new_text = ' '.join(corrected_words)
    return new_text


def letter_case_transformation(word):
    if '\'' not in word:  # might be a proper noun, or sentence beginning
        if not word.islower() and not word.isupper():  # mixed case
            if word[0].isupper() and word[1:].islower():  # assume proper noun or sentence beginning
                return word
        return word.lower()
    else:
        size = len(word)
        pos = word.find('\'')
        if pos > 0 and pos < size - 1:  # if apostrophe is in the middle assume proper noun
            word = word.capitalize()
        else:
            word = word.lower()
    return word


def accent_normalization(word, patterns):  # covers some of the cases
    temp = word
    for key, value in patterns.items():
        temp = re.sub(key, value, temp)
        if temp != word:
            break
    return temp

def deascification(word, vocab, ascii_pairs):
    keys = list(ascii_pairs.keys())
    subset_keys = generate_subsets(keys)
    temp_word = word
    changed = False
    for i in subset_keys:
        for j in i:
            for k in j:
                word = re.sub(k, ascii_pairs[k], word)
            if word in vocab:
                changed = True
                break
        if changed:
            break
    if changed:
        return word
    else:
        return temp_word




def generate_subsets(values):
    subsets = []
    for i in range(len(values)):
        subsets.append(list(itertools.combinations(values, i+1)))
    return subsets




if __name__ == '__main__':
    data_dir = '../../../UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'
    vocab = load_vocab(data_dir, labelled_data)
    corpus = open(data_dir + corpus_name, 'r', encoding='utf8').read().replace('\n', ' ')
    word_prob = load_word_probabilites(corpus, vocab)
    all_pos = load_all_possible_words(vocab)
    text = 'askim'
    new_text = string_normalize(text, vocab, all_pos, word_prob)
    print('Orijinal cümle: ' + text)
    print('Normalize edilmiş cümle: ' + new_text)

    list = ['lı', 'li', 'lu', 'lü', 'casına', 'çasına', 'cesine', 'çesine', 'sınız', 'siniz', 'sunuz', 'sünüz',
            'muş', 'miş', 'müş', 'mış', 'ken', 'sın', 'sin', 'sun', 'sün', 'lar', 'ler', 'nız', 'niz', 'nuz', 'nüz',
            'tır', 'tir', 'tur', 'tür', 'dır', 'dir', 'dur', 'dür', 'ız', 'iz', 'uz', 'üz', 'ım', 'im', 'um', 'üm',
            'dı', 'di', 'du', 'dü', 'tı', 'ti', 'tu', 'tü', 'sa', 'se', 'm', 'n', 'k', 'ndan', 'ntan', 'nden', 'nten',
            'ları', 'leri', 'mız', 'miz', 'muz', 'müz', 'nız', 'niz', 'nuz', 'nüz', 'lar', 'ler', 'nta', 'nte','nda',
            'nde', 'dan', 'tan', 'den', 'ten', 'la', 'le', 'ın', 'in', 'un', 'ün', 'ca', 'ce', 'nı', 'ni', 'nu', 'nü',
            'na', 'ne', 'da', 'de', 'ta', 'te', 'ki', 'sı', 'si', 'su', 'sü', 'yı', 'yi', 'yu', 'yü', 'ya', 'ye']