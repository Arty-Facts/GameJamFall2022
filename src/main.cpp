#include "Game.hpp"
#include "Display.hpp"

#include <iostream>

int main()
{
    int n{};
    std::cout << "Hello World" << std::endl;
    Game g;
    g.hi("Arty");
    std::cin >> n;
    Display d;
    d.show(); 
    return 0;
}