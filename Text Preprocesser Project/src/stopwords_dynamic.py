import math

import numpy as np
import conllu
import os

def generate_vocab(data_dir, filename):
    vocab = []
    with open(data_dir + filename, 'r', encoding='utf8') as f:
        for tokenlist in conllu.parse_incr(f):
            for i in tokenlist:
                if i['upos'] != 'PUNCT':
                    word = i['form']
                    if word not in vocab:
                        vocab.append(word)
    vocab_dir = '../vocabulary/'
    name = 'stopword_vocab.txt'
    with open(vocab_dir + name, 'w', encoding='utf8') as f:
        for i in vocab:
            f.write('%s\n' % i)

def load_vocab(vocab_dir, name):
    vocab = []
    with open(vocab_dir + name, 'r', encoding='utf8') as f:
        for i in f.readlines():
            vocab.append(i.strip())
    return vocab

def generate_word_probabilities(corpus, vocab):
    size = len(vocab)
    reverse_tfs = np.zeros([size])
    for i in range(len(vocab)):
        count = corpus.count(vocab[i])
        print(vocab[i])
        print("count: " + str(count))
        reverse_tfs[i] = (1 / (1 + round(math.log(count, 10), 5)))
        # (1 / (1 + round(math.log(term_frequency, 10), 5)))
    np.save('../vocabulary/word_reverse_tfs.npy', reverse_tfs)

if __name__ == '__main__':
    data_dir = '../../../datasets/ud-treebanks-v2.7/UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'
    if not (os.path.exists('../vocabulary/stopword_vocab.txt')):
        generate_vocab(data_dir, labelled_data)
    vocab = load_vocab(vocab_dir='../vocabulary/', name='stopword_vocab.txt')
    corpus = open(data_dir + corpus_name, 'r', encoding='utf8').read()
    generate_word_probabilities(corpus, vocab)