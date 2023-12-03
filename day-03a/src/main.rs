use std::fs::read_to_string;

fn main() {

    let mut matrix: Vec<Vec<char>> = Vec::new();
    for line in read_to_string("input.txt").unwrap().lines() {
        let mut row: Vec<char> = Vec::new();
        for c in line.chars() {
            if c != '.' && !c.is_numeric() {
                row.push('S');
            } else {
                row.push(c);
            }
        }
        matrix.push(row);
    }

    let mut sum = 0;
    let mut skip = 0;
    for (i, row) in matrix.iter().enumerate() {
        for j in 0..row.len() {
            let mut to_sum = false;

            if skip > 0 {
                skip -= 1;
                continue
            }

            for (z, n) in row[j..].iter().enumerate() {
                if !n.is_numeric() {
                    break
                }
                skip += 1;
                to_sum = check_adjacent(&matrix, i, j + z);
                if to_sum {
                    break
                }
            }

            if to_sum {
                let mut number = 0;
                let mut z = 0;
                while j + z < matrix[i].len() && matrix[i][j + z].is_numeric() {
                    number = number * 10 + matrix[i][j + z].to_digit(10).unwrap();
                    z += 1;
                }
                if z > skip {
                    skip = z;
                }
                sum += number
            }
        }
    }
    println!("{}", sum)
}

fn check_adjacent(matrix: &Vec<Vec<char>>, current_row: usize, current_column: usize) -> bool {

    if check(matrix, current_row, current_column) {
        return true
    }
    if current_row > 0 && check(matrix, current_row - 1, current_column) {
        return true
    }
    if current_row < matrix.len() - 1 && check(matrix, current_row + 1, current_column) {
        return true
    }
    return false;
}

fn check (matrix: &Vec<Vec<char>>, row: usize, column: usize) -> bool  {

    if column > 0 && matrix[row][column - 1] == 'S' {
        return true;
    } else if matrix[row][column] == 'S' {
        return true;
    } else if column < matrix[0].len() - 1 && matrix[row][column + 1] == 'S' {
        return true;
    }
    return false;
}
