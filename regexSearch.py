# Regex search
# 1.Get the path of the folder and regular expression;
# 2.Open all .txt files in this folder and search the regex in it;
# 3.Print the result to the screen.

import os
import re

# 1.Path and regular expression.
path = str(input('Which folder do you want to search?\n'))
regexStr = input('Which pattern do you want to search?\n')
regex = re.compile(regexStr)
pattern = []

# 2.Search regex
for files in os.listdir(path):
    if files.endswith('.txt'):
        f = open(os.path.join(path, files))
        pattern += regex.findall(f.read())

# 3.Print
print(pattern)
