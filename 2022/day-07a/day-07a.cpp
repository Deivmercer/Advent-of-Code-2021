#include <fstream>
#include <string>
#include <cassert>
#include <sstream>
#include <iostream>

int folder_size(std::ifstream&);

const std::string file_name = "input.txt";
int sum = 0;

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());
	
	folder_size(input);

	std::cout << sum << std::endl;
}

int folder_size(std::ifstream& input)
{
	std::string line;
	int size = 0;

	std::getline(input, line);
	do
	{
		if (line.empty())
			continue;

		std::stringstream stream(line);
		std::string token;
		stream.ignore(2);
		stream >> token;

		if (token == "cd")
		{
			stream >> token;
			if (token == "..")
			{
				break;
			}
			size += folder_size(input);

			std::getline(input, line);
		}
		else if (token == "ls")
		{
			std::getline(input, line);
			do
			{
				if (!line.empty())
				{
					token = line.substr(0, line.find(' '));
					if (token != "dir")
						size += std::stoi(token);
				}
				if (input.eof())
					break;
				std::getline(input, line);
			} while (line[0] != '$');
		}
	} while (!input.eof());

	if (size <= 100000)
		sum += size;

	return size;
}