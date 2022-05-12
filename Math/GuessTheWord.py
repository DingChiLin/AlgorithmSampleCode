class Solution:
    def matchCount(self, word1, word2):
        return len([i for i in range(len(word1)) if word1[i] == word2[i]])
    
    
    def expectationOfElemination(self, words, target):
        chanceOfMatchCnt = [0,0,0,0,0,0,0]
        for word in words:
            matchCnt = self.matchCount(word, target)
            chanceOfMatchCnt[matchCnt] += 1
        
        chanceOfMatchCnt = [n/len(words) for n in chanceOfMatchCnt]
        expectation = 0
        for matchCnt in range(6):
            eliminateCnt = 0
            for word in words:
                if self.matchCount(word, target) != matchCnt:
                    eliminateCnt += 1
            
            expectation += chanceOfMatchCnt[matchCnt] * eliminateCnt
            
        return expectation

    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        candidates = wordlist
        for i in range(10):
            maxExpectation = -inf
            bestChoice = ""
            for word in candidates:
                zeroCnt = 0
                expectation = self.expectationOfElemination(candidates, word)
                if expectation > maxExpectation:
                    maxExpectation = expectation
                    bestChoice = word
            
            matchCnt = master.guess(bestChoice)
            if matchCnt == 6:
                break
                
            newCandidates = []
            for word in candidates:
                if self.matchCount(bestChoice, word) == matchCnt:
                    newCandidates.append(word)
            candidates = newCandidates