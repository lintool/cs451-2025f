# boolean_retrieval_uncompressed.py

import argparse
import os

# Add additional imports if needed.

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
