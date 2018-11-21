import argparse

from markold.markold import Markold
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


def main_multi(args):
    file = args.file
    markov = int(args.markov)
    number = int(args.number)
    output = args.output

    markold = Markold()
    markold.import_sentences(file)
    markold.generate_multiple_sentences(markov, number, to_output=output, to_print=args.print)


if __name__ == '__main__':
    args = parse_args()

    main_multi(args)
