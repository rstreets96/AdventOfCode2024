#include <iostream>
#include <fstream>
#include <string>

bool read_file(std::string filename, std::string *output)
{
    std::ifstream f(filename);
    if(!f.is_open())
    {
        std::cerr << "Error opening the file!";
        return false;
    }
    std::string s;
    while(getline(f, s))
    {
        output->append(s);
        output->append("\n");
    }
    f.close();
    return true;
}