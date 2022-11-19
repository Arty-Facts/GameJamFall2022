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

set(SOURCES 
    pewpew/src/main.cpp 
    pewpew/src/Game.cpp 
    pewpew/src/Display.cpp
)

add_executable(pewpew ${SOURCES})

target_include_directories(pewpew PRIVATE
    pewpew/include 
    ${box2d_SOURCE_DIR}/include
)

target_link_libraries(
    pewpew
    sfml-graphics
    box2d
)


add_executable(boxbuilder boxbuilder/main.cpp)

target_link_libraries(
    boxbuilder
    sfml-graphics
    box2d
)

target_include_directories(boxbuilder PRIVATE ${box2d_SOURCE_DIR}/include)
add_custom_command(TARGET boxbuilder POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            "${PROJECT_SOURCE_DIR}/boxbuilder/assets"
            $<TARGET_FILE_DIR:boxbuilder>/assets)