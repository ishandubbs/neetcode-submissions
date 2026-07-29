class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.isWord = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        ROWS = len(board)
        COLS = len(board[0])

        result = set()
        visit = set()

        def dfs(row, column, node, word):
            if (row < 0 or column < 0 or         # out of bounds
                row == ROWS or column == COLS or # out of bounds
                board[row][column] not in node.children or # characters are not in children
                (row, column) in visit):          # tuple is inside of our set
                return

            visit.add((row, column))
            node = node.children[board[row][column]]
            word += board[row][column]
            if node.isWord:
                result.add(word)

            dfs(row - 1, column, node, word) 
            dfs(row + 1, column, node, word) 
            dfs(row, column - 1, node, word) 
            dfs(row, column + 1, node, word)
            visit.remove((row, column))

        for row in range(ROWS):
            for column in range(COLS):
                dfs(row, column, root, "")
        return list(result)