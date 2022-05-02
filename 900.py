# https://leetcode.com/problems/rle-iterator/submissions/

class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.run_length = encoding

    def next(self, n: int) -> int:
        while n > 0:
            if len(self.run_length) == 0:
                return -1
            
            if self.run_length[0] == 0:
                self.run_length.pop(0)
                self.run_length.pop(0)
            elif self.run_length[0] > n:
                self.run_length[0] -= n
                n -= n
            elif self.run_length[0] < n:
                n -= self.run_length[0]
                self.run_length[0] = 0
            else:
                self.run_length[0] -= 1
                n -= 1

        return self.run_length[1]



# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)