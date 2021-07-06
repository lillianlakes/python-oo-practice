from random import choice


class WordFinder:

    """Word Finder: finds random words from a dictionary."""

    def __init__(self, file_path):
        """Open up a file containing different words in each line and call create_words_list method"""

        self.file = open(file_path)
        self.words_list = []
        self.create_words_list()

    def create_words_list(self):
        """Turn the file into a list of words"""

        for word in self.file:
            word = word.strip()
            self.words_list.append(word)
        print(f"{len(self.words_list)} words read")

    def random(self):
        """Select a random word for the list"""
        return choice(self.words_list)

