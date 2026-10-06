class AnagramChecker:

    def __init__(self):
        with open("sowpod.txt") as f:
           self.word_list = set(word.strip().lower() for word in f)

    
    def is_valid_word(self, word):
        return word.lower() in self.word_list

    def get_anagrams(self, word):
        return [w for w in self.word_list if w != word.lower() and self.is_anagram(word,w)]
   
        anagrams = []
        word = word.lower()
        for w in self.word_list:
            if self.is_anagram(word, w) and word != w:
                anagrams.append(w)
        return anagrams

    def is_anagram(self, word1, word2):
        
        if len(word1) != len(word2):
            return False
        
            return sorted(word1) == sorted(word2)

    