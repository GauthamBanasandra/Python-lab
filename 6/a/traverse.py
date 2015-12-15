import os
import sys

__author__ = 'gauth_000'
loc = sys.argv[1]
dirs=files=0
for path, directory, file in os.walk(loc):
    print('path:', path)
    if directory:
        print('directories:', ', '.join(directory))
        dirs+=len(directory)
    if file:
        print('files:', ', '.join(file))
        files+=len(file)
    print()
print('directories=', dirs)
print('files=', files)