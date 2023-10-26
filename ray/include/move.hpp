
#ifndef MOVER_H
#define MOVER_H

#include <SFML/Graphics.hpp>

template <typename T>
void move(T &shape, sf::RenderWindow &window, float speed = 5.0f){
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
        shape.move(-speed, 0);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
        shape.move(speed, 0);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
        shape.move(0, -speed);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
        shape.move(0, speed);
}



#endif // MOVER_H