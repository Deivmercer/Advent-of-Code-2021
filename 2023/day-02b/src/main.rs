use std::fs::read_to_string;

fn main() {

    let mut sum = 0;
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut red = 0;
        let mut green = 0;
        let mut blue = 0;
        let game: Vec<&str> = line.split(": ").collect();
        for game in game[1].split("; ") {
            for cubes in game.split(", ") {
                let split: Vec<&str> = cubes.split(" ").collect();
                let cube_number = split[0].parse::<i32>().unwrap();
                match split[1] {
                    "red" => {
                        if cube_number > red {
                            red = cube_number
                        }
                    },
                    "green" => {
                        if cube_number > green {
                            green = cube_number
                        }
                    },
                    "blue" => {
                        if cube_number > blue {
                            blue = cube_number
                        }
                    },
                    _ => {}
                }
            }
        }
        sum += red * green * blue;
    }
    println!("{}", sum)
}
