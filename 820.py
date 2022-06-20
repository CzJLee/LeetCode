# https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_reversed = [word[::-1] for word in words]
        words_reversed.sort()
        
        # Find all words that have an overlaping stem
        # Iterate through the reversed list, removing any prefixed substrings 
        # If a word is not a prefix to the following word, keep it
        
        # List of valid words to keep (non overlapping)
        valid_words = []
        # Iterate over every word but the last. The last is guaranteed to not be a suffix substring. 
        for i in range(len(words_reversed) - 1):
            # If the prior word is a substring of the latter word, and the prefix of the reversed word matches the next word
            # Then we discard it. 
            if words_reversed[i] in words_reversed[i+1] and words_reversed[i] == words_reversed[i+1][:len(words_reversed[i])]:
                pass
            else:
                valid_words.append(words_reversed[i])
        valid_words.append(words_reversed[-1])
        
        # Sum the total number of characters 
        num_words = len(valid_words) # Add a "#" for each word
        char_sum = reduce(lambda x, y: x + len(y), valid_words, num_words)
        return char_sum