#!/usr/bin/python3

import os
import io

for filename in os.listdir('../odt'):

    line = """#+BEGIN_COMMENT
    .. title: {}
    .. slug: {}
    .. date: 2016-11-01 17:39:15 UTC+03:00
    .. tags: sort
    .. category:
    .. link:
    .. description:
    .. type: text
#+END_COMMENT\n""".format(filename, filename)

    filename_meta = filename[:-4] + ".meta"
    with open(filename_meta, "w") as file:

        file.write(line)

