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
    ray/main.cpp 

)

add_executable(ray ${SOURCES})
target_include_directories(ray PRIVATE
    ray/include 
    ${box2d_SOURCE_DIR}/include
)

target_link_libraries(
    ray
    sfml-graphics
    box2d
)


add_custom_command(TARGET ray POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            "${PROJECT_SOURCE_DIR}/ray/assets"
            $<TARGET_FILE_DIR:ray>/assets)