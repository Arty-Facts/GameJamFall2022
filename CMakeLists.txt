project(gamejam-fall-2022)

cmake_minimum_required(VERSION 3.16)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED true)

add_compile_definitions(_HAS_AUTO_PTR_ETC)

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
 box2d
 GIT_REPOSITORY https://github.com/erincatto/box2d.git
 GIT_TAG v2.4.1
)
FetchContent_MakeAvailable(box2d)
#add_subdirectory(${box2d_SOURCE_DIR}/Box2D ${box2d_BINARY_DIR})

set(SOURCES 
            src/main.cpp 
            src/Game.cpp 
            src/Display.cpp
            )

add_executable(pewpew ${SOURCES})

target_link_libraries(
    pewpew
    sfml-graphics
    box2d
)

target_include_directories(pewpew PRIVATE include ${box2d_SOURCE_DIR}/include)
