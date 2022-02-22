#!/usr/bin/env python

import sys
import collections

min_reads = int(sys.argv[1])
dirt = sys.argv[2]

prev_barcode = ""
instances = []
heads = []
for line in sys.stdin:
    if line.split()[0]=='@SQ' or line.split()[0]=='@PG':
        heads.append(line)
    cur_barcode = line.strip().split()[0].split(':')[0]
    if cur_barcode != prev_barcode:
        if(len(instances) >= min_reads):
            with open(dirt + '/' +  prev_barcode + '.sam', 'w') as fout:
                for elem in heads:
                    fout.write(elem)
                for elem in instances:
                    fout.write(elem)
        prev_barcode = cur_barcode
        instances = []
        instances.append(line)
    else:
        instances.append(line)
