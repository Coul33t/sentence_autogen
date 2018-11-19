import argparse

import simple_markov_chain
import multi_markov
from tools import reformate_sentence
import pdb


def parse_args():
    """ Arguments parser. """

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="the file containing the sentences", type=str)
    parser.add_argument("-n", "--number", help="the number of sentences to generate", type=int, default=10)
    parser.add_argument("-m", "--markov", help="the number of words to look forward for (more = more realistic sentences, but less variation from original sentences)",
                        type=int, default=3)
    parser.add_argument("-o", "--output", help="the name of the output file", type=str)
    parser.add_argument("-p", "--print", help="print to the console", action="store_true", default=False)
    args = parser.parse_args()

    if not args.file:
        parser.error("Error: file required as an argument (-f or --file).")

    if not 0 < int(args.markov):
        parser.error("Error: markov value must be > 0.")

    return args


def main_single(file):
    initial_sentences = []

    # Load the sentences
    with open(file, 'r', encoding='utf-8') as input_file:
        initial_sentences = input_file.read().split('\n')

    # Generate sentences
    generated_sentences = simple_markov_chain.examples_to_sentences(initial_sentences, 30)
    
    # Print them
    for sentence in generated_sentences:
        print(reformate_sentence(sentence))


def main_multi(args):
    initial_sentences = []

    file = args.file
    markov = int(args.markov)
    number = int(args.number)
    output = args.output

    # Load the sentences
    with open(file, 'r', encoding='utf-8') as input_file:
        initial_sentences = input_file.read().split('\n')

    # Generate sentences
    generated_sentences = multi_markov.examples_to_sentences(initial_sentences, markov, number_to_generate=number, min_word_length=15, max_word_length=150)

    # Print and/or write them
    if output:
        output_file = open(output, 'a', encoding='utf-8')

    for sentence in generated_sentences:
        if args.print:
            print(reformate_sentence(sentence))
        if output:
            output_file.write(reformate_sentence(sentence) + '\n')

    if output:
        output_file.close()

if __name__ == '__main__':
    args = parse_args()

    main_multi(args)
