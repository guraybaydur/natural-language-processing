import math

import numpy as np
import conllu
import os


def generate_vocab(data_dir, filename):
    vocab = []
    with open(data_dir + filename, 'r', encoding='utf8') as f:
        for tokenlist in conllu.parse_incr(f):
            for i in tokenlist:
                if i['upos'] != 'AUX' and i['upos'] != 'PUNCT':
                    word = i['lemma'].lower()
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
            vocab.append(i.rstrip('\n'))
    return vocab


def generate_word_probabilities(corpus, vocab):
    if not os.path.exists('../vocabulary/tfs.npy'):
        corpus = corpus.split()
        size = len(vocab)
        tfs = np.zeros([size])
        for i in range(len(vocab)):
            count = corpus.count(vocab[i])
            tfs[i] = count
            # (1 / (1 + round(math.log(term_frequency, 10), 5)))
        np.save('../vocabulary/tfs.npy', tfs)

def determine_stopwords(vocab, n):
    tfs = np.load('../vocabulary/tfs.npy')
    sorted_indices = tfs.argsort()
    stopwords = [vocab[i] for i in list(sorted_indices[-n:])]
    #print(stopwords)

    return stopwords


def evaluate(vocab, true_labels):
    f1_scores = []
    n = range(20, 50)
    for i in n:
        stopwords = determine_stopwords(vocab, i)
        true_positives = 0
        for elem in stopwords:
            if elem in true_labels:
                true_positives += 1

        precision = true_positives / len(stopwords)
        recall = true_positives / len(true_labels)

        f1_score = (2 * precision * recall) / (precision + recall)
        f1_scores.append(f1_score)

    max_index = f1_scores.index(max(f1_scores)) + 20
    return determine_stopwords(vocab,max_index),max_index




if __name__ == '__main__':
    data_dir = '../../../datasets/ud-treebanks-v2.7/UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'

    predefined_stopwords = ['acaba', 'ama', 'aslında', 'az', 'bazı', 'belki', 'biri', 'birkaç', 'birşey', 'biz', 'bu',
                            'çok', 'çünkü', 'da', 'daha', 'de', 'defa', 'diye', 'eğer', 'en', 'gibi', 'hem', 'hep',
                            'hepsi', 'her', 'hiç', 'için', 'ile', 'ise', 'kez', 'ki', 'kim', 'mı', 'mu', 'mü', 'nasıl',
                            'ne', 'neden', 'nerde', 'nerede', 'nereye', 'niçin', 'niye', 'o', 'sanki', 'şey', 'siz',
                            'şu', 'tüm', 've', 'veya', 'ya', 'yani']

    if not (os.path.exists('../vocabulary/stopword_vocab.txt')):
        generate_vocab(data_dir, labelled_data)
    vocab = load_vocab(vocab_dir='../vocabulary/', name='stopword_vocab.txt')
    corpus = open(data_dir + corpus_name, 'r', encoding='utf8').read().replace("\n", " ")

    generate_word_probabilities(corpus, vocab)

    stopwords, max =evaluate(vocab,predefined_stopwords)
    print(max)