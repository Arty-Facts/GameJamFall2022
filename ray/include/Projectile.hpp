#ifndef PROJECTILE_HPP
#define PROJECTILE_HPP

#include <SFML/Graphics.hpp>

class Projectile : public sf::CircleShape {
public:
    Projectile(float x, float y, float speedX, float speedY, float radius = 5)
        : sf::CircleShape(radius), speedX(speedX), speedY(speedY) {
        setFillColor(sf::Color::White);
        setPosition(x, y);
    }

    void update(float deltaTime) {
        move(speedX * deltaTime, speedY * deltaTime);
    }

private:
    float speedX, speedY;
};

#endif // PROJECTILE_HPP