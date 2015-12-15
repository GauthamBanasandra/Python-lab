import os
import sys

__author__ = 'gauth_000'
path = sys.argv[1]
os.chdir(path)
for file in os.listdir('.'):
    if os.path.isfile(file) and not os.path.getsize(file):
        os.remove(file)
