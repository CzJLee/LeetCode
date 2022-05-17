# Design a Word Dictionary data structure that implements an add_word and a search method.
# The add_word method will add the word to the dict if it does not already exist.
# The search will return True if the requested word is in the dict, and False if it does not. 
# The user can use the '.' character as a search wildcard substitute for any character. 

from collections import defaultdict

class WordDict:
    def __init__(self):
        # Each element in character index is a dict mapping the letter to a set of words, where the index of the list represents the character position
        self.character_index = []

    def add_word(self, word: str) -> None:
        for i, char in enumerate(word):
            try:
                dict_at_index = self.character_index[i]
            except IndexError:
                self.character_index.append(defaultdict(set))
                dict_at_index = self.character_index[i]

            # Add the word to the set for that character 
            dict_at_index[char].add(word)

    def search(self, word: str) -> bool:
        search_results = None
        for i, char in enumerate(word):
            try:
                dict_at_index = self.character_index[i]
                if char == ".":
                    list_of_possible_word_sets = list(dict_at_index.values())
                    possible_words = set()
                    for word_set in list_of_possible_word_sets:
                        possible_words = possible_words.union(word_set)
                else:
                    possible_words = dict_at_index[char]

                if search_results is None:
                    search_results = possible_words
                else:
                    search_results = search_results.intersection(possible_words)
            except IndexError:
                return False
        
        search_results_of_proper_length = set()
        word_length = len(word)
        for result in search_results:
            if len(result) == word_length:
                search_results_of_proper_length.add(result)

        if search_results_of_proper_length is None:
            return False
        if len(search_results_of_proper_length) > 0:
            return search_results_of_proper_length
        else:
            return False

import time
if __name__ == "__main__":
    all_words = set()

    start_time = time.perf_counter()
    with open("/usr/share/dict/words", "r") as f:
        for word in f:
            all_words.add(word.strip().lower())

    print(f"Read all words in {time.perf_counter() - start_time} seconds")
    

    # Add all words to dict

    word_dict = WordDict()

    start_time = time.perf_counter()
    for word in all_words:
        word_dict.add_word(word)

    print(f"Add all words to dict in {time.perf_counter() - start_time} seconds")

    examples = [
        "cow",
        "ho...",
        ".......",
        "help",
        "compu.er",
        "bxieysd.",
        "................",
        "platypus",
        "name",
        "words",
        "g....e"
    ]
    
    start_time = time.perf_counter()

    for example in examples:
        if word_dict.search(example):
            print(f"The search term '{example}' is found in Word Dict")
            print(f"Matches:")
            for match in word_dict.search(example):
                print(f"\t{match}")
        else:
            print(f"The search term '{example}' NOT found in Word Dict")

    print(f"Searched {len(examples)} words in {time.perf_counter() - start_time} seconds")


