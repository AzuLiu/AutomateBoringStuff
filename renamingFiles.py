# Renaming the files with American-Style dates to European-Style files
# 1.Getting path and regular expression;
# 2.Searching the regex in files names:
# 3.Renaming the names with the regex.

import os, shutil, re

# 1.Regex and path
dataRegex = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    ((0|1|2|3)?\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)
path = input('Path:')

# 2.Search
for files in os.listdir(path):
    mo = dataRegex.search(files)
    if mo is None:
        continue
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)
# 3.Rename
    filesNew = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    files = os.path.join(path, files)
    filesNew = os.path.join(path, filesNew)
    print('Renaming "%s" to  "%s"' % (files, filesNew))
    # shutil.move(files,filesNew)
