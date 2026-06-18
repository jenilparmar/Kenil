import random
import secrets
from typing import List, Tuple

class RandomNumberGenerator:
    """A comprehensive random number generator with various utilities."""
    
    def __init__(self, seed=None):
        """Initialize the random number generator with an optional seed."""
        if seed is not None:
            random.seed(seed)
    
    def generate_int(self, start: int = 0, end: int = 100) -> int:
        """Generate a random integer between start and end (inclusive)."""
        return random.randint(start, end)
    
    def generate_float(self, start: float = 0.0, end: float = 1.0) -> float:
        """Generate a random float between start and end."""
        return random.uniform(start, end)
    
    def generate_choice(self, items: List) -> any:
        """Randomly select an item from a list."""
        return random.choice(items)
    
    def generate_sample(self, items: List, k: int) -> List:
        """Generate a random sample of k items from a list without replacement."""
        return random.sample(items, k)
    
    def generate_shuffle(self, items: List) -> List:
        """Shuffle a list randomly in-place and return it."""
        random.shuffle(items)
        return items
    
    def generate_secure_random(self, length: int = 16) -> str:
        """Generate a cryptographically secure random string."""
        return secrets.token_hex(length)
    
    def generate_random_list(self, size: int, start: int = 0, end: int = 100) -> List[int]:
        """Generate a list of random integers."""
        return [random.randint(start, end) for _ in range(size)]
    
    def generate_random_matrix(self, rows: int, cols: int, start: int = 0, end: int = 100) -> List[List[int]]:
        """Generate a matrix of random integers."""
        return [[random.randint(start, end) for _ in range(cols)] for _ in range(rows)]
    
    def generate_weighted_choice(self, items: List, weights: List[float]) -> any:
        """Select an item based on weighted probabilities."""
        return random.choices(items, weights=weights, k=1)[0]


if __name__ == "__main__":
    # Example usage
    rng = RandomNumberGenerator(seed=42)
    
    print("Random Integer (0-100):", rng.generate_int())
    print("Random Float (0-1):", rng.generate_float())
    print("Random Choice:", rng.generate_choice(['apple', 'banana', 'cherry']))
    print("Random List:", rng.generate_random_list(5))
    print("Secure Random String:", rng.generate_secure_random())
    print("Weighted Choice:", rng.generate_weighted_choice(['A', 'B', 'C'], [0.5, 0.3, 0.2]))
