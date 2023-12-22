use std::fs::read_to_string;

fn main() {

    let mut sum = 0;
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut chars = vec![' ', ' '];
        for c in line.chars() {
            if c.is_numeric() {
                if chars[0] == ' ' {
                    chars[0] = c;
                }
                chars[1] = c;
            }
        }
        sum += String::from_iter(chars).parse::<i32>().unwrap();
    }
    println!("{}", sum)
}