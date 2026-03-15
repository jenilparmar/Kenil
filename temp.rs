fn main() {
    let numbers = [10, 20, 30, 40, 50];

    // 1. Off-by-one error (ArrayIndexOutOfBoundsException in Java)
    for number in numbers.iter() {
        println!("Number: {}", number);
    }

    // 2. NullPointerException equivalent in Rust
    let text = Some("hello");
    if let Some(t) = text {
        println!("Text length: {}", t.len());
    }

    // 3. Infinite loop (logical bug in Java)
    let mut count = 0;
    while count < 5 {
        println!("Count: {}", count);
        count += 1;
    }

    // 4. Division by zero
    let a = 10;
    let b = 2;
    if b != 0 {
        println!("Result: {}", a / b);
    }

    // 5. String comparison
    let s1 = String::from("hello");
    let s2 = String::from("hello");

    if s1 == s2 {
        println!("Strings are equal");
    } else {
        println!("Strings are NOT equal");
    }
}