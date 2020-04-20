#!/usr/bin/env python3

import sys
from collections import defaultdict

mapped_list = defaultdict(list)

for line in sys.stdin:                                          # Takes an input for dataset path from console
    # print(line)
    line = line.strip()
    data = line.lower()                                         # Converting to lower case.
    words = data.split(" ")                                     # Spliting all words.

    for word in words:
        word = ''.join(e for e in word if e.isalnum())          # Filtering  alphanumeric characters.
        sorted_word = ''.join(sorted(word))                     # Sorting the word so if the word is "hello" sorted ..

        if sorted_word in mapped_list:                            # ... word would be "ehllo". The program check if ..
            list_of_words = mapped_list[sorted_word]              # .. "ehllo" is a key in dictionary. If so, the original...
            mapped_list[sorted_word].append(word)                 # ..word is appended to the key's value. If not the ..
        else:                                                   # .. sorted word is added to the dictionary as key and..
            mapped_list[sorted_word] = []                         # .. the original word is appended as value.
            mapped_list[sorted_word].append(word)                 # eg. mapped dict: {'ehllo':['hello', 'oellh'],
                                                                  #                   'eimt'  :['time', 'item', 'emit']}
# print(word_list)
for key, value in mapped_list.items():                          # The mapped dictionary is printed.
    print(*value, sep=' ')

