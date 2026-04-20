class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l = 0
        r = len(matrix[0])-1
        t = 0
        b = len(matrix)-1

        res = []

        direction = 1

        while len(res) < len(matrix) * len(matrix[0]):
            if direction % 4 == 1:
                for i in range(l, r+1):
                    res.append(matrix[t][i])
                t += 1
            elif direction % 4 == 2:
                for i in range(t, b+1):
                    res.append(matrix[i][r])
                r -= 1
            elif direction % 4 == 3:
                for i in range(r, l-1, -1):
                    res.append(matrix[b][i])
                b -= 1
            else:
                for i in range(b, t-1, -1):
                    res.append(matrix[i][l])
                l += 1
            direction += 1

        return res
