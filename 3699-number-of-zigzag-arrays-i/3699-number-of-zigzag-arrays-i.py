class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [0] * m
        down = [0] * m

        for x in range(m):
            up[x] = x
            down[x] = m - x - 1

        for _ in range(3, n + 1):

            pref_down = [0] * m
            pref_down[0] = down[0]
            for i in range(1, m):
                pref_down[i] = (pref_down[i-1] + down[i]) % MOD

            suff_up = [0] * m
            suff_up[-1] = up[-1]
            for i in range(m-2, -1, -1):
                suff_up[i] = (suff_up[i+1] + up[i]) % MOD

            new_up = [0] * m
            new_down = [0] * m

            for y in range(m):
                if y > 0:
                    new_up[y] = pref_down[y-1]

                if y < m-1:
                    new_down[y] = suff_up[y+1]

            up, down = new_up, new_down

        return (sum(up) + sum(down)) % MOD