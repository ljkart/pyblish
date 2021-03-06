import os
import sys

# Expose Pyblish to PYTHONPATH
path = os.path.dirname(__file__)
sys.path.insert(0, path)

from pyblish.vendor import nose

if __name__ == '__main__':
    argv = sys.argv[:]
    argv.extend(['--verbose', '--exclude=vendor', '--with-doctest'])
    nose.main(argv=argv)
