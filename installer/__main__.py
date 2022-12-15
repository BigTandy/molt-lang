import sys
import os
from time import sleep

from install import install
from bundler import bundle

dirpath = os.path.dirname(os.path.realpath(__file__))


print("Bundling for installation...")
bundled_system = bundle(os.path.join(dirpath, '../molt/src'))

print("Installing...")

try:
    install(bundled_system)
except BaseException as e:
    if e == 0:
        print("Done!")

print("Done!")