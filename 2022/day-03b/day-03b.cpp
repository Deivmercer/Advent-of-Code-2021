#include <fstream>
#include <string>
#include <cassert>
#include <iostream>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	std::string elf_1, elf_2, elf_3;
	int priority_sum = 0;

	while (!input.eof())
	{
		std::getline(input, elf_1);

		if (elf_1.empty())
			continue;

		std::getline(input, elf_2);
		std::getline(input, elf_3);

		char duplicate = -1;
		for (const char i : elf_1)
		{
			for (const char j : elf_2)
				if (i == j)
				{
					const char candidate_duplicate = i;
					for (const char z : elf_3)
					{
						if (z == candidate_duplicate)
						{
							duplicate = candidate_duplicate;
							break;
						}
					}
					if (duplicate != -1)
						break;
				}
			if (duplicate != -1)
				break;
		}

		if (isupper(duplicate))
			priority_sum += duplicate - 38;
		else
			priority_sum += duplicate - 96;
	}

	std::cout << priority_sum << std::endl;
}