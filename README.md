# sentence_autogen

Creates sentences by using Markov chains.

Needs a text (.txt) file with sentences (one line per sentence).

Arguments:
- `-f` / `--file`: the input file
- `-n` / `--number` (default: 10): the number of sentences to generate
- `-m`/ `--markov` (default: 3): the number of forward word: bigger values means more realistic sentences, but less variation from original sentences
- `-o` / `--output`: the output file where the sentences will be written
- `-p` / `--print` (default: `False`): if set, the sentences will be printed in the console

Example:
- `py -3 main.py -f data.txt`
  - Generates 10 sentences from `data.txt`, wont't print/write anything
- `py -3 main.py -f data.txt -o output.txt`
  - Generates 10 sentences from `data.txt` and write them into `output.txt`
- `py -3 main.py -f data.txt -n 100 -m 5 -o output.txt -p`
  - Generate 100 sentences from `data.txt`, looking forward for 5 words, write them into `output.txt` and print them in the console
