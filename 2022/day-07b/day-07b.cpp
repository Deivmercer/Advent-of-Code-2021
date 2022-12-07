#include <fstream>
#include <string>
#include <cassert>
#include <sstream>
#include <vector>
#include <iostream>

struct file
{
	int size = 0;
	bool is_directory = true;
	std::vector<file> sub_directories;
};
typedef file file;

file root;
const std::string file_name = "input.txt";
constexpr int disk_size = 70000000;
constexpr int update_size = 30000000;
int available_space;

file folder_tree(std::ifstream&);
int find_folder(file&);

int main()
{
	std::ifstream input(file_name);

	assert(input.is_open() && !input.eof());

	root = folder_tree(input);
	available_space = disk_size - root.size;

	std::cout << find_folder(root) << std::endl;
}

file folder_tree(std::ifstream& input)
{
	file dir;
	std::string line;

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
				break;

			file sub_dir = folder_tree(input);
			dir.sub_directories.push_back(sub_dir);
			dir.size += sub_dir.size;

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
						dir.size += std::stoi(token);
				}
				if (input.eof())
					break;
				std::getline(input, line);
			} while (line[0] != '$');
		}
	} while (!input.eof());

	return dir;
}

int find_folder(file& current_dir)
{
	int smallest_folder = update_size;
	for (file& directory : current_dir.sub_directories)
	{
		if (directory.size + available_space >= update_size && directory.size <= smallest_folder)
			smallest_folder = directory.size;
		if (directory.is_directory)
		{
			const int found = find_folder(directory);
			if (found < smallest_folder)
				smallest_folder = found;
		}
	}
	return smallest_folder;
}
