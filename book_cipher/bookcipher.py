import re
from typing import List, Tuple

class BookCipher:
    def __init__(self, book_path: str):
        self.book_path = book_path
        self.index = self._create_index()

    def _create_index(self) -> dict:
        index = {}
        with open(self.book_path, 'r', encoding='utf-8') as file:
            for page_number, page in enumerate(file.readlines(), start=1):
                # Split page into lines and then words
                for line_number, line in enumerate(page.splitlines(), start=1):
                    words = re.findall(r"\b\w+\b", line.lower())
                    for word_number, word in enumerate(words, start=1):
                        if word not in index:
                            index[word] = []
                        index[word].append((page_number, line_number, word_number))
        return index

    def encrypt(self, message: str) -> List[Tuple[int, int, int]]:
        message_words = message.lower().split()
        encrypted_message = []
        for word in message_words:
            if word in self.index:
                # Use the first occurrence for simplicity (can be randomized for more security)
                encrypted_message.append(self.index[word][0])
            else:
                raise ValueError(f"Word '{word}' not found in the key book.")
        return encrypted_message

    def decrypt(self, indices: List[Tuple[int, int, int]]) -> str:
        book_lines = []
        with open(self.book_path, 'r', encoding='utf-8') as file:
            book_lines = file.readlines()
        decrypted_message = []
        for (page, line, word) in indices:
            # Extract the target line and find the word
            line_text = book_lines[page - 1].splitlines()[line - 1]
            words = re.findall(r"\b\w+\b", line_text.lower())
            if 1 <= word <= len(words):
                decrypted_message.append(words[word - 1])
            else:
                raise ValueError(f"Invalid index ({page}, {line}, {word}).")
        return ' '.join(decrypted_message)

# Example usage:
cipher = BookCipher('pride_and_prejudice.txt')
encoded = cipher.encrypt("hello world")
print(f"Encrypted: {encoded}")
decoded = cipher.decrypt(encoded)
print(f"Decrypted: {decoded}")
