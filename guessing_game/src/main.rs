// Import the input library
use std::io;
// Import the random number generator library
use rand::Rng;
// Import the library to compare between two values
use std::cmp::Ordering;

fn main() {
    println!("Guess the number!");

    // Generate a random number between 1 and 101
    let secret_number = rand::thread_rng().gen_range(1..=100);
    println!("The secret number is: {}", secret_number);

    println!("Please input your guess.");

    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");

    // Convert the input guess to a number
    let guess: u32 = match guess.trim().parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Please enter a valid number.");
            return;
        }
    };

    println!("You guessed: {}", guess);

    // Compare guess to the secret number and provide feedback
    match guess.cmp(&secret_number) {
        Ordering::Less => println!("Too small!"),
        Ordering::Greater => println!("Too big!"),
        Ordering::Equal => println!("You win!"),
    }
}
