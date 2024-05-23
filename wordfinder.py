"""Word Finder: finds random words from a dictionary."""
import random # ability to generate random variable from provided example

class WordFinder:
    """generates random words from dictionary
    
    >>> wf = WordFinder("/Users/student/words.txt")
    3 words read

    >>> wf.random()
    'cat'

    >>> wf.random()
    'cat'

    >>> wf.random()
    'porcupine'

    >>> wf.random()
    'dog'"""

    def __init__(self, path):
        """Returns number of items read from dictionary"""

        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Read dictionary and returns number of items read"""

        return [w.strip() for w in dict_file]
    
    def random(self):
        """Returns a random word"""

        return random.choice(self.words)

wf = WordFinder("words.txt") # 235886 words read
wf.random() # 'esculin'
wf.random() # 'liespfund'



class SpecialWordFinder(WordFinder):
    """Excludes symbols and blank lines and commands
    
    # Veggies
    kale
    parsnips

    # Fruits
    apple
    mango
    
    will be able to draw from list and ignore the comments
    """

    def parse(self, dict_file):
        """parse skips blanks/comments"""

        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]
    
swf = SpecialWordFinder("special.txt") # 4 words read
