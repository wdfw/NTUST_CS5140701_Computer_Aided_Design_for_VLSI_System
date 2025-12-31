project(Project3)
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
set(CMAKE_CXX_STANDARD 11)

add_executable(./bin/multilevel ./src/Utils.cpp ./src/main.cpp) 
include_directories("/usr/include/boost/")

