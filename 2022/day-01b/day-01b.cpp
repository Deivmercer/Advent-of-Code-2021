#include <fstream>
#include <string>
#include <cassert>
#include <iostream>
#include <vector>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	std::vector<int> elves;
	int current_elf = 0;
	std::string line;

	while (!input.eof())
	{
		std::getline(input, line);
		if (line.empty())
		{
			elves.push_back(current_elf);
			current_elf = 0;
			continue;
		}
		current_elf += std::stoi(line);
	}
	
	for (size_t i = 0; i < elves.size() - 1; ++i)
		for (size_t j = i + 1; j < elves.size(); ++j)
			if (elves[j] < elves[i])
				std::swap(elves[j], elves[i]);

	std::cout << elves[elves.size() - 1] + elves[elves.size() - 2] + elves[elves.size() - 3] << std::endl;
}