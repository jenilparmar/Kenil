"""String utility functions for common operations."""

def capitalize_words(text):
    """Capitalize the first letter of each word."""
    return ' '.join(word.capitalize() for word in text.split())

def reverse_string(text):
    """Reverse a string."""
    return text[::-1]

def count_vowels(text):
    """Count the number of vowels in a string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)
