#!usr/bin/python3
# -*- coding: utf-8 -*-

'''
This program requires one .fasta file and a tag list and generate a new .fasta file containing sequences whose tags are given in the list.
'''
import sys

def usage():
    print('Usage: python3 script.py [input_fasta_filename] [taglist_filename] [output_fasta_filename]')


def main():
    output_file = open(sys.argv[3], 'w')
    dict = {}
    with open(sys.argv[1], 'r') as input_file:
        for line in input_file:
            if line.startswith('>'):
                name = line.strip().split()[0][1:]
                dict[name] = ''
            else:
                dict[name] += line.replace('\n', '')

    with open(sys.argv[2], 'r') as taglist:
        for row in taglist:
            row = row.strip()
            for key in dict.keys():
                if key == row:
                    output_file.write('>' + key + '\n')
                    output_file.write(dict[key] + '\n')
    output_file.close()


try:
    main()
except IndexError:
    usage()