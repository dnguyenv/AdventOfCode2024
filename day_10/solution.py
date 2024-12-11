"""
      _                   _                         _ 
   __| |  _   _   _   _  | |__     __ _   _ __   __| |
  / _` | | | | | | | | | | '_ \   / _` | | '__| / _` |
 | (_| | | |_| | | |_| | | | | | | (_| | | |   | (_| |
  \__,_|  \__,_|  \__, | |_| |_|  \__,_| |_|    \__,_|
                  |___/                               
AoC Day 10 
"""
class HikingTrailAnalyzer:
    def __init__(self, map_data):
        """
        Initialize the HikingTrailAnalyzer with a 2D height map.
        """
        self.height_map = [list(map(int, line)) for line in map_data.strip().split("\n")]

    def get_trailheads(self):
        """
        Identify all starting positions (trailheads) with height 0.
        """
        return [(r, c) for r, row in enumerate(self.height_map) for c, val in enumerate(row) if val == 0]

    def explore_trails(self, start, distinct=False):
        """
        Explore trails starting from a given trailhead.
        - If distinct is False, count reachable END_OF_TRAIL positions.
        - If distinct is True, count distinct paths to END_OF_TRAIL.
        """
        visited = set()
        paths = set()

        def traverse(position, path):
            r, c = position

            # Base case: check if the trail ends
            if self.height_map[r][c] == 9:
                if distinct:
                    paths.add(tuple(path + [position]))
                else:
                    visited.add(position)
                return

            # Explore valid neighbors
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                neighbor = (nr, nc)
                if 0 <= nr < len(self.height_map) and 0 <= nc < len(self.height_map[0]):
                    if self.height_map[nr][nc] == self.height_map[r][c] + 1:
                        if distinct or neighbor not in visited:
                            traverse(neighbor, path + [position])

        traverse(start, [])
        return len(paths) if distinct else len(visited)

    def calculate_totals(self):
        """
        Calculate total scores and ratings for all trailheads.
        - Score: Count of reachable END_OF_TRAIL positions.
        - Rating: Count of distinct paths to END_OF_TRAIL.
        """
        trailheads = self.get_trailheads()
        total_score = sum(self.explore_trails(head, distinct=False) for head in trailheads)
        total_rating = sum(self.explore_trails(head, distinct=True) for head in trailheads)
        return total_score, total_rating

if __name__ == "__main__":
    with open("./day_10/day10.txt", "r") as file:
        map_data = file.read()

    analyzer = HikingTrailAnalyzer(map_data)
    score, rating = analyzer.calculate_totals()
    print("Sum of scores of all trailheads:", score)
    print("Sum of ratings of all trailheads:", rating)



