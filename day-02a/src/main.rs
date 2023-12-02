use std::fs::read_to_string;

fn main() {

    let mut sum = 0;
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut possible = true;
        let game: Vec<&str> = line.split(": ").collect();
        for game in game[1].split("; ") {
            for cubes in game.split(", ") {
                let split: Vec<&str> = cubes.split(" ").collect();
                let cube_number = split[0].parse::<i32>().unwrap();
                match split[1] {
                    "red" => {
                        if cube_number > 12 {
                            possible = false;
                            break
                        }
                    },
                    "green" => {
                        if cube_number > 13 {
                            possible = false;
                            break
                        }
                    },
                    "blue" => {
                        if cube_number > 14 {
                            possible = false;
                            break
                        }
                    },
                    _ => {}
                }
            }
            if !possible {
                break
            }
        }
        if possible {
            sum += game[0].split(" ").last().unwrap().parse::<i32>().unwrap();
        }
    }
    println!("{}", sum)
}
