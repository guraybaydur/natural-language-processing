from rule_based_tokenizer import rule_based_tokenizer
from rule_based_sentence_splitter import rule_based_sentence_splitter
from ml_tokenizer import ml_tokenizer
from ml_sentence_splitter import ml_sentence_splitter
from normalization import normalize
from stemmer import stemmer
from stopwords import static_eliminate_stopwords
from stopwords_dynamic import dynamic_stopword_eliminate
import time

def print_operation_list():
    print('Possible processing options:')
    print('1) Tokenization')
    print('2) Sentence Segmentation')
    print('3) Normalization')
    print('4) Stemming')
    print('5) Stopword Elimination')
    print('Type \'text\' if you want to enter a new text')
    print('Type \'exit\' if you want to terminate the program')

if __name__ == '__main__': #burası yarım kaldı yarın tamamlarım
    print('Welcome to Basic Text Preprocessing Tool')
    print('This program was implemented by Mansur Yeşilbursa and Güray Baydur as a course assignment in CMPE 561')
    time.sleep(2)
    user_input = ''
    text = input('Enter the text you want to process')
    print_operation_list()
    while user_input != 'exit' and user_input != 'Exit':

        op_no = input('Enter the operation number you want to continue with (i.e. 1 -> Tokenization) \n Type \'exit\' to finish execution')
        if int(op_no) == 1: # Tokenization
            print('There are two types of tokenization:')
            print('1) Rule-based Tokenization')
            print('2) Logistic Regression Based Tokenization')
            sub_op = input('Which type of tokenization do you want to use? (1 or 2)')
            if int(sub_op) == 1: # rule based tokenization
                processed_text = rule_based_tokenizer(text)
            elif int(sub_op) == 2:
                processed_text = ml_tokenizer(text)
            else:
                print('Invalid Choice')
