use std::fs::read_to_string;

fn main() {

    let mut seeds = Vec::new();
    let file_content = read_to_string("input.txt").unwrap();
    let lines: Vec<&str> = file_content.lines().collect();
    for seed in lines[0].split(' ') {
        if seed.contains(':') {
            continue
        }
        seeds.push((seed.parse::<i64>().unwrap(), 0));
    }
    let mut step = 0;
    for line in &lines[1..] {
        if line.is_empty() {
            step += 1;
            continue
        }
        if line.contains(':') {
            continue
        }
        let values: Vec<i64> = line.split(" ").map(|x| x.parse::<i64>().unwrap()).collect();
        for i in 0..seeds.len() {
            if seeds[i].1 == step {
                continue
            }
            if seeds[i].0 >= values[1] && seeds[i].0 < values[1] + values[2] {
                seeds[i].0 = values[0] + (seeds[i].0 - values[1]);
                seeds[i].1 = step
            }
        }
    }
    println!("{:?}", seeds.into_iter().min().unwrap().0)
}
