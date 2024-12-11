"""
 ┓    ┓      ┓
┏┫┓┏┓┏┣┓┏┓┏┓┏┫
┗┻┗┻┗┫┛┗┗┻┛ ┗┻
     ┛
AoC Day 11 
"""
from collections import Counter # Keep it simple stupid

class PebblesMeditation:
    def __init__(self, init_stones):
        """
        init the PebblesMeditation with the initial arrangement of stones.
        :param init_stones: List of integers representing the initial stones.
        """
        self.stones = Counter(init_stones)

    def blink(self):
        """
        simul a single blink and update the state of the stones based on the rules.
        """
        new_stones = Counter()

        for stone, count in self.stones.items():
            if stone == 0:
                # Rule 1: Replace 0 with 1
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                # Rule 2: split even-digit number into two stones
                digits = str(stone)
                mid = len(digits) // 2
                left, right = int(digits[:mid]), int(digits[mid:])
                new_stones[left] += count
                new_stones[right] += count # again, KISS
            else:
                # Rule 3: replace with number multiplied by 2024
                new_stones[stone * 2024] += count

        self.stones = new_stones

    def s_blinks(self, blinks):
        """
        sim the given number of blinks.
        :param blinks: mumber of blinks to simulate.
        """
        for _ in range(blinks):
            self.blink()

    def get_stone_count(self):
        """
        Get the current number of stones.
        """
        return sum(self.stones.values())

if __name__ == "__main__":
    # read the input from file
    with open('./day_11/day11.txt', 'r') as file:
        puzzle_input = file.read().strip()

    init_stones = list(map(int, puzzle_input.split()))

    # Create the PebblesMeditation instance
    pebbles = PebblesMeditation(init_stones)

    # Simulate 25 blinks for Part 1
    pebbles.s_blinks(25)
    print("# stones after 25 blinks (Part 1):", pebbles.get_stone_count())

    # Reset and simulate 75 blinks for Part 2
    pebbles = PebblesMeditation(init_stones)
    pebbles.s_blinks(75)
    print("# stones after 75 blinks (Part 2):", pebbles.get_stone_count())
