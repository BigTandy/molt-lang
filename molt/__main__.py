import os
from bundler import bundle

dirpath = os.path.dirname(os.path.realpath(__file__))

bundled_system = bundle(os.path.join(dirpath, 'src'))

with open(os.path.join(dirpath, "molt"), 'w') as write_handle:
    write_handle.write(bundled_system)

exec(bundled_system)
