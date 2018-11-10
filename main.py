import string
import re
import copy
import random as rn
import argparse

import pdb

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the file containing the sentences")
    args = parser.parse_args()
    
    if not args.file:
        parser.error("Error: file required as an argument (-f or --file).")
        
    return args

def purify(sentences):
    """ Gets rid of all punctuation signs. """

    # maketrans('this_is_mapped_to...', '...this', 'erase this')
    translator = str.maketrans('', '', string.punctuation)
    if type(sentences) == str:
        return sentences.translate(translator)

    elif type(sentences) == list:
        new_lst = []
        for sentence in sentences:
            new_lst.append(sentence.translate(translator))
        return new_lst

# 
def beautify(sentences):
    """ Reformats sentences by adding a space before and after punctuation (to treat them as regular sentence parts). """

    translator = str.maketrans({key: " {0} ".format(key) for key in ',\''})

    if type(sentences) == str:
        return re.sub( '\s+', ' ', sentences.translate(translator)).strip()

    elif type(sentences) == list:
        new_lst = []
        for sentence in sentences:
            new_lst.append(re.sub( '\s+', ' ', sentence.translate(translator)).strip())
        return new_lst


def compute_words(sentences):
    """ Returns a set of unique words across all the sentences. """

    yo = set()
    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            yo.add(word)
    return yo


def compute_word_occurence(sentences, word_order):
    """ Computes the number of occurences of each words following each ones. """

    matrix = {}

    for word in word_order:
        matrix[word] = {}

    for sentence in sentences:
        splitted = sentence.split(' ')
        for i,word in enumerate(splitted):
            if i == 0:
                if 'BEGIN' in matrix[word]:
                    matrix[word]['BEGIN'] += 1
                else:
                    matrix[word]['BEGIN'] = 1
            if i == len(splitted) - 1:
                if 'END' in matrix[word]:
                    matrix[word]['END'] += 1
                else:
                    matrix[word]['END'] = 1
            else:
                if splitted[i+1] in matrix[word]:
                    matrix[word][splitted[i+1]] += 1
                else:
                    matrix[word][splitted[i+1]] = 1

    return matrix

def normalise_word_matrix(word_matrix):
    """ Normalises the number of occurences of each word (from occurences to probabilities). """
    new_matrix = copy.deepcopy(word_matrix)

    for k, v in new_matrix.items():
        total_sum = sum(v.values())

        for kk, vv in v.items():
            new_matrix[k][kk] = new_matrix[k][kk] / total_sum

    return new_matrix

def cumulative_probs(lst):
    """ Orders the a list of probabilities and transforms them into cumulative probabilities. """
    total_sum = sum([x[1] for x in lst])

    # Normalising (-> probs)
    lst = [[x[0], x[1] / total_sum] for x in lst]

    # Ordering probs
    lst = sorted(lst ,key=lambda x: x[1], reverse=False)

    # Cumulative probs
    for i, val in enumerate(lst):
        if i != 0:
            lst[i][1] += lst[i-1][1]

    return lst

def return_selected(random_choice, lst):
    """ Chose a random word from a probabilities list. """
    for i, word in enumerate(lst):
        if i == 0:
            if random_choice < word[1]:
                return word[0]
                break

        if i == len(lst) - 1:
            return word[0]
            break

        else:
            if lst[i-1][1] <= random_choice < lst[i][1]:
                return word[0]
                break

def generate_sentence(wpm, wpm_normalised):
    """ Generates a sentence from a list of word probabilities. """
    new_sentence = ''
    first_word = []
    last_word = ''

    for k, v in wpm.items():
        if 'BEGIN' in v:
            first_word.append([k, wpm[k]['BEGIN']])

    first_word = cumulative_probs(first_word)

    random_choice = rn.random()

    first_choice = return_selected(random_choice, first_word)

    new_sentence += first_choice + ' '
    last_word = first_choice

    for i in range(30):
        next_word_proba = wpm_normalised[last_word]
        next_word_proba_lst = [[k, v] for k,v in next_word_proba.items() if k != 'BEGIN']
        next_word_proba_lst = cumulative_probs(next_word_proba_lst)
        random_choice = rn.random()
        choice = return_selected(random_choice, next_word_proba_lst)

        if choice == 'END':
            break

        new_sentence += choice + ' '
        last_word = choice

    return new_sentence

def reformate_sentence(sentence):
    """ Reformat the sentence correctly, such as punctuation have the correct spacing. """
    sentence = sentence.replace(' , ', ', ')
    sentence = sentence.replace(' \' ', '\'')
    return sentence

def main():
    args = parse_args()

    initial_sentences = []

    # Load the sentences
    with open(args.file, 'r', encoding='utf-8') as input_file:
        initial_sentences = input_file.read().split('\n')

    word_proba = []

    # Add spaces before and after quotes and commas
    trimmed = beautify(initial_sentences)

    # Get all unique words across all sentences
    word_order = compute_words(trimmed)

    # Compute the number of occurence of each words
    word_prob_matrix = compute_word_occurence(trimmed, word_order)

    # Transforms occurences into cumulative proabilities
    word_prob_matrix_normalised = normalise_word_matrix(word_prob_matrix)

    # Generate sentences
    for i in range(10):
        print(reformate_sentence(generate_sentence(word_prob_matrix, word_prob_matrix_normalised)))
        print('\n')



if __name__ == '__main__':
    main()