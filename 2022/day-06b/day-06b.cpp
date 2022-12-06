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
	std::getline(input, line);

	size_t i;
	for (i = 0; i < line.size() - 3; ++i)
	{
		std::string possible_marker = line.substr(i, 14);
		bool marker_found = true;
		for (size_t j = 0; j < possible_marker.size() - 1; ++j)
		{
			for (size_t z = j + 1; z < possible_marker.size(); ++z)
				if (possible_marker[j] == possible_marker[z])
					marker_found = false;
			if (!marker_found)
				break;
		}
		if (marker_found)
			break;
	}

	std::cout << i + 14 << std::endl;
}