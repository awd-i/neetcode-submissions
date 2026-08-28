from collections import defaultdict
class PrefixNode:
    def __init__(self, c):
        self.char = c
        self.children = {}
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        if not word:
            return

        if word[0] not in self.root:
            self.root[word[0]] = PrefixNode(word[0])

        node = self.root[word[0]]
        
        if len(word) > 1:
            for c in word[1:]:
                if c not in node.children:
                    node.children[c] = PrefixNode(c[0])
                node = node.children[c] # keep traversing down the node
    
        node.is_end_of_word = True

            
    def search(self, word: str) -> bool:
        if not word:
            return
            
        if word[0] not in self.root:
            return False

        node = self.root[word[0]]

        if len(word) == 1:
            return node.is_end_of_word
        
        for c in word[1:]:
            if c not in node.children:
                return False
            node = node.children[c]

        return node.is_end_of_word
        

    def startsWith(self, prefix: str) -> bool:
        if not prefix:
            return
            
        if prefix[0] not in self.root:
            return False
        
        if len(prefix) == 1:
            return True

        node = self.root[prefix[0]]
        
        for c in prefix[1:]:
            if c not in node.children:
                return False
            node = node.children[c]
        
        return True
        
        