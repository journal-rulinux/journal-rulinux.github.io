#!/usr/bin/python3

import os
import io

for filename in os.listdir('../odt'):

    filename_base = filename[:-4]

    line = """.. title: {}
.. slug: {}
.. date: 2016-11-01 17:39:15 UTC+03:00
.. tags: sort
.. category:
.. link:
.. description:
.. type: text\n""".format(filename_base, filename_base)

    filename_meta = filename[:-4] + ".meta"
    with open(filename_meta, "w") as file:

        file.write(line)
