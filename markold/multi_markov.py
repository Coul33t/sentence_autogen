import pdb
from .tools import (cumulative_probs, return_selected, beautify, normalise_word_matrix, reformate_sentence)
import random as rn

def get_key(words, i, n):
    new_key = []
    for j in range(n):
        new_key.append(words[i+j])
    return tuple(new_key)

def compute_words(sentences, nb):
    """ Returns a set of unique pair of words across all the sentences. """

    n_words_set = set()

    for sentence in sentences:
        words = sentence.split(' ')
        if len(words) > (nb - 1):
            for i, _ in enumerate(words):
                if i < len(words) - nb + 1:
                    n_words_set.add(get_key(words, i, nb))
    
    return n_words_set

def compute_word_occurence(sentences, word_order, n):
    """ Computes the number of occurences of each words following each pair of words. """

    matrix = {}

    for word in word_order:
        matrix[word] = {}

    for sentence in sentences:
        splitted = sentence.split(' ')
        if len(splitted) > n - 1:
            for i, word in enumerate(splitted):

                if i < len(splitted) - n + 1:
                    key = get_key(splitted, i, n)
                else:
                    break

                if i == 0:
                    if 'BEGIN' in matrix[key]:
                        matrix[key]['BEGIN'] += 1
                    else:
                        matrix[key]['BEGIN'] = 1

                if i == len(splitted) - n:
                    if 'END' in matrix[key]:
                        matrix[key]['END'] += 1
                    else:
                        matrix[key]['END'] = 1

                if i < len(splitted) - n:
                    if splitted[i+n] in matrix[key]:
                        matrix[key][splitted[i+n]] += 1
                    else:
                        matrix[key][splitted[i+n]] = 1

    return matrix

def generate_sentence(wpm, wpm_normalised, min_word_length=0, max_word_length=50):
    """ Generates a sentence from a list of word probabilities. """

    new_sentence = ''
    first_word = []
    last_word = ''

    # Get every couple of words that can start a sentence
    for word, next_word_proba in wpm.items():
        if 'BEGIN' in next_word_proba:
            first_word.append([word,  wpm[word]['BEGIN']])

    first_word = cumulative_probs(first_word)

    # Choose a random one
    random_choice = rn.random()
    first_choice = return_selected(random_choice, first_word)

    # We got our first couple of words. Yay!
    new_sentence += ' '.join(first_choice) + ' '
    last_word = first_choice

    iteration = 0

    while iteration <= max_word_length or 'END' not in next_word_proba.keys():
        
        #BUG: Sometimes, the algorithm get stuck in an infinite loop between 2 words
        if iteration > max_word_length * 2:
            print(f'WARNING: endless loop between two words, invalid sentence (ditched)')
            return ''
            

        # BUG: shouldn't happen (but it did)
        try:
            # Get the probable words following the last one
            next_word_proba = wpm_normalised[last_word]
        except KeyError:
            break

        next_word_proba_lst = [[k, v] for k, v in next_word_proba.items() if k != 'BEGIN']
        next_word_proba_lst = cumulative_probs(next_word_proba_lst)

        # If we have reached the maximum number of words allowed and we can end here, do it
        if iteration > max_word_length and any(x[0] == 'END' for x in next_word_proba_lst):
            break
        
        # Else, pick a random one
        else:
            random_choice = rn.random()
            
            choice = return_selected(random_choice, next_word_proba_lst)

        # If we chose that this is the end of the sentence
        if choice == 'END':
            # If we reached the minimal number of words in the sentence, we're done
            if iteration >= min_word_length:
                break
            
            else:
                # Else, check if there are other possibilities than END
                removed_end_cumulative = [x for x in next_word_proba_lst if x[0] != 'END']
                if removed_end_cumulative:
                    random_choice = rn.random()
                    choice = tuple([return_selected(random_choice, removed_end_cumulative)])
                # Else, we have no other choice than finishing the sentence
                else:
                    break


        # Else, take a random couple of words beginning with the choosen word
        else:
            lst = [k for k in wpm.keys() if k[0] == choice]
            if lst:
                choice = lst[rn.randint(0, len(lst) - 1)]
            else:
                break

        # Continue until we have reached the maximum number of words allowed
        new_sentence += ' '.join(choice) + ' '
        last_word = choice

        iteration += 1

    return new_sentence

def examples_to_sentences(initial_sentences, markov=2, number_to_generate=30, min_word_length=15, max_word_length=200):
    # Add spaces before and after quotes and commas
    trimmed = beautify(initial_sentences)

    # Get all unique words across all sentences
    word_set = compute_words(trimmed, markov)

    # Compute the number of occurence of each words
    word_prob_matrix = compute_word_occurence(trimmed, word_set, markov)

    # Transforms occurences into cumulative probabilities
    word_prob_matrix_normalised = normalise_word_matrix(word_prob_matrix)

    generated_sentences = []
    for x in range(number_to_generate):
        print(f'Generating sentence {x}...', end=' ')
        generated_sentences.append(reformate_sentence(generate_sentence(word_prob_matrix, word_prob_matrix_normalised, 
                                                                        min_word_length=min_word_length, max_word_length=max_word_length)))
        print(f'sentence generated.')
    
    return generated_sentences