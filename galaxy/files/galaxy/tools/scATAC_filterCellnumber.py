#!/usr/bin/env python

import sys

def main():
    barcode_list = []
    min_cov = int(sys.argv[1])
    fname = sys.argv[2]
    # load in the barcode
    with open(fname) as fin:
        for line in fin:
            [barcode, num] = line.split()
            num = int(num)
            if num >= min_cov: barcode_list.append(barcode)
    # iterate sam file
    for line in sys.stdin:
        # head of bam file
        if line[0] == '@':
            try:
                print line,
            except IOError:
                try:
                    sys.stdout.close()
                except IOError:
                    pass
                try:
                    sys.stderr.close()
                except IOError:
                    pass
            continue

        barcode_cur = line.split()[0].split(":")[0]
        if barcode_cur in barcode_list:
            try:
                print line,
            except IOError:
                try:
                    sys.stdout.close()
                except IOError:
                    pass
                try:
                    sys.stderr.close()
                except IOError:
                    pass


if __name__ == '__main__':
    main()
