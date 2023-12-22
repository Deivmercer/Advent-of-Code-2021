use std::collections::HashMap;
use std::fs::read_to_string;

fn main() {

    let mut cards = HashMap::new();
    let mut owned_cards = Vec::new();
    let lines = read_to_string("input.txt").unwrap();
    for line in lines.lines() {
        let card: Vec<&str> = line.split(": ").collect();
        let mut card_numbers = (Vec::new(), Vec::new());
        let numbers: Vec<&str> = card[1].split(" | ").collect();
        for n in numbers[0].split(" ") {
            if !n.is_empty() {
                card_numbers.0.push(n);
            }
        }
        for n in numbers[1].split(" ") {
            if !n.is_empty() {
                card_numbers.1.push(n);
            }
        }
        let card_number = card[0].split(" ").last().unwrap().parse::<i32>().unwrap();
        cards.insert(card_number, card_numbers);
        owned_cards.push(card_number)
    }
    let mut card_number = owned_cards.len();
    let mut i = 0;
    while i < card_number {
        let card = owned_cards[i];
        let mut card_value = 0;
        for n in &cards[&card].1 {
            if cards[&card].0.contains(&n) {
                card_value += 1;
                owned_cards.push(card + card_value);
                card_number += 1;
            }
        }
        i += 1;
        println!("{}", card_number);
    }
    println!("{}", card_number);
}
