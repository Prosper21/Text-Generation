import sys
import json

from nltk.util import ngrams
from nltk.tokenize import RegexpTokenizer
from nltk.probability import FreqDist

#Set up a tokenizer that captures only words
#This requires that input has been preprocessed to lowercase all letters
TOKENIZER = RegexpTokenizer("[a-z]+")

def count_ngrams(frequencies, order):
	'''Read the text content of a file and keep a running count of how often
	each ngram (sequence of n) characters appears.

	Arguments:
		frequencies ‑‑ mapping from each bigram to its counted frequency
		order -- the value of n to be used for the ngrams
		
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
		#Join ngrams into a single space separated string
		ngram_text = ' '.join(ngram)
		#Extra layer to make sure no multiple runs of spaces sneak through
		ngram_text = ' '.join(ngram_text.split())
		#Increment the count for the ngram. Automatically handles any
		#ngram not seen before. The join expression turns n separate 
		#single‑character strings into one n‑character string
		frequencies[ngram_text] += 1
		
	return

if __name__ == '__main__':
	#Initialize the frequency distribution, a Subclass of collections.Counter
	frequencies = FreqDist()
	#The order of the ngrams is the third command line argument
	order = int(sys.argv[2])
	#Pull the input data from the console
	count_ngrams(frequencies, order)
	outputfp = open(sys.argv[3], 'w')
	json.dump(dict(frequencies), outputfp)
	print('Stored frequencies of {} encountered N‑grams.'.format(len(frequencies)))
