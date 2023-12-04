use std::fs::read_to_string;

fn main() {

    let mut result = 0;
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut winning_numbers: Vec<&str> = Vec::new();
        let numbers: Vec<&str> = line.split(": ").last().unwrap().split(" | ").collect();
        for n in numbers[0].split(" ") {
            if !n.is_empty() {
                winning_numbers.push(n);
            }
        }
        let mut card_value = 0;
        for n in numbers[1].split(" ") {
            if winning_numbers.contains(&n) {
                if card_value == 0 {
                    card_value = 1;
                } else {
                    card_value *= 2;
                }
            }
        }
        result += card_value;
    }
    println!("{}", result);
}
