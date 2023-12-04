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
        owned_cards.push(1);
    }

    let mut result = owned_cards.len() as i32;
    while !owned_cards.iter().all(|&n| n == 0) {
        let mut i = 0;
        while i < owned_cards.len() {
            let card = &cards[&(i as i32 + 1)];
            let mut card_value = 0;
            for n in &card.1 {
                if card.0.contains(&n) {
                    card_value += 1;
                    owned_cards[i + card_value] += owned_cards[i];
                    result += owned_cards[i];
                }
            }
            owned_cards[i] = 0;
            i += 1;
        }
    }
    println!("{}", result);
}
