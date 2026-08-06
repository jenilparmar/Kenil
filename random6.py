import random
import secrets

# Simple random number generator
def random_int(min_val: int = 0, max_val: int = 100) -> int:
    """
    Generate a random integer between min_val and max_val (inclusive).
    """
    return random.randint(min_val, max_val)

# Generate random float
def random_float(min_val: float = 0.0, max_val: float = 1.0) -> float:
    """
    Generate a random float between min_val and max_val.
    """
    return random.uniform(min_val, max_val)

# Generate secure random number (cryptographically strong)
def secure_random_int(min_val: int = 0, max_val: int = 100) -> int:
    """
    Generate a cryptographically strong random integer.
    """
    return secrets.randbelow(max_val - min_val + 1) + min_val

# Generate random choice from list
def random_choice(items: list):
    """
    Select a random item from a list.
    """
    return random.choice(items)

# Generate random sample from list
def random_sample(items: list, k: int):
    """
    Select k random items from a list without replacement.
    """
    return random.sample(items, k)

# Shuffle a list
def shuffle_list(items: list) -> list:
    """
    Shuffle a list in place and return it.
    """
    random.shuffle(items)
    return items

if __name__ == "__main__":
    print("Random Number Generator Examples:")
    print(f"Random int (0-100): {random_int()}")
    print(f"Random float (0-1): {random_float()}")
    print(f"Secure random int (1-6): {secure_random_int(1, 6)}")
    print(f"Random choice: {random_choice(['apple', 'banana', 'orange'])}")
    print(f"Random sample: {random_sample([1, 2, 3, 4, 5], 3)}")
    print(f"Shuffled list: {shuffle_list([1, 2, 3, 4, 5])}")
