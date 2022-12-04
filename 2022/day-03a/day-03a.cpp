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
	int priority_sum = 0;

	while (!input.eof())
	{
		std::getline(input, line);

		if (line.empty())
			continue;

		char duplicate = -1;
		for (size_t i = 0; i < line.size() / 2; ++i)
		{
			for (size_t j = line.size() / 2; j < line.size(); j++)
				if (line[i] == line[j])
				{
					duplicate = line[i];
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