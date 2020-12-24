import nltk
import ssl
import re
import os

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('stopwords')

from nltk.corpus import stopwords

print(stopwords.words('turkish'))


def identify_unambiguous_punctuations(document):
    unambiguous_punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"']
    unambiguous_punctuations_locations = []

    for charIndex in range(0, len(document)):
        is_found = 0
        for punctuation in unambiguous_punctuations:
            if document[charIndex] == punctuation:
                is_found = 1
                break
        if is_found:
            # print("Punctuation " + punctuation + " detected ")
            unambiguous_punctuations_locations.append((charIndex, charIndex))
    return unambiguous_punctuations_locations


def identify_proper_commas_and_dots(document):
    proper_commas_and_dots_locations = []
    for char_index in range(0, len(document)):
        if document[char_index] == ',' or document[char_index] == '.':
            if char_index - 1 >= 0 and char_index + 1 < len(document):
                is_between_numbers = (document[char_index - 1].isnumeric() and document[char_index + 1].isnumeric())
                if not is_between_numbers:
                    # print("Punctuation " + document[char_index] + " detected at index " + str(char_index) + " and it is not between numbers")
                    proper_commas_and_dots_locations.append((char_index, char_index))
    return proper_commas_and_dots_locations


def identify_urls(document):
    regex = r"(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/|HTTP:\/\/WWW\.|HTTPS:\/\/WWW\.|HTTP:\/\/|HTTPS:\/\/)?[A-Za-z0-9]+([\-\.]{1}[A-Za-z0-9]+)*\.[A-Za-z]{2,5}(:[0-9]{1,5})?(\/.[^\s]*)?"
    urls = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
    return urls


def identify_emails(document):
    regex = r'[\w\.-]+@[\w\.-]+'
    emails = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
    return emails


def identify_hashtags(document):
    regex = r"\B#([^\s])*\b"
    hashtags = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
    return hashtags

def identify_multi_word_expressions(document):
    input_file_name = "../vocabulary/verbal_mwe_lexicon.txt"
    all_mwe_locations = []

    with open(input_file_name) as f:
        mwes = f.read().splitlines()

    for mwe in mwes:
        mwe_locations = [(m.start(0), m.end(0)) for m in re.finditer(r'\b%s\b' % mwe, document)]
        #if len(mwe_locations) > 0:
            # print(document)
            # print(mwe)
            # print(mwe_locations)
            # x = document[mwe_locations[0][0]:mwe_locations[0][1]]
            # print(document[mwe_locations[0][0]:mwe_locations[0][1]])
        all_mwe_locations.extend(mwe_locations)

    return all_mwe_locations

# print("String is: \n" + document)


def split_document(document, tuple_list):
    tuple_list_index = 0
    result = ""
    char_index = 0

    while char_index != len(document):
        if tuple_list_index < len(tuple_list):
            while char_index < tuple_list[tuple_list_index][0]:
                result += document[char_index]
                char_index += 1
            result += " "
            while char_index < tuple_list[tuple_list_index][1]:
                result += document[char_index]
                char_index += 1
            if char_index < len(document):
                result = result + document[char_index] + " "
                tuple_list_index += 1
                char_index += 1
        else:
            result += document[char_index]
            char_index += 1
    return result.split()


def rule_based_tokenizer(document):
    all_locations = []

    hashtags_tuple = identify_hashtags(document)
    urls_tuple = identify_urls(document)
    emails_tuple = identify_emails(document)
    mwes_tuple = identify_multi_word_expressions(document)
    unambiguous_punctuations_tuple = identify_unambiguous_punctuations(document)
    proper_commas_and_dots_tuple = identify_proper_commas_and_dots(document)


    if hashtags_tuple:
        all_locations = all_locations + hashtags_tuple
    if urls_tuple:
        all_locations = all_locations + urls_tuple
    if emails_tuple:
        all_locations = all_locations + emails_tuple
    if mwes_tuple:
        all_locations = all_locations + mwes_tuple
    if unambiguous_punctuations_tuple:
        all_locations = all_locations + unambiguous_punctuations_tuple
    if proper_commas_and_dots_tuple:
        all_locations = all_locations + proper_commas_and_dots_tuple

    all_locations.sort()

    single_token_locations = []
    other_token_locations = []

    for tuple in all_locations:
        [start, end] = [*tuple]
        if end == start:
            single_token_locations.append(tuple)
        else:
            other_token_locations.append(tuple)

    single_token_locations_copy = single_token_locations.copy()
    other_token_locations_copy = other_token_locations.copy()

    for single_token in single_token_locations_copy:
        for other_token in other_token_locations_copy:
            if single_token[0] in range(*other_token):
                print(single_token)
                if single_token in single_token_locations:
                    single_token_locations.remove(single_token)
                else:
                    if other_token in other_token_locations:
                        other_token_locations.remove(other_token)

    all_locations = single_token_locations + other_token_locations
    all_locations.sort()
    return split_document(document, all_locations)


def static_eliminate_stopwords(token_list):
    for token in token_list:
        if token in stopwords.words('turkish'):
            token_list.remove(token)
    return token_list


if __name__ == '__main__':

    general_folder_path = "/Users/guraybaydur/Desktop/BOUN/561 NLP/Assignment1/datasets/42bin_haberv2/news/"
    filename_suffix= "rule_based_tokenizer_and_stopwords_eliminated.txt"

    for folder_name in os.listdir(general_folder_path):
        for file in os.listdir(general_folder_path + folder_name):
            regex = r'^[0-9]+\.txt$'
            if re.search(regex, file):
                f = open(general_folder_path + folder_name + "/" + file, "r")
                document = f.read()
                result = rule_based_tokenizer(document)
                output_file_name = general_folder_path + folder_name + "/" + file[0:len(file) - 4] + filename_suffix
                f = open(output_file_name, "a")
                final_list = static_eliminate_stopwords(result)
                for token in final_list:
                    f.write(token + "\n")
                f.close()
