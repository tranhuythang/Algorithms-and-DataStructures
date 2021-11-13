import collections
class Solution:
    def __init__(self):
        self.result = None
        self.current_setup = None
        self.n = None

    def is_valid_position(self, k, x, y):
        if k <= 0:
            return True
        else:
            kx, ky = self.current_setup[k - 1][0], self.current_setup[k - 1][1]
            if (x == kx) or (y == ky) or (y == x + (ky - kx)) or (y == (ky + kx) - x):
                return False
            else:
                return self.is_valid_position(k - 1, x, y)

    def place_queen(self, i):
        coordinate2string = lambda x : str(x[0]) + ',' + str(x[1])

        y = i
        for x in range(self.n):
            if self.is_valid_position(i, x, y):
                self.current_setup[i] = [x, y]
                if i < self.n - 1:
                    self.place_queen(i + 1)
                else:
                    isPresent = False
                    for s in self.result:
                        if collections.Counter(list(map(coordinate2string, s))) == collections.Counter(list(map(coordinate2string, self.current_setup))):
                            isPresent = True
                            break
                    if not isPresent:
                        self.result.append(self.current_setup[::])

    def QueensOnChessBoard(self, n):
        """
        :param n:
        :return:
        """
        self.n = n
        self.result = []
        self.current_setup = [[-1, -1] for i in range(self.n)]
        self.place_queen(0)
        return self.result

test = [4, 5, 6, 7, 8]
sol = Solution()

for n in test:
    result = sol.QueensOnChessBoard(n)
    print("****** n = ", n, '-', len(result))
    for s in result:
        print('--------')
        temp = [["_" for j in range(n)] for i in range(n)]
        for t in s:
            temp[t[1]][t[0]] = "x"
        for j in temp:
            print(j)




