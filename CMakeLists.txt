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

set(SOURCES 
            src/main.cpp 
            src/Game.cpp 
            src/Display.cpp)

add_executable(pewpew ${SOURCES})
#add_definitions(-D_ITERATOR_DEBUG_LEVEL=0) 
#add_compile_definitions(SFML_STATIC)

target_include_directories(pewpew PRIVATE include SFML/include)

if (MSVC)
    add_custom_command(TARGET pewpew POST_BUILD
        COMMAND ${CMAKE_COMMAND} -E copy_directory
            "${PROJECT_SOURCE_DIR}/SFML/bin"
            $<TARGET_FILE_DIR:pewpew>)
    target_link_directories(pewpew PRIVATE SFML/lib)
    target_link_libraries(pewpew PRIVATE 
                            sfml-graphics-d 
                            sfml-system-d 
                            sfml-window-d 
                            openal32 
                            sfml-main 
                            sfml-audio-d 
                            ogg 
                            freetype 
                            flac 
                            vorbis 
                            vorbisenc 
                            vorbisfile)
else()
endif()
