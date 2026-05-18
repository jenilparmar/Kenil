import random
import secrets
from typing import List, Tuple


class RandomNumberGenerator:
    """A class for generating random numbers with various distributions."""

    @staticmethod
    def generate_integer(start: int = 0, end: int = 100) -> int:
        """Generate a random integer between start and end (inclusive)."""
        return random.randint(start, end)

    @staticmethod
    def generate_float(start: float = 0.0, end: float = 1.0) -> float:
        """Generate a random float between start and end."""
        return random.uniform(start, end)

    @staticmethod
    def generate_integers(count: int, start: int = 0, end: int = 100) -> List[int]:
        """Generate a list of random integers."""
        return [random.randint(start, end) for _ in range(count)]

    @staticmethod
    def generate_floats(count: int, start: float = 0.0, end: float = 1.0) -> List[float]:
        """Generate a list of random floats."""
        return [random.uniform(start, end) for _ in range(count)]

    @staticmethod
    def generate_choice(choices: List) -> any:
        """Return a random element from the given sequence."""
        return random.choice(choices)

    @staticmethod
    def generate_choices(choices: List, count: int, allow_duplicates: bool = True) -> List:
        """Generate multiple random choices from the given sequence."""
        if allow_duplicates:
            return [random.choice(choices) for _ in range(count)]
        else:
            return random.sample(choices, count)

    @staticmethod
    def generate_shuffle(items: List) -> List:
        """Return a shuffled copy of the given list."""
        shuffled = items.copy()
        random.shuffle(shuffled)
        return shuffled

    @staticmethod
    def generate_secure_random(length: int = 16) -> str:
        """Generate a secure random string of given length."""
        return secrets.token_hex(length)

    @staticmethod
    def generate_weighted_choice(choices: List, weights: List[float]) -> any:
        """Generate a random choice based on weighted probabilities."""
        return random.choices(choices, weights=weights, k=1)[0]


if __name__ == "__main__":
    rng = RandomNumberGenerator()
    
    print("Random Integer (0-100):", rng.generate_integer())
    print("Random Float (0.0-1.0):", rng.generate_float())
    print("5 Random Integers:", rng.generate_integers(5))
    print("3 Random Floats:", rng.generate_floats(3))
    print("Random Choice from list:", rng.generate_choice([1, 2, 3, 4, 5]))
    print("Secure Random Token:", rng.generate_secure_random())
