# Program takes a text file and computes the frequency of each lowercase character
# or space  that appears in the file

import sys
import pprint
import string

WHITELIST_CHARACTERS = string.ascii_lowercase + ' '

def count_chars(frequencies, whitelist=WHITELIST_CHARACTERS):
    '''Read the text content of a file and keep a running count of how often
    each character appears.

    Arguments:
        frequencies ‑‑ mapping from each character to its counted frequency
        whitelist ‑‑ string containing all characters to be included in the stats
            defaults to all lowercase letters and space

    Returns:
        nothing
    '''

    # Read in all the text from the file
    with open(sys.argv[1],"r") as f:
        text = f.read()

    # Loop over the whole file
    for c in text:
        if c in WHITELIST_CHARACTERS:
            # Accommodate the character if seen for the first time
            frequencies.setdefault(c, 0)
            # Increment the count for the present character
            frequencies[c] += 1
    
    return

if __name__ == '__main__':
    # Initialize the mapping
    frequencies = {}
    
    count_chars(frequencies)
    #count_chars(sys.argv[1], frequencies)
    # Display the resulting frequencies in readable format
    pprint.pprint(frequencies)
    