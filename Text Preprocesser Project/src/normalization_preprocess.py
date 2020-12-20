import numpy as np
import conllu
import os
from spelling_correction import create_predictions


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


def search_error(word, vocab, all_pos, word_prob):
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
    words = text.split()
    corrected_words = []
    for i in words:
        corrected_words.append(search_error(i, vocab, all_pos, word_prob))
    new_text = ' '.join(corrected_words)
    return new_text

if __name__ == '__main__':
    data_dir = '../../../UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'
    vocab = load_vocab(data_dir, labelled_data)
    corpus = open(data_dir + corpus_name, 'r', encoding='utf8').read().replace('\n', ' ')
    #generate_word_probabilities(corpus, vocab)
    #generate_all_possible_words(vocab)
    word_prob = load_word_probabilites(corpus, vocab)
    all_pos = load_all_possible_words(vocab)
    text = 'yaptığ hç ho deil'
    new_text = string_normalize(text, vocab, all_pos, word_prob)
    print('Orijinal cümle: ' + text)
    print('Normalize edilmiş cümle: ' + new_text)