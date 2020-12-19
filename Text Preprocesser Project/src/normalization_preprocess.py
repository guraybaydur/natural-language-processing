import numpy as np
import conllu
import os

def generate_vocab(data_dir, filename):
    vocab = []
    with open(data_dir + filename, 'r', encoding='utf8') as f:
        for tokenlist in conllu.parse_incr(f):
            for i in tokenlist:
                if i['upos'] != 'AUX' and i['upos'] != 'PUNCT':
                    word = i['form']
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


def load_vocab(vocab_dir, name):
    vocab = []
    with open(vocab_dir + name, 'r', encoding='utf8') as f:
        for i in f.readlines():
            vocab.append(i.rstrip('\n'))
    return vocab


def generate_word_probabilities(corpus, vocab):
    size = len(vocab)
    probs = np.zeros([size])
    for i in range(len(vocab)):
        count = corpus.count(vocab[i])
        probs[i] = np.log(count+1/size)
    np.save('../vocabulary/word_probs.npy', probs)

if __name__ == '__main__':
    data_dir = '../../../UD_Turkish-BOUN/'
    labelled_data = 'tr_boun-ud-train.conllu'
    corpus_name = 'tr_boun-ud-train.txt'
    if not (os.path.exists('../vocabulary/normalization_vocab.txt')):
        generate_vocab(data_dir, labelled_data)
    vocab = load_vocab(vocab_dir='../vocabulary/', name='normalization_vocab.txt')
    corpus = open(data_dir + corpus_name, 'r', encoding='utf8').read()
    generate_word_probabilities(corpus, vocab)