"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    
    def __init__(self, wf):
        '''allows file to have access to txt file and reads it'''
        with open('words.txt', 'r') as f:
            self.words = f.read().split()

    def generate(self):
        '''selects random word from txt file'''
        self.random_word = random.choice(self.words)

    def __repr__(self):
        '''makes word in terminal readible '''
        self.generate()
        return self.random_word


class SpecialWordFinder(WordFinder):

    def generate(self):

        while True:
            '''looks for spaces and # to disregard them'''
            self.random_word = super().generate()
            if self.random_word and not self.random_word.startswith('#'):
                return None

    def __repr__(self):
        self.generate()
        return self.random_word

wf = SpecialWordFinder('words.txt')


#ANSWER
# """Word Finder: finds random words from a dictionary."""

# import random


# class WordFinder:
#     """Machine for finding random words from dictionary.
    
#     >>> wf = WordFinder("simple.txt")
#     3 words read

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True

#     >>> wf.random() in ["cat", "dog", "porcupine"]
#     True
#     """

#     def __init__(self, path):
#         """Read dictionary and reports # items read."""

#         dict_file = open(path)

#         self.words = self.parse(dict_file)

#         print(f"{len(self.words)} words read")

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words."""

#         return [w.strip() for w in dict_file]

#     def random(self):
#         """Return random word."""

#         return random.choice(self.words)


# class SpecialWordFinder(WordFinder):
#     """Specialized WordFinder that excludes blank lines/comments.
    
#     >>> swf = SpecialWordFinder("complex.txt")
#     3 words read

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True

#     >>> swf.random() in ["pear", "carrot", "kale"]
#     True
#     """

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words, skipping blanks/comments."""

#         return [w.strip() for w in dict_file
#                 if w.strip() and not w.startswith("#")]






                



        

        

