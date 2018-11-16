# sentence_autogen

Creates sentences by using Markov chains.

Needs a text (.txt) file with sentences (one line per sentence).

Arguments:
- `-f` / `--file` : the input file
- `-m`/ `--markov` (default: 2): the number of forward word: bigger values means more realistic sentences, but less variation from original sentences

Example:
`py -3 main.py -f data.txt`
