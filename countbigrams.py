# Program takes a text file and computes the frequency of each bigram that
# appears in the file

import sys
from collections import Counter
import pprint

from nltk.util import bigrams
from nltk.tokenize import RegexpTokenizer

# Set up a tokenizer which only captures lowercase letters and spaces
# This requires that input has been preprocessed to lowercase all letters
TOKENIZER = RegexpTokenizer("[a-z ]")

def count_bigrams(frequencies):
    '''Read the text content of a file and keep a running count of how often
    each bigram (sequence of two) characters appears.

    Arguments:
        frequencies ‑‑ mapping from each bigram to its counted frequency
        
    Returns:
        nothing
    '''

    # Read in all the text from the file and set all letters to lowercase
    with open(sys.argv[1],"r") as f:
        text = f.read().lower()

    # This step is needed to collapse runs of space characters into one
    text = ' '.join(text.split())
    
    """
    spans = TOKENIZER.span_tokenize(text)
    tokens = (text[begin : end] for (begin, end) in spans)
    """

    tokens = TOKENIZER.tokenize(text)
    for bigram in bigrams(tokens):
        # Increment the count for the bigram. Automatically handles any
        # bigram not seen before. The join expression turns 2 separate 
        # single‑character strings into one 2‑character string
        frequencies[''.join(bigram)] += 1
        
    return


if __name__ == '__main__':
    # Initialize the mapping
    frequencies = Counter()
    
    count_bigrams(frequencies)
    # Uncomment the following line to display all the resulting frequencies
    # in readable format
    pprint.pprint(frequencies)
    # Print just the 20 most common bigrams and their frequencies
    # in readable format
    pprint.pprint(frequencies.most_common(20))