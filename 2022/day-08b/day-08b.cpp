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

	int max_score = 0;
	for (size_t i = 0; i < forest.size(); ++i)
	{
		for (size_t j = 0; j < forest[i].size(); ++j)
		{
			int score = 0;
			for (int z = j - 1; z >= 0; --z)
			{
				++score;
				if (forest[i][j].height <= forest[i][z].height)
					break;
			}

			int dir_score = 0;
			for (int z = j + 1; z < forest[i].size(); ++z)
			{
				++dir_score;
				if (forest[i][j].height <= forest[i][z].height)
					break;
			}
			score *= dir_score;

			dir_score = 0;
			for (int z = i - 1; z >= 0; --z)
			{
				++dir_score;
				if (forest[i][j].height <= forest[z][j].height)
					break;
			}
			score *= dir_score;

			dir_score = 0;
			for (int z = i + 1; z < forest.size(); ++z)
			{
				++dir_score;
				if (forest[i][j].height <= forest[z][j].height)
					break;
			}
			score *= dir_score;

			if (score > max_score)
				max_score = score;
		}
	}

	std::cout << max_score << std::endl;
}