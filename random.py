import random


def generate_random_number(lower: int = 1, upper: int = 100) -> int:
    return random.randint(lower, upper)


if __name__ == "__main__":
    print(generate_random_number())
