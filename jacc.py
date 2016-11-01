from collections import Counter as C

class WordSet():

    def __init__(self, setOfWords):
        """Initiate by adding all the words to a dictionary"""

        # We use this set to quick check for matches
        self._setOfWords = set(setOfWords)

        # The dictionary is used to look for words in a more efficient way
        self._wordDict = {}
        # For word in set to aviod duplicates
        for word in self._setOfWords:
            length = len(word) # Add them to a dictionary depending on their length
            if length not in self._wordDict:
                self._wordDict[length] = {word}
            else:    
                self._wordDict[length].add(word)

    def wordIndex(self, word):
        """Returns a tupple of first word and it's index"""
        if word in self._setOfWords:
            return (word, 1.0)
        return self._findBestMatch(word)

    def _calculateIndex(self, w1, w2):
        """Returns the index value of two words"""
        w1Count, w2Count = C(w1.lower()), C(w2.lower())
        return round(sum((w1Count & w2Count).values()) / sum((w1Count | w2Count).values()), 2)

    def _findBestMatch(self, word):
        # The length in dictionary to check
        lenToCheck = len(word) 

        # Get base case from same length
        bestWord, bestIndex = self._checkDict(word, lenToCheck)

        # Keeps track of increase in word length
        increase = 1

        # We use 'x' as a token character to do the calculation
        # If possible to get better results check next dict
        while bestIndex < self._calculateIndex(word, word + ('x' * increase)):
            lenToCheck += 1
            #print(lenToCheck, bestIndex)
            increase += 1
            newWord, newIndex = self._checkDict(word, lenToCheck)
            if newIndex > bestIndex:
                bestWord, bestIndex = newWord, newIndex

        # Keep track of the decrease 
        decrease = 1
        lenToCheck = len(word) # Reset length of word

        # If there is a chance to get better results, check shorter words
        while bestIndex < self._calculateIndex(word, word[:-decrease]):
            lenToCheck -= 1
            #print(lenToCheck, bestIndex)
            decrease += 1
            newWord, newIndex = self._checkDict(word, lenToCheck)
            if newIndex > bestIndex:
                bestWord, bestIndex = newWord, newIndex

        return (bestWord, bestIndex)

    def _checkDict(self, word, lenOfWord):
        bestIndex, bestWord = 0.0, ''
        new = float()

        for word2 in self._wordDict[lenOfWord]:
            if bestIndex == 1:
                break
            new = self._calculateIndex(word, word2)
            if new > bestIndex:
                bestWord, bestIndex = word2, new
        return (bestWord, bestIndex)


listOfWords = list()
for line in open('ordformer.txt', 'r'):
    listOfWords.append(line.lower().strip())

Jacc = WordSet(listOfWords)

while True:
    try:
        print(Jacc.wordIndex(input("Word to compare: ")))
    except:
        break
        

