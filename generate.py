#!/usr/bin/env python3

import os

txt = """![](./dongxu/{})
"""

f = open("README.md", "a")
for filename in os.listdir("./dongxu"):
    if filename.endswith(".jpeg") or filename.endswith(".png"): 
         # print(os.path.join(directory, filename))
        f.write(txt.format(filename))
    else:
        continue
f.close()
