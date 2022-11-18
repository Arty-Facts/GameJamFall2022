project(gamejam-fall-2022)

cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_STANDARD 17)
if (MSVC)
    # warning level 4 and all warnings as errors
    add_compile_options(/W4 /WX)
else()
    # lots of warnings and all warnings as errors
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()

set(SOURCES src/main.cpp src/Game.cpp)
include_directories(includes)

add_executable(pewpew ${SOURCES})