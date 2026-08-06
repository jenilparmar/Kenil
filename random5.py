import random
import numpy as np
from typing import List, Tuple, Optional

class AdvancedRandomGenerator:
    """Advanced random number generator with statistical distributions and utilities."""
    
    def __init__(self, seed: Optional[int] = None):
        """Initialize the advanced random generator."""
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
    
    def gaussian_distribution(self, mean: float = 0.0, std_dev: float = 1.0, size: int = 1) -> List[float]:
        """Generate random numbers from a Gaussian (normal) distribution."""
        return np.random.normal(mean, std_dev, size).tolist()
    
    def uniform_distribution(self, low: float = 0.0, high: float = 1.0, size: int = 1) -> List[float]:
        """Generate random numbers from a uniform distribution."""
        return np.random.uniform(low, high, size).tolist()
    
    def exponential_distribution(self, scale: float = 1.0, size: int = 1) -> List[float]:
        """Generate random numbers from an exponential distribution."""
        return np.random.exponential(scale, size).tolist()
    
    def poisson_distribution(self, lam: float = 1.0, size: int = 1) -> List[int]:
        """Generate random numbers from a Poisson distribution."""
        return np.random.poisson(lam, size).tolist()
    
    def binomial_distribution(self, n: int, p: float, size: int = 1) -> List[int]:
        """Generate random numbers from a binomial distribution."""
        return np.random.binomial(n, p, size).tolist()
    
    def beta_distribution(self, alpha: float, beta: float, size: int = 1) -> List[float]:
        """Generate random numbers from a beta distribution."""
        return np.random.beta(alpha, beta, size).tolist()
    
    def gamma_distribution(self, shape: float, scale: float = 1.0, size: int = 1) -> List[float]:
        """Generate random numbers from a gamma distribution."""
        return np.random.gamma(shape, scale, size).tolist()
    
    def random_permutation(self, n: int) -> List[int]:
        """Generate a random permutation of integers from 0 to n-1."""
        return np.random.permutation(n).tolist()
    
    def random_combinations(self, items: List, r: int) -> List[Tuple]:
        """Generate random combinations of items."""
        from itertools import combinations
        all_combinations = list(combinations(items, r))
        num_samples = min(10, len(all_combinations))
        return random.sample(all_combinations, num_samples)
    
    def monte_carlo_pi(self, num_samples: int = 100000) -> float:
        """Estimate pi using Monte Carlo method."""
        inside = 0
        for _ in range(num_samples):
            x = random.random()
            y = random.random()
            if x*x + y*y <= 1:
                inside += 1
        return (inside / num_samples) * 4
    
    def random_walk_1d(self, steps: int = 100, start: int = 0) -> List[int]:
        """Generate a 1D random walk."""
        position = start
        walk = [position]
        for _ in range(steps):
            position += random.choice([-1, 1])
            walk.append(position)
        return walk
    
    def random_walk_2d(self, steps: int = 100) -> Tuple[List[int], List[int]]:
        """Generate a 2D random walk."""
        x, y = 0, 0
        x_path, y_path = [x], [y]
        for _ in range(steps):
            dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            x += dx
            y += dy
            x_path.append(x)
            y_path.append(y)
        return x_path, y_path


if __name__ == "__main__":
    # Example usage
    rng = AdvancedRandomGenerator(seed=42)
    
    print("Gaussian Distribution:", rng.gaussian_distribution(mean=0, std_dev=1, size=5))
    print("Uniform Distribution:", rng.uniform_distribution(0, 10, size=5))
    print("Exponential Distribution:", rng.exponential_distribution(scale=2.0, size=5))
    print("Poisson Distribution:", rng.poisson_distribution(lam=3.0, size=5))
    print("Binomial Distribution:", rng.binomial_distribution(n=10, p=0.5, size=5))
    print("Estimated Pi:", rng.monte_carlo_pi(100000))
    print("Random Walk 1D:", rng.random_walk_1d(10))
