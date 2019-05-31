import sys
import json

from nltk.probability import FreqDist
from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer

#Set up a tokenizer that captures only lowercase letters and spaces
#This requires that input has been preprocessed to lowercase all letters
TOKENIZER = RegexpTokenizer("[a-z ]")

def count_ngrams(frequencies, order):
    '''Read the text content of a file and keep a running count of how often
    each ngram (sequence of n characters) appears.

    Arguments:
        frequencies ‑‑ mapping from each bigram to its counted frequency
        order ‑‑ The N in each N‑gram (i.e. number of items)

    Returns:
        nothing
    '''


    # Read in all the text from the file and set all letters to lowercase
    with open(sys.argv[1],"r") as f:
        text = f.read().lower()

    #This step is needed to collapse runs of space characters into one
    text = ' '.join(text.split())
    
    """
    spans = TOKENIZER.span_tokenize(text)
    tokens = (text[begin : end] for (begin, end) in spans)
    """

    tokens = TOKENIZER.tokenize(text)
    for ngram in ngrams(tokens, order):
        #Increment the count for the bigram. Automatically handles any
        #bigram not seen before. The join expression turns 2 separate 
        #single‑character strings into one 2‑character string
        if '  ' not in ''.join(ngram):
            frequencies[''.join(ngram)] += 1
        
    return

if __name__ == '__main__':
    #Initialize the mapping
    frequencies = FreqDist()
    #The order of the ngrams is the first command line argument
    ngram_order = int(sys.argv[2])
    #Pull the input data from the console
    count_ngrams(frequencies, ngram_order)
    outputfp = open(sys.argv[3], 'w')
    json.dump(dict(frequencies), outputfp)
    print('Stored frequencies of {} encountered N‑grams.'.format(len(frequencies)))
