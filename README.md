How It Works:
Initialization: Loads the book file and creates an index of all words with their locations

Encryption:

Splits the message into words

Looks up each word in the index

Returns the coordinates (page, line, word position)

Decryption:

Takes the coordinates

Looks up each word in the original book

Reconstructs the original message

1. Handling Page vs. Line Numbers
Challenge:
The original code confused physical pages with lines. Books have pages containing multiple lines, but the initial implementation treated each line as a separate "page."

Solution:

Introduced a configurable page_size parameter (default: 40 lines per page).

Tracked absolute line numbers while calculating page numbers dynamically.

Example:

python
if lines_in_page >= self.page_size:
    current_page += 1
    lines_in_page = 0
2. Word Matching and Tokenization
Challenge:
Simple word splitting (e.g., split()) failed to handle contractions ("don’t") or hyphenated words ("state-of-the-art").

Solution:

Used regex with r"\b[\w'-]+\b" to properly tokenize words:

python
words = re.findall(r"\b[\w'-]+\b", line.lower())
This matches:

Alphanumeric words (\w).

Apostrophes (e.g., "don’t").

Hyphens (e.g., "state-of-the-art").