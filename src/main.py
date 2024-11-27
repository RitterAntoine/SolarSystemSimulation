import pygame
from config import *
from graphics import *
from planets import *
import math

def main():
    """Main function to run the simulation."""
    clock = pygame.time.Clock()
    running = True
    angles = [0] * len(PLANET_DATA)  # Initial orbital angles
    orbital_speeds = [planet["orbital_speed"] for planet in PLANET_DATA]  # Orbital speeds

    while running:
        running = handle_events()

        # Update planets' data with zoom factor
        scaled_planets = update_scaled_planets()

        # Clear screen
        WINDOW.fill(BLACK)

        # Draw the Sun and planets
        draw_sun()

        # Draw orbits and planets
        draw_orbit_paths(scaled_planets)

        # Draw each planet
        for i, planet_data in enumerate(scaled_planets):
            draw_planet(planet_data, angles[i], PLANET_COLORS[i])

        # Update angles of planets based on their speeds
        angles = update_orbits(angles, orbital_speeds)

        # Update the display
        pygame.display.update()
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()

if __name__ == "__main__":
    main()
