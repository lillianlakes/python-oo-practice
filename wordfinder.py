from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary.

    >>> wf = WordFinder("/usr/share/dict/words")
    235886 words read

    >>> type(wf.random())
    <class 'str'>

    """

    def __init__(self, file_path):
        """Reads a file containing different words on each line and makes an attribute of a list of those words,
        then prints out the number of words read"""
        self.file_path = file_path
        self.file = open(file_path)
        self.words = []
        self.create_words()
        self.print_message()

    def __repr__(self):
        """Describes this class"""

        return f'<{self.__class__} file_path={self.file_path}>'

    def create_words(self):
        """Turns the file into a list of words"""

        self.words = [word.strip() for word in self.file]

    def print_message(self):
        """Prints a message with the number of words read"""

        self.message = f"{len(self.words)} words read"
        print(self.message)

    def random(self):
        """Selects a random word for the list"""

        return choice(self.words)


class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary, with blanks and lines starting with the # symbol removed.

    >>> type(wf.random())
    str

    """

    def create_words(self):
        """Turns the file into a list of words without blanks and lines starting with the # symbol"""

        super().create_words()
        self.words = [
            word for word in self.words if word and not word.startswith('#')]
