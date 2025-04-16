import csv
from collections import defaultdict

# Output structures
dictionary = {}             # word -> list of definition words
word_types = {}             # word -> type (like 'n', 'v', etc.)
all_def_words = []          # flat list of all words in all definitions (for counting)

# Load from CSV
with open("ginger_words.csv", encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 3:
            continue  # skip bad rows

        word = row[0].strip()
        word_type = row[1].strip().rstrip('.')  # remove trailing dot
        definition = row[2].strip().replace('.', '')  # remove periods in definition

        def_words = definition.split()

        dictionary[word] = def_words
        word_types[word] = word_type
        all_def_words.extend(def_words)
