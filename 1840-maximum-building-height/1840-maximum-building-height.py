class Solution:
    def maxBuilding(self, n: int, restrictions: List[List[int]]) -> int:
        restrictions.append([1, 0])
        has_n = False
        for b, h in restrictions:
            if b == n:
                has_n = True
                break

        if not has_n:
            restrictions.append([n, n - 1])

        restrictions.sort()

        m = len(restrictions)

        # Forward pass
        for i in range(1, m):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i - 1][1] +
                (restrictions[i][0] - restrictions[i - 1][0])
            )

        # Backward pass
        for i in range(m - 2, -1, -1):
            restrictions[i][1] = min(
                restrictions[i][1],
                restrictions[i + 1][1] +
                (restrictions[i + 1][0] - restrictions[i][0])
            )

        ans = 0

        for i in range(1, m):
            id1, h1 = restrictions[i - 1]
            id2, h2 = restrictions[i]

            d = id2 - id1
            peak = (h1 + h2 + d) // 2

            ans = max(ans, peak)

        return ans