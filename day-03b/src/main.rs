use std::fs::read_to_string;

fn main() {

    let mut matrix: Vec<Vec<char>> = Vec::new();
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut row: Vec<char> = Vec::new();
        for c in line.chars() {
            row.push(c);
        }
        matrix.push(row);
    }

    let mut sum = 0;
    for (i, row) in matrix.iter().enumerate() {
        for (j, c) in row.iter().enumerate() {
            if c != &'*' {
                continue
            }

            sum += check_adjacent(&matrix, i, j);
        }
    }
    println!("{}", sum)
}

fn check_adjacent(matrix: &Vec<Vec<char>>, current_row: usize, current_column: usize) -> i32 {

    let mut count = 0;
    let mut gear_value = 1;
    if current_column > 0 && matrix[current_row][current_column - 1].is_numeric() {
        gear_value *= get_value(matrix, current_row, current_column - 1);
        count += 1;
    }
    if current_column < matrix[0].len() && matrix[current_row][current_column + 1].is_numeric() {
        gear_value *= get_value(matrix, current_row, current_column + 1);
        count += 1;
    }
    if current_row > 0 {
        if current_column > 0 && matrix[current_row - 1][current_column].is_numeric() {
            gear_value *= get_value(matrix, current_row - 1, current_column);
            count += 1;
        } else {
            if current_column > 0 && matrix[current_row - 1][current_column - 1].is_numeric() {
                gear_value *= get_value(matrix, current_row - 1, current_column - 1);
                count += 1;
            }
            if current_column < matrix[0].len() && matrix[current_row - 1][current_column + 1].is_numeric() {
                gear_value *= get_value(matrix, current_row - 1, current_column + 1);
                count += 1;
            }
        }
    }
    if current_row < matrix.len() {
        if current_column > 0 && matrix[current_row + 1][current_column].is_numeric() {
            gear_value *= get_value(matrix, current_row + 1, current_column);
            count += 1;
        } else {
            if current_column > 0 && matrix[current_row + 1][current_column - 1].is_numeric() {
                gear_value *= get_value(matrix, current_row + 1, current_column - 1);
                count += 1;
            }
            if current_column < matrix[0].len() && matrix[current_row + 1][current_column + 1].is_numeric() {
                gear_value *= get_value(matrix, current_row + 1, current_column + 1);
                count += 1;
            }
        }
    }

    if count == 2 {
        gear_value
    } else {
        0
    }
}

fn get_value(matrix: &Vec<Vec<char>>, row: usize, column: usize) -> i32 {

    let mut string_value = matrix[row][column].to_string();

    let mut i = 1;
    while i <= column && matrix[row][column - i].is_numeric() {
        string_value = matrix[row][column - i].to_string() + &string_value;
        i += 1;
    }

    i = 1;
    while column + i < matrix[0].len() && matrix[row][column + i].is_numeric() {
        string_value += &matrix[row][column + i].to_string();
        i += 1;
    }

    return string_value.parse::<i32>().unwrap()
}
