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

		if (line[0] == 'A')
		{
			if (line[2] == 'X')
				score += 3;
			else if (line[2] == 'Y')
				score += 4;
			else if (line[2] == 'Z')
				score += 8;
		}
		else if (line[0] == 'B')
		{
			if (line[2] == 'X')
				score += 1;
			else if (line[2] == 'Y')
				score += 5;
			else if (line[2] == 'Z')
				score += 9;
		}
		else if (line[0] == 'C')
		{
			if (line[2] == 'X')
				score += 2;
			else if (line[2] == 'Y')
				score += 6;
			else if (line[2] == 'Z')
				score += 7;
		}
	}

	std::cout << score << std::endl;
}