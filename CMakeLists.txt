project(gamejam-fall-2022)

cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)

include(FetchContent)

set(BUILD_SHARED_LIBS OFF)
FetchContent_Declare(
 SFML
 GIT_REPOSITORY https://github.com/SFML/SFML.git
 GIT_TAG 2.5.1
)
FetchContent_MakeAvailable(SFML)

set(BUILD_SHARED_LIBS OFF)
FetchContent_Declare(
 Box2D
 GIT_REPOSITORY https://github.com/erincatto/box2d.git
 GIT_TAG v2.4.1
)
FetchContent_MakeAvailable(Box2D)

set(SOURCES 
            src/main.cpp 
            src/Game.cpp 
            src/Display.cpp
            )

add_executable(pewpew ${SOURCES})

target_link_libraries(
    pewpew
    sfml-graphics
)

target_include_directories(pewpew PRIVATE include)
