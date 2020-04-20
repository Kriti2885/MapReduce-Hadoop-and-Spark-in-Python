#!/usr/bin/env python3

import sys
from collections import defaultdict

reducedDict = defaultdict(list)
duplicate = []
num = 0
for line in sys.stdin:                              # Reading the results of mapperAnagram. The anagrams are printed
                                                    # line by line.
    line = line.strip()                             # Strip the line from console
    word = line.split()                             # Splitting the words
    if len(word)>1:                                 # checking for length of word to be greater than 1
        for i in range(len(word)):
            if word[i] not in reducedDict[num]:     # Creating reduced dictionary where key is number i.e. number of
                reducedDict[num].append(word[i])    # ..anagram. implemented this way so that we can know how many
    num += 1                                        # ..anagrams are in total.
for key, value in reducedDict.items():
    if len(value)>1 and value not in duplicate:     # removing single words, more that one words can be anagrams pairs.
        duplicate.append(value)                     # .. checking for duplicacy
        print(*value, sep=' ')                      # printing the final reduced list.
print(num)                                          # printing the number of anagrams.