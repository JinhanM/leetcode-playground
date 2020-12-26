class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.s = compressedString
        self.p = 0
        self.num = 0
        self.c = ' '
    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            if self.num == 0:
                self.c = self.s[self.p]
                self.p += 1
                while self.p < len(self.s) and self.isNum(self.s[self.p]):
                    self.num = self.num * 10 + int(self.s[self.p])
                    self.p += 1
            self.num -= 1
            return self.c
        else:
            return ' '
    def hasNext(self):
        """
        :rtype: bool
        """
        return self.num != 0 or self.p < len(self.s)

    def isNum(self, n):
        if ord('0') <= ord(n) <= ord('9'):
            return True
        else:
            return False




# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()