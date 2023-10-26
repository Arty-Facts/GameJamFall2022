#ifndef SENSOR_HPP
#define SENSOR_HPP

#include <SFML/Graphics.hpp>

class Sensor : public sf::CircleShape {
public:
    Sensor(size_t size, float x, float y,  float speed)
        : sf::CircleShape(size), speed(speed){
        setFillColor(sf::Color::Yellow);
        setPosition(x, y);
    }

    void update(sf::RenderWindow &window, float deltaTime){
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
            move(-speed*deltaTime, 0);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
            move(speed*deltaTime, 0);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
            move(0, -speed*deltaTime);
        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
            move(0, speed*deltaTime);
        }

private:
    float speed;
};

#endif // SENSOR_HPP