#include <SFML/Graphics.hpp>
#include "move.hpp"

#define SPEED 100.0f

int main() {
    // Create a window with the size of 800x600 pixels
    sf::RenderWindow window(sf::VideoMode(800, 600), "Circle in the Middle");

    // Create a circle with a radius of 50 pixels
    sf::CircleShape circle(50);

    // Set the circle's color to green
    circle.setFillColor(sf::Color::Green);

    // Set the circle's position to the middle of the window
    circle.setPosition(window.getSize().x / 2 - circle.getRadius(), 
                       window.getSize().y / 2 - circle.getRadius());

    sf::Clock clock; // Create a clock to measure time elapsed

    // Main loop that continues until the window is closed
    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }
        float deltaTime = clock.restart().asSeconds(); // Get time elapsed since last frame
        move(circle, window, SPEED*deltaTime);

        // Clear the window
        window.clear();

        // Draw the circle
        window.draw(circle);

        // Display the contents of the window
        window.display();
    }

    return 0;
}