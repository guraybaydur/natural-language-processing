# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# import re
# #
#
# def identify_unambiguous_punctuations(document):
#     unambiguous_punctuations = ['?', ';', '(', ')', '!', ':', '[', ']', '{', '}', '"']
#     unambiguous_punctuations_locations = []
#
#     for charIndex in range(0, len(document)):
#         is_found = 0
#         for punctuation in unambiguous_punctuations:
#             if document[charIndex] == punctuation:
#                 is_found = 1
#                 break
#         if is_found:
#             # print("Punctuation " + punctuation + " detected ")
#             unambiguous_punctuations_locations.append((charIndex, charIndex))
#     return unambiguous_punctuations_locations
#
#
# def identify_proper_commas_and_dots(document):
#     proper_commas_and_dots_locations = []
#     for char_index in range(0, len(document)):
#         if document[char_index] == ',' or document[char_index] == '.':
#             if char_index - 1 >= 0 and char_index + 1 < len(document):
#                 is_between_numbers = (document[char_index - 1].isnumeric() and document[char_index + 1].isnumeric())
#                 if not is_between_numbers:
#                     # print("Punctuation " + document[char_index] + " detected at index " + str(char_index) + " and it is not between numbers")
#                     proper_commas_and_dots_locations.append((char_index, char_index))
#     return proper_commas_and_dots_locations
#
#
# def identify_urls(document):
#     # regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
#     regex = r"(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/|HTTP:\/\/WWW\.|HTTPS:\/\/WWW\.|HTTP:\/\/|HTTPS:\/\/)?[A-Za-z0-9]+([\-\.]{1}[A-Za-z0-9]+)*\.[A-Za-z]{2,5}(:[0-9]{1,5})?(\/.[^\s]*)?"
#     urls = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
#     # urls = re.findall(regex, document)
#     # urls = [a_tuple[0] for a_tuple in urls]
#     return urls
#
#
# def identify_emails(document):
#     regex = r'[\w\.-]+@[\w\.-]+'
#     emails = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
#     # new_document = [a_tuple[0] for a_tuple in new_document]
#     return emails
#
#
# # f2 = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/1239.txt", "r")
# f2 = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/magazin/1468.txt", "r")
# # f2 = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/2900.txt", "r")
# # f2 = open("/Users/guraybaydur/Desktop/BOUN/561 NLP/42bin_haber_mansur/news/dunya/test.txt", "r")
# # mystr = f.read()
# mystr2 = f2.read()
#
#
# # print(mystr)
# # print(identify_urls(mystr))
#
# def identify_hashtags(document):
#     regex = r"\B#([^\s])*\b"
#     hashtags = [(m.start(0), m.end(0)) for m in re.finditer(regex, document)]
#     return hashtags
#
#
# print("String is: \n" + mystr2)
#
#
# def rule_based_tokenizer(document):
#
#
#     all_locations = []
#
#     hashtags_tuple = identify_hashtags(mystr2)
#     urls_tuple = identify_urls(mystr2)
#     emails_tuple = identify_emails(mystr2)
#     unambiguous_punctuations_tuple = identify_unambiguous_punctuations(mystr2)
#     proper_commas_and_dots_tuple = identify_proper_commas_and_dots(mystr2)
#
#     # print(len(hashtags_tuple))
#     # print(len(urls_tuple))
#     # print(len(unambiguous_punctuations_tuple))
#     # print(len(proper_commas_and_dots_tuple))
#     # print(len(emails_tuple))
#
#     if hashtags_tuple:
#         all_locations = all_locations + hashtags_tuple
#     if urls_tuple:
#         all_locations = all_locations + urls_tuple
#     if emails_tuple:
#         all_locations = all_locations + emails_tuple
#     if unambiguous_punctuations_tuple:
#         all_locations = all_locations + unambiguous_punctuations_tuple
#     if proper_commas_and_dots_tuple:
#         all_locations = all_locations + proper_commas_and_dots_tuple
#
#     all_locations.sort()
#
#     # print(all_locations)
#
#     single_token_locations = []
#     other_token_locations = []
#
#     for tuple in all_locations:
#         [start, end] = [*tuple]
#         # print("tuple[0] = "+ str(tuple[0]))
#         # print("tuple[1] = "+ str(tuple[1]))
#         # print("start = "+ str(start))
#         # print("end = "+ str(end))
#         # print()
#         if end == start:
#             # print(str(start) + ' ' + str(end))
#             single_token_locations.append(tuple)
#         else:
#             other_token_locations.append(tuple)
#
#     print("Single tokens: " + str(single_token_locations))
#     print("Other tokens: " + str(other_token_locations))
#
#     # print(str(single_token_locations[1]))
#
#     single_token_locations_copy = single_token_locations.copy()
#     other_token_locations_copy = other_token_locations.copy()
#
#     for single_token in single_token_locations_copy:
#         for other_token in other_token_locations_copy:
#             if single_token[0] in range(*other_token):
#                 print("single token index: " + str(single_token[0]) + " is in range: " + str(other_token[0]) + ":" + str(
#                     other_token[1]))
#                 print(single_token)
#                 if single_token in single_token_locations:
#                     single_token_locations.remove(single_token)
#                     print("Single token: " + str(single_token) + " is removed\n")
#                 else:
#                     other_token_locations.remove(other_token)
#
#     all_locations = single_token_locations + other_token_locations
#     all_locations.sort()
#     print(all_locations)
#
# rule_based_tokenizer(mystr2)

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




