import random
import string
from typing import List, Tuple

# Generate random string
def random_string(length: int = 10) -> str:
    """
    Generate a random string of given length.
    """
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate random bytes
def random_bytes(length: int = 16) -> bytes:
    """
    Generate random bytes of given length.
    """
    return bytes(random.randint(0, 255) for _ in range(length))

# Generate random hex string
def random_hex(length: int = 16) -> str:
    """
    Generate a random hexadecimal string.
    """
    return ''.join(random.choices(string.hexdigits[:16], k=length))

# Generate random UUID-like string
def random_uuid_like() -> str:
    """
    Generate a random UUID-like string.
    """
    hex_chars = string.hexdigits[:16]
    return '-'.join([
        ''.join(random.choices(hex_chars, k=8)),
        ''.join(random.choices(hex_chars, k=4)),
        ''.join(random.choices(hex_chars, k=4)),
        ''.join(random.choices(hex_chars, k=4)),
        ''.join(random.choices(hex_chars, k=12))
    ])

# Generate random coordinates
def random_coordinates() -> Tuple[float, float]:
    """
    Generate random latitude and longitude coordinates.
    """
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return (latitude, longitude)

# Generate random weighted choice
def random_weighted_choice(choices: dict) -> str:
    """
    Generate a random choice based on weights.
    choices: dict with values as weights
    """
    items = list(choices.keys())
    weights = list(choices.values())
    return random.choices(items, weights=weights, k=1)[0]

# Generate random date within range
def random_date_string() -> str:
    """
    Generate a random date string.
    """
    year = random.randint(2000, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"{year}-{month:02d}-{day:02d}"

if __name__ == "__main__":
    print("Random7 Generator Examples:")
    print(f"Random string: {random_string(15)}")
    print(f"Random hex: {random_hex(8)}")
    print(f"Random UUID-like: {random_uuid_like()}")
    print(f"Random coordinates: {random_coordinates()}")
    print(f"Random date: {random_date_string()}")
    print(f"Random weighted choice: {random_weighted_choice({'A': 0.5, 'B': 0.3, 'C': 0.2})}")
