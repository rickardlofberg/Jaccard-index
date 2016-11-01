from collections import Counter as C

class WordSet():

    def __init__(self, setOfWords):
        self._setOfWords = set(setOfWords)

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
        bestIndex, bestWord = 0.0, ''
        new = float()
        for word2 in self._setOfWords:
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
        

