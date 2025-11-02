# build_index_uncompressed.py

import argparse
import re
from collections import Counter
from pyspark import SparkConf, SparkContext

# Add additional imports if needed.

# Use this function to tokenize text.
def tokenize(line):
    TOKEN_RE = re.compile(r'(^[^a-z]+|[^a-z]+$)')
    out = []
    for tok in line.split():
        w = TOKEN_RE.sub('', tok.lower())
        if w:
            out.append(w)
    return out

# Each input line is "docid<TAB>text".
# Use this function to parse.
def parse_line(line):
    parts = line.split("\t", 1)
    if len(parts) == 2:
        return int(parts[0]), parts[1]
    else:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-input', required=True)
    ap.add_argument('-output', required=True)
    args = ap.parse_args()

    conf = SparkConf().setAppName('build_index_uncompressed')
    sc = SparkContext(conf=conf)

    # Read content in the file (docid, text)
    rdd = sc.textFile(args.input)

    # BEGIN OF YOUR CODE
    # Write your code below.



    # END OF YOUR CODE

    postings_lists.saveAsTextFile(args.output)
    sc.stop()


if __name__ == '__main__':
    main()
