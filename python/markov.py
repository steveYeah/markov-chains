import random
import string
import sys

from collections import defaultdict

def create_map():
    word_map = defaultdict(list)
    transl = ''.maketrans('', '', string.punctuation)

    with open('../text.txt', 'r') as text:
        # Move all text into one line
        lines = text.readlines()
        full_text = ' '.join([line.strip() for line in lines])
        # Get rid of multiple spaces and remove punctuation
        full_text = ' '.join(full_text.split()).lower().translate(transl)
        words = full_text.split(' ')

        for i, word in enumerate(words):
            if i == 0:
                continue
            if i == len(words) - 1:
                break
                
            key = '{} {}'.format(words[i -1], word)
            value = words[i + 1]
            word_map[key].append(value)

    return word_map

if __name__ == '__main__':
    chain_length = int(sys.argv[1])
    word_map = create_map()
    
    starting_key = random.choice(list(word_map.keys()))
    result_words = starting_key.split(' ')
    result_words.append(random.choice(word_map[starting_key]))
    
    for i in range(1, chain_length - 2):
        key = '{} {}'.format(result_words[i], result_words[i + 1])
        if key not in word_map:
            break

        result_words.append(random.choice(word_map[key]))

    print(' '.join(result_words).lower().capitalize())
    print('({})'.format(len(result_words)))
