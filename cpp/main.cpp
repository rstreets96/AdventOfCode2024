#include <iostream>
#include <CLI11.hpp>

#include <file_helpers.hpp>
#include <day1.hpp>

int main(int argc, char** argv){
    CLI::App app{"App description"};
    argv = app.ensure_utf8(argv);

    std::string filename = "default";
    std::uint8_t day_select = 0;
    std::uint8_t part_select = 0;
    app.add_option("-f,--file", filename, "The file name to be read.");
    app.add_option("-d,--day", day_select, "The day of the problem selected");
    app.add_option("-p,--part", part_select, "The part of the day selected");

    CLI11_PARSE(app, argc, argv);
    std::cout << part_select;
    
    std::string contents;
    read_file(filename, &contents);

    switch(day_select)
    {
        case 1:
            day1_main(contents, part_select);
            break;

        default:
            std::cout << "Invalid Day Selection";
            break;
    }

    return 0;
}
