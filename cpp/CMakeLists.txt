cmake_minimum_required(VERSION 3.5.0)
project(advent_of_code VERSION 0.1.0 LANGUAGES C CXX)

add_library(utils_lib STATIC ${CMAKE_SOURCE_DIR}/utils/src/file_helpers.cpp)
add_library(days_lib STATIC ${CMAKE_SOURCE_DIR}/days/src/day1.cpp)
include_directories(./third-party/inc ./utils/inc ./days/inc)

add_executable(advent_of_code main.cpp)
# target_link_directories(cpp_learn ${CMAKE_SOURCE_DIR}/utils)
target_link_libraries(advent_of_code utils_lib)
target_link_libraries(advent_of_code days_lib)

