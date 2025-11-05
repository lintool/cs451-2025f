# boolean_retrieval_uncompressed.py

import argparse
import pickle

# Add additional imports if needed.

def vint_decode_one(buf, i):
    # returns (value, next_index)
    shift = 0
    n = 0
    while True:
        b = buf[i]
        i += 1
        n |= (b & 0x7F) << shift
        if (b & 0x80) == 0:
            break
        shift += 7
    return n, i


# BEGIN OF YOUR CODE
# Write your code below.


# END OF YOUR CODE


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('-index', required=True)
    ap.add_argument('-corpus', required=True)
    ap.add_argument('-query', required=True)
    args = ap.parse_args()

    # You'll have to implement this function:
    run_query(args.index, args.corpus, args.query)

if __name__ == '__main__':
    main()
