import random as rn
import pdb
from tools import (cumulative_probs, return_selected, beautify, normalise_word_matrix, reformate_sentence)

def compute_words(sentences):
    """ Returns a set of unique words across all the sentences. """

    words_set = set()

    for sentence in sentences:
        words = sentence.split(' ')
        for word in words:
            words_set.add(word)

    return words_set


def compute_word_occurence(sentences, word_order):
    """ Computes the number of occurences of each words following each ones. """

    matrix = {}

    for word in word_order:
        matrix[word] = {}

    for sentence in sentences:
        splitted = sentence.split(' ')
        for i, word in enumerate(splitted):
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


def generate_sentence(wpm, wpm_normalised, max_word_length=50):
    """ Generates a sentence from a list of word probabilities. """

    new_sentence = ''
    first_word = []
    last_word = ''

    # Get every words that can start a sentence
    for word, next_word_proba in wpm.items():
        if 'BEGIN' in next_word_proba:
            first_word.append([word, wpm[word]['BEGIN']])

    first_word = cumulative_probs(first_word)

    # Choose a random one
    random_choice = rn.random()
    first_choice = return_selected(random_choice, first_word)

    # We got our first word. Yay!
    new_sentence += first_choice + ' '
    last_word = first_choice

    iteration = 0

    # TODO: if X words is reached, go for the next with END
    while iteration < max_word_length or 'END' not in next_word_proba.keys():
        # Get the probable words following the last one
        next_word_proba = wpm_normalised[last_word]
        next_word_proba_lst = [[k, v] for k, v in next_word_proba.items() if k != 'BEGIN']
        next_word_proba_lst = cumulative_probs(next_word_proba_lst)
        # Choose a random one
        random_choice = rn.random()
        choice = return_selected(random_choice, next_word_proba_lst)

        # If we chose that this is the end of the sentence, then stop 
        if choice == 'END':
            break

        # Else, continue until we have reached the maximum number of words allowed
        new_sentence += choice + ' '
        last_word = choice

        iteration += 1

    return new_sentence

def examples_to_sentences(initial_sentences, number_to_generate=30, max_word_length=50):
    # Add spaces before and after quotes and commas
    trimmed = beautify(initial_sentences)

    # Get all unique words across all sentences
    word_order = compute_words(trimmed)

    # Compute the number of occurence of each words
    word_prob_matrix = compute_word_occurence(trimmed, word_order)

    # Transforms occurences into cumulative proabilities
    word_prob_matrix_normalised = normalise_word_matrix(word_prob_matrix)

    generated_sentences = [reformate_sentence(generate_sentence(word_prob_matrix, word_prob_matrix_normalised, max_word_length=max_word_length)) for x in range(number_to_generate)]

    return generated_sentences