import argparse

import simple_markov_chain
import dual_markov_chain
from tools import reformate_sentence
import pdb


def parse_args():
    """ Arguments parser. """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the file containing the sentences")
    parser.add_argument("-m", "--markov", help="the number of words to look forward for (more = more realistic sentences, but less variation from original sentences)",
                        default=2)
    args = parser.parse_args()

    if not args.file:
        parser.error("Error: file required as an argument (-f or --file).")

    return args


def main_single(file):
    initial_sentences = []

    # Load the sentences
    with open(file, 'r', encoding='utf-8') as input_file:
        initial_sentences = input_file.read().split('\n')

    generated_sentences = simple_markov_chain.examples_to_sentences(initial_sentences, 30)

    # Generate sentences
    for sentence in generated_sentences:
        print(reformate_sentence(sentence))


def main_dual(file):
    initial_sentences = []

    # Load the sentences
    with open(file, 'r', encoding='utf-8') as input_file:
        initial_sentences = input_file.read().split('\n')

    generated_sentences = dual_markov_chain.examples_to_sentences(initial_sentences, 30)

    for sentence in generated_sentences:
        print(reformate_sentence(sentence))


if __name__ == '__main__':
    args = parse_args()

    if int(args.markov) == 1:
        main_single(args.file)
    elif int(args.markov) == 2:
        main_dual(args.file)
