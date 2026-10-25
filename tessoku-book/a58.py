class rmq:
    def __init__(self, n):
        self.size = n
        self.dat = [-1] * (2*n + 1)

    def update(self, pos, x):
        pos = pos + self.size
        self.dat[pos] = x
        while pos >= 2:
            pos //= 2
            self.dat[pos] = max(self.dat[pos * 2], self.dat[pos*2 + 1])

    def query(self, l, r, a, b, u):
        if r <= a or b <= l: return -100000000000
        if l <= a and b <= r: return self.dat[u]

        m = (a + b) // 2
        AnswerL = self.query(l, r, a, m, u * 2)
        AnswerR = self.query(l, r, m, b, u * 2 + 1)
        return max(AnswerL, AnswerR)