class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        hashset = set(wordList)
        q = deque()
        q.append((beginWord,1))

        while q:
            word,length = q.popleft()
            
            if word == endWord:
                return length
            
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = word[:i] + ch + word[i+1:]
                    if next_word in hashset:
                        hashset.remove(next_word)
                        q.append((next_word, length + 1))
        
        return 0