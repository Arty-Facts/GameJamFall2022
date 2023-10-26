#include <SFML/Graphics.hpp>
#include "Sensor.hpp"
#include "Projectile.hpp"
#include "SliderMenu.hpp"
#include <vector>

#define SPEED 100.0f

int main() {
    // Create a window with the size of 900x600 pixels
    sf::RenderWindow window(sf::VideoMode(900, 600), "Circle in the Middle");

    // Create a sensor
    Sensor sensor(10, window.getSize().x / 2, window.getSize().y / 2, SPEED);
    SliderMenu sliderMenu(900, 600);

    std::vector<Projectile> projectiles;
    sf::Clock clock; // Create a clock to measure time elapsed

    // Main loop that continues until the window is closed
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            sliderMenu.handleEvent(event, window);
            if (event.type == sf::Event::Closed)
                window.close();
        }

        if (sf::Mouse::isButtonPressed(sf::Mouse::Left)) {
            float sx = sensor.getPosition().x + sensor.getRadius()/2;
            float sy = sensor.getPosition().y + sensor.getRadius()/2;

            // Calculate the direction of the projectile
            float dx = sf::Mouse::getPosition(window).x - sx;
            float dy = sf::Mouse::getPosition(window).y - sy;

            // Normalize the direction
            float length = std::sqrt(dx * dx + dy * dy);
            dx /= length / SPEED;
            dy /= length / SPEED;

            projectiles.emplace_back(sx, sy, dx, dy);
        }

        float deltaTime = clock.restart().asSeconds();
        sensor.update(window, deltaTime);
        for (auto& projectile : projectiles) {
            projectile.update(deltaTime);
        }
        sliderMenu.update(window);

        window.clear();
        window.draw(sensor);
        for (const auto& projectile : projectiles) {
            window.draw(projectile);
        }
        sliderMenu.draw(window);
        window.display();
    }

    return 0;
}