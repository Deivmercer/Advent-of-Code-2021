#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <sstream>
#include <iostream>

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	std::vector<std::vector<char>> stacks;
	std::string line;

	std::getline(input, line);
	for (size_t i = 0; i <= line.size() / 4; ++i)
	{
		std::vector<char> stack;
		stacks.push_back(stack);
	}

	do
	{
		if (line.empty())
			continue;

		for (size_t i = 0; i < line.size(); i += 4)
		{
			char crate = line.substr(i, 3)[1];
			if (crate != ' ')
				stacks[i / 4].insert(stacks[i / 4].begin(), crate);
		}

		std::getline(input, line);
	} while (line.substr(0, 3) != " 1 ");

	while (!input.eof())
	{
		std::getline(input, line);

		if (line.empty())
			continue;

		std::stringstream stream(line);
		size_t q, from, to;

		stream.ignore(5);
		stream >> q;
		stream.ignore(5);
		stream >> from;
		stream.ignore(3);
		stream >> to;

		std::vector<char> moving_stack;
		for (size_t i = 0; i < q; ++i)
		{
			char crate = stacks[from - 1].back();
			stacks[from - 1].pop_back();
			moving_stack.insert(moving_stack.begin(), crate);
		}
		stacks[to - 1].insert(stacks[to - 1].end(), moving_stack.begin(), moving_stack.end());
	}

	for (std::vector<char> stack : stacks)
		std::cout << stack.back();
}