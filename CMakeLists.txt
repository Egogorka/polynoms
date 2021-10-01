cmake_minimum_required(VERSION 3.17)
project(polynoms)

set(CMAKE_CXX_STANDARD 20)

add_executable(polynoms main.cpp src/Polynom.h src/durand_kerner.cpp src/durand_kerner.h src/approximation.cpp src/approximation.h)