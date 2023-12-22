use std::fs::read_to_string;

fn main() {

    let file_content = read_to_string("input.txt").unwrap();
    let lines: Vec<&str> = file_content.lines().collect();
    let time = lines[0].replace(' ', "").split(':').last().unwrap().parse::<i64>().unwrap();
    let distance = lines[1].replace(' ', "").split(':').last().unwrap().parse::<i64>().unwrap();
    let mut result = 0;
    for j in 0..time {
        if (time - j) * j > distance {
            result += 1;
        }
    }
    println!("{}", result);
}
