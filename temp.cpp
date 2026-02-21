#include <iostream>
#include <vector>
#include <string>

void main() {
    std::vector<int> numbers = {10, 20, 30, 40, 50};

    // 1. Off-by-one error (ArrayIndexOutOfBoundsException)
    for (int i = 0; i < numbers.size(); i++) {
        std::cout << "Number: " << numbers[i] << std::endl;
    }

    // 2. NullPointerException
    std::string text = "hello";
    if (!text.empty()) {
        std::cout << "Text length: " << text.length() << std::endl;
    }

    // 3. Infinite loop (logical bug)
    int count = 0;
    while (count < 5) {
        std::cout << "Count: " << count << std::endl;
        count++;
    }

    // 4. Division by zero
    int a = 10;
    int b = 2;
    if (b != 0) {
        std::cout << "Result: " << (a / b) << std::endl;
    }

    // 5. Wrong string comparison (logical bug)
    std::string s1 = "hello";
    std::string s2 = "hello";

    if (s1 == s2) {
        std::cout << "Strings are equal" << std::endl;
    } else {
        std::cout << "Strings are NOT equal" << std::endl;
    }
}