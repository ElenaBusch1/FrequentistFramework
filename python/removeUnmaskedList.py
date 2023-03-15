#!/bin/env python

from __future__ import print_function
import sys, argparse

keep_masked = True

#suffix to search:
suffix = "_masked.root"
#suffix to remove:
suffix_rm = ".root"

def main(args):

    paths = args

    for path in paths:
        with open(path, 'r') as f:
            lines = f.read().splitlines()

        for l in lines:
            if l.endswith(suffix):
                if keep_masked:
                    _l = l.replace(suffix, suffix_rm)
                    lines.remove(_l)
                else:
                    lines.remove(l)
            
        with open(path.replace(".txt", "_removed.txt"), 'w') as f:
            f.writelines([line + '\n' for line in lines])

if __name__ == "__main__":  
   sys.exit(main(sys.argv[1:]))   
