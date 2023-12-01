use std::fs::read_to_string;

fn main() {

    let mut sum = 0;
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut chars = vec![' ', ' '];
        for (i, c) in line.chars().enumerate() {
            if c.is_numeric() {
                update_chars(&mut chars, c);
            } else {
                let suffix = &line[i..];
                if suffix.starts_with("one") {
                    update_chars(&mut chars, '1');
                } else if suffix.starts_with("two") {
                    update_chars(&mut chars, '2');
                } else if suffix.starts_with("three") {
                    update_chars(&mut chars, '3');
                } else if suffix.starts_with("four") {
                    update_chars(&mut chars, '4');
                } else if suffix.starts_with("five") {
                    update_chars(&mut chars, '5');
                } else if suffix.starts_with("six") {
                    update_chars(&mut chars, '6');
                } else if suffix.starts_with("seven") {
                    update_chars(&mut chars, '7');
                } else if suffix.starts_with("eight") {
                    update_chars(&mut chars, '8');
                } else if suffix.starts_with("nine") {
                    update_chars(&mut chars, '9');
                }
            }
        }
        sum += String::from_iter(chars).parse::<i32>().unwrap();
    }
    println!("{}", sum)
}

fn update_chars(chars: &mut Vec<char>, c: char) {

    if chars[0] == ' ' {
        chars[0] = c;
    }
    chars[1] = c;
}