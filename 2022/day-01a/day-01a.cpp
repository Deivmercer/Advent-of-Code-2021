#include <fstream>
#include <string>
#include <cassert>
#include <iostream>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	int max = 0, current_elf = 0;
	std::string line;

	while(!input.eof())
	{
		std::getline(input, line);
		if (line.empty())
		{
			if (current_elf > max)
				max = current_elf;
			current_elf = 0;
			continue;
		}
		current_elf += std::stoi(line);
	}

	std::cout << max;
}