import random


def generate_random_number(lower: int = 1, upper: int = 100) -> int:
    return random.randint(lower, upper)


def generate_random_float(lower: float = 0.0, upper: float = 1.0) -> float:
    return random.uniform(lower, upper)


if __name__ == "__main__":
    print(generate_random_number())
    print(generate_random_float())
