class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            # If out of bounds or at water, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            
            # Mark the land as visited by changing 'L' to 'W'
            grid[r][c] = 'W'

            # Explore all four directions (up, down, left, right)
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L':
                    # Found a new island
                    island_count += 1
                    # Start DFS to mark the whole island
                    dfs(i, j)

        return island_count

# Example usage:
solution = Solution()
map1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"],
]

map2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"],
]

print(solution.getTotalIsles(map1))  # Output: 1
print(solution.getTotalIsles(map2))  # Output: 3
