#include <stdio.h>
#include <string.h>

int main() {
    int numbers[] = {10, 20, 30, 40, 50};
    int size = sizeof(numbers) / sizeof(numbers[0]);

    // 1. Off-by-one error (ArrayIndexOutOfBoundsException)
    for (int i = 0; i < size; i++) {
        printf("Number: %d\n", numbers[i]);
    }

    // 2. NullPointerException
    char text[] = "hello";
    if (strlen(text) > 0) {
        printf("Text length: %lu\n", strlen(text));
    }

    // 3. Infinite loop (logical bug)
    int count = 0;
    while (count < 5) {
        printf("Count: %d\n", count);
        count++;
    }

    // 4. Division by zero
    int a = 10;
    int b = 2;
    if (b != 0) {
        printf("Result: %d\n", a / b);
    }

    // 5. Wrong string comparison (logical bug)
    char s1[] = "hello";
    char s2[] = "hello";

    if (strcmp(s1, s2) == 0) {
        printf("Strings are equal\n");
    } else {
        printf("Strings are NOT equal\n");
    }

    return 0;
}