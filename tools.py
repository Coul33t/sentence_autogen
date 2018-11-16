import string
import re
import copy
import pdb  

def purify(sentences):
    """ Gets rid of all punctuation signs. """

    # maketrans('this_is_mapped_to...', '...this', 'erase this')
    translator = str.maketrans('', '', string.punctuation)
    if isinstance(sentences, str):
        return sentences.translate(translator)

    elif isinstance(sentences, list):
        new_lst = []
        for sentence in sentences:
            new_lst.append(sentence.translate(translator))
        return new_lst

    return sentences


def beautify(sentences):
    """ Reformats sentences by adding a space before and after punctuation
        (to treat them as regular sentence parts). """

    translator = str.maketrans({key: " {0} ".format(key) for key in ','})

    if isinstance(sentences, str):
        return re.sub(r'\s+', ' ', sentences.translate(translator)).strip()

    elif isinstance(sentences, list):
        new_lst = []
        for sentence in sentences:
            new_lst.append(re.sub(r'\s+', ' ', sentence.translate(translator)).strip())
        return new_lst

    return sentences

def normalise_word_matrix(word_matrix):
    """ Normalises the number of occurences of each word (from occurences to probabilities). """

    new_matrix = copy.deepcopy(word_matrix)

    for word, probs in new_matrix.items():
        total_sum = sum(probs.values())

        for next_word_prob in probs.keys():
            new_matrix[word][next_word_prob] = new_matrix[word][next_word_prob] / total_sum

    return new_matrix

def cumulative_probs(lst):
    """ Orders the a list of probabilities and transforms them into cumulative probabilities. """

    total_sum = sum([x[1] for x in lst])

    # Normalising (-> probs)
    lst = [[x[0], x[1] / total_sum] for x in lst]

    # Ordering probs
    lst = sorted(lst, key=lambda x: x[1], reverse=False)

    # Cumulative probs
    for i, _ in enumerate(lst):
        if i != 0:
            lst[i][1] += lst[i-1][1]

    return lst

def return_selected(random_choice, lst):
    """ Chose a random word from a probabilities list. """

    for i, word in enumerate(lst):
        if i == 0:
            if random_choice < word[1]:
                return word[0]

        if i == len(lst) - 1:
            return word[0]

        else:
            if lst[i-1][1] <= random_choice < lst[i][1]:
                return word[0]

    # Sometimes, lst is empty
    try:
        return lst[0][0]
    except IndexError:
        return []


def reformate_sentence(sentence):
    """ Reformat the sentence correctly, such as punctuation have the correct spacing. """

    sentence = sentence.replace(' , ', ', ')
    sentence = sentence.replace(' \' ', '\'')
    return sentence