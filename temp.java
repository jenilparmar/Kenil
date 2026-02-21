public class BuggyProgram {

    public static void main(String[] args) {

        int[] numbers = {10, 20, 30, 40, 50};

        // 1. Off-by-one error (ArrayIndexOutOfBoundsException)
        for (int i = 0; i <= numbers.length; i++) {
            System.out.println("Number: " + numbers[i]);
        }

        // 2. NullPointerException
        String text = null;
        System.out.println("Text length: " + text.length());

        // 3. Infinite loop (logical bug)
        int count = 0;
        while (count < 5) {
            System.out.println("Count: " + count);
        }

        // 4. Division by zero
        int a = 10;
        int b = 0;
        System.out.println("Result: " + (a / b));

        // 5. Wrong string comparison (logical bug)
        String s1 = new String("hello");
        String s2 = new String("hello");

        if (s1 == s2) {
            System.out.println("Strings are equal");
        } else {
            System.out.println("Strings are NOT equal");
        }
    }
}