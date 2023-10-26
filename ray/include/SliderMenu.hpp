#ifndef SLIDER_MENU_HPP
#define SLIDER_MENU_HPP

#include <SFML/Graphics.hpp>
#include <cassert>

class SliderMenu {
public:
    SliderMenu(float windowWidth, float windowHeight, const std::string& labelText = "placeholder" )
        : dragging(false) {

        // Sidebar
        sidebar.setSize(sf::Vector2f(100, windowHeight));
        sidebar.setFillColor(sf::Color(100, 100, 100));
        sidebar.setPosition(windowWidth - 100, 0);

        // Slider background
        sliderBackground.setFillColor(sf::Color(150, 150, 150));
        sliderBackground.setSize(sf::Vector2f(400, 20));
        sliderBackground.setPosition((windowWidth - 400) / 2, windowHeight - 100);

        // Slider
        slider.setFillColor(sf::Color::White);
        slider.setSize(sf::Vector2f(50, 20));
        slider.setPosition((windowWidth - 50) / 2, windowHeight - 100);

        //Label
        bool fontLoaded = font.loadFromFile("resources/sansation.ttf");
        assert(fontLoaded);
        label.setFont(font);
        label.setString(labelText);
        label.setCharacterSize(24);
        label.setFillColor(sf::Color::White);
        label.setPosition(windowWidth - 90, 20);


    }

    void handleEvent(const sf::Event& event, const sf::RenderWindow& window) {
        if (event.type == sf::Event::MouseButtonPressed) {
            if (event.mouseButton.button == sf::Mouse::Left) {
                sf::Vector2i mousePos = sf::Mouse::getPosition(window);
                if (slider.getGlobalBounds().contains(mousePos.x, mousePos.y)) {
                    dragging = true;
                }
            }
        }

        if (event.type == sf::Event::MouseButtonReleased) {
            if (event.mouseButton.button == sf::Mouse::Left) {
                dragging = false;
            }
        }
    }

    void update(const sf::RenderWindow& window) {
        if (dragging) {
            sf::Vector2i mousePos = sf::Mouse::getPosition(window);
            slider.setPosition(mousePos.x - slider.getSize().x / 2, slider.getPosition().y);
            
            float upperLimit = sliderBackground.getPosition().x;
            float lowerLimit = upperLimit + sliderBackground.getSize().x - slider.getSize().x;

            if (slider.getPosition().x < upperLimit) {
                slider.setPosition(upperLimit, slider.getPosition().y);
            }
            if (slider.getPosition().x > lowerLimit) {
                slider.setPosition(lowerLimit, slider.getPosition().y);
            }
        }
    }

    void draw(sf::RenderWindow& window) const {
        window.draw(sidebar);
        window.draw(sliderBackground);
        window.draw(slider);
        window.draw(label);

    }

private:
    sf::RectangleShape sidebar;
    sf::RectangleShape sliderBackground;
    sf::RectangleShape slider;
    sf::Font font;
    sf::Text label;
    bool dragging;
};

#endif // SLIDER_MENU_HPP