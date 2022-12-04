#include <fstream>
#include <string>
#include <cassert>
#include <iostream>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	int score = 0;
	std::string line;

	while (!input.eof())
	{
		std::getline(input, line);

		if (line.empty())
			continue;

		if (line[2] == 'X')
			score += 1;
		else if (line[2] == 'Y')
			score += 2;
		else if (line[2] == 'Z')
			score += 3;

		if (line == "A X" || line == "B Y" || line == "C Z")
			score += 3;
		else if (line == "A Y" || line == "B Z" || line == "C X")
			score += 6;
	}

	std::cout << score << std::endl;
}