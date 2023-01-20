# This is my text_generator project

from nltk.probability import FreqDist
from nltk.tokenize import WhitespaceTokenizer, word_tokenize

# All tokens
user_file = input()
f = open(user_file, 'r', encoding='utf8')
my_file = f.read()
my_tokenizer = WhitespaceTokenizer()
token_split = my_tokenizer.tokenize(my_file)
counter = 0
for tokens in token_split:
    counter += 1
print('Corpus statistics')
print('All tokens : ', counter)

# Unique tokens
words = word_tokenize(my_file)
my_dist = FreqDist(words)
word_freq = dict((word, freq) for word, freq in my_dist.items() if not word.isdigit())
my_list = []
for x in word_freq:
    my_list.append(word_freq[x])
list_string = map(str, my_list)
b = 0
for a in list_string:
    if a == '1':
        b += 1
print('Unique token : ', b)

# Print index
x = list(word_freq.keys())
while True:
    enter_index = input()
    try:
        if enter_index == 'exit':
            break
        elif int(enter_index) in range(len(x)):
            print('Your token is : ', x[int(enter_index)])
        elif int(enter_index) not in range(len(x)):
            print('IndexError')
        else:
            print('ValueError')
    except TypeError:
        print('Type Error')
    except ValueError:
        print('Value Error')
