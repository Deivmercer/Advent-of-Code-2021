#include <fstream>
#include <string>
#include <cassert>
#include <iostream>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	std::string line;
	int counter = 0;

	while (!input.eof())
	{
		std::getline(input, line);

		if (line.empty())
			continue;
		
		const size_t elf_delimiter = line.find(',');
		std::string elf = line.substr(0, elf_delimiter);
		size_t section_delimiter = elf.find('-');
		const int elf_1_start = stoi(elf.substr(0, section_delimiter)), elf_1_end = stoi(elf.substr(section_delimiter + 1,  elf.size()));
		elf = line.substr(elf_delimiter + 1, line.size());
		section_delimiter = elf.find('-');
		const int elf_2_start = stoi(elf.substr(0, section_delimiter)), elf_2_end = stoi(elf.substr(section_delimiter + 1, elf.size()));
		if (elf_1_start <= elf_2_start && elf_1_end >= elf_2_end || elf_2_start <= elf_1_start  && elf_2_end >= elf_1_end)
			++counter;
	}

	std::cout << counter << std::endl;
}