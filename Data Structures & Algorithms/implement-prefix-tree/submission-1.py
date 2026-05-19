class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False

    def get_child(self, char):
        if char not in self.children:
            return None
        return self.children[char]

    def add_child(self, char):
        self.children[char] = TrieNode()

    def is_end(self):
        return self.end_of_word

    def set_end(self):
        self.end_of_word = True

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        word_ptr = 0

        curr = self.root
        while word_ptr < len(word) and curr.get_child(word[word_ptr]):
            curr = curr.get_child(word[word_ptr])
            word_ptr += 1

        while word_ptr < len(word):
            curr.add_child(word[word_ptr])
            curr = curr.get_child(word[word_ptr])
            word_ptr += 1
        
        curr.set_end()

    def search(self, word: str) -> bool:
        word_ptr = 0

        curr = self.root
        while word_ptr < len(word) and curr.get_child(word[word_ptr]):
            curr = curr.get_child(word[word_ptr])
            word_ptr += 1

        if word_ptr != len(word) or (curr and not curr.is_end()):
            return False

        return True

    def startsWith(self, prefix: str) -> bool:
        word_ptr = 0

        curr = self.root
        while word_ptr < len(prefix) and curr.get_child(prefix[word_ptr]):
            curr = curr.get_child(prefix[word_ptr])
            word_ptr += 1

        if word_ptr != len(prefix):
            return False

        return True
        