#!/usr/bin/python3

import os
import io

for filename in os.listdir('../odt'):
    filename_without_extension = filename[:-4]
    with io.FileIO(filename_without_extension + ".meta", "w") as file:

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
    file.write(line)

