#include <fstream>
#include <string>
#include <cassert>
#include <vector>
#include <iostream>

struct tree
{
	int height;
	bool visible;
};
typedef tree tree;

const std::string file_name = "input.txt";

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	std::vector<std::vector<tree>> forest;
	std::string line;
	int counter = 0;

	while (!input.eof())
	{
		std::getline(input, line);

		if (line.empty())
			continue;

		std::vector<tree> row;
		for (const char i : line)
		{
			tree t = { i - 48, false };
			row.push_back(t);
		}
		forest.push_back(row);
	}
	
	for (size_t i = 0; i < forest.size(); ++i)
	{
		for (size_t j = 0; j < forest[i].size(); ++j)
		{
			if (forest[i][j].visible)
				continue;

			bool visible = true;
			for (size_t z = 0; z < j; ++z)
				if (forest[i][z].height >= forest[i][j].height)
				{
					visible = false;
					break;
				}
			forest[i][j].visible = visible;

			if (forest[i][j].visible)
				++counter;
		}

		for (size_t j = forest[i].size() - 1; j > 0; --j)
		{
			if (forest[i][j].visible)
				continue;

			bool visible = true;
			for (size_t z = j + 1; z < forest[i].size(); ++z)
				if (forest[i][z].height >= forest[i][j].height)
				{
					visible = false;
					break;
				}
			forest[i][j].visible = visible;

			if (forest[i][j].visible)
				++counter;
		}

		for (size_t j = 0; j < forest[i].size(); ++j)
		{
			if (forest[i][j].visible)
				continue;

			bool visible = true;
			for (size_t z = 0; z < i; ++z)
				if (forest[z][j].height >= forest[i][j].height)
				{
					visible = false;
					break;
				}
			forest[i][j].visible = visible;

			if (forest[i][j].visible)
				++counter;
		}

		for (size_t j = 0; j < forest[i].size(); ++j)
		{
			if (forest[i][j].visible)
				continue;

			bool visible = true;
			for (size_t z = i + 1; z < forest[i].size(); ++z)
				if (forest[z][j].height >= forest[i][j].height)
				{
					visible = false;
					break;
				}
			forest[i][j].visible = visible;

			if (forest[i][j].visible)
				++counter;
		}
	}

	std::cout << counter << std::endl;
}