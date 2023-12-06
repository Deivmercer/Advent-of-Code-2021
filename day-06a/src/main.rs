use std::fs::read_to_string;

fn main() {

    let mut time: Vec<i32> = Vec::new();
    let mut distance = Vec::new();
    let file_content = read_to_string("input.txt").unwrap();
    let lines: Vec<&str> = file_content.lines().collect();
    for line in lines[0].split(" ") {
        if line.contains(":") || line.is_empty() {
            continue
        }
        time.push(line.parse::<i32>().unwrap());
    }
    for line in lines[1].split(" ") {
        if line.contains(":") || line.is_empty() {
            continue
        }
        distance.push(line.parse::<i32>().unwrap());
    }
    let mut result = 1;
    for i in 0..time.len() {
        let mut winning_strategies = 0;
        for j in 0..time[i] {
            if (time[i] - j) * j > distance[i] {
                winning_strategies += 1;
            }
        }
        result *= winning_strategies;
    }
    println!("{}", result);
}
