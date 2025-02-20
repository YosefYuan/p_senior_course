import re

def parse(text):
    # Remove special characters
    text = re.sub(r'[^\w]', ' ', text)

    # Convert to lower case
    text = text.lower()

    # Split text into words
    words = text.split(' ')

    # Remove empty words
    words = filter(None, words)

    # Return a dict for the word and word frequency
    word_cnt = {}
    for word in words:
        if word not in word_cnt:
            word_cnt[word] = 0
        word_cnt[word] += 1

    # Sort by frequency
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda kv: kv[1], reverse=True)

    return sorted_word_cnt

with open('in.txt', 'r') as fin:
    text = fin.read()

word_and_freq = parse(text)

with open('out.txt', 'w') as fout:
    for word, freq in word_and_freq:
        fout.write('{} {}\n'.format(word, freq))