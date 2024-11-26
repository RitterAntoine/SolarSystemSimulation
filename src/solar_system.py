import pygame
import math

# Initialize pygame
pygame.init()

# Window parameters
WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Solar System Simulation")

# Colors
BLACK = (0, 0, 0)
SUN_COLOR = (255, 223, 0)  # Yellow for the Sun
PLANET_COLORS = [
    (192, 192, 192),  # Mercury (Gray)
    (255, 215, 0),    # Venus (Gold)
    (0, 191, 255),    # Earth (Blue)
    (255, 69, 0),     # Mars (Red)
    (255, 165, 0),    # Jupiter (Orange)
    (218, 165, 32),   # Saturn (Goldenrod)
    (0, 206, 209),    # Uranus (Turquoise)
    (25, 25, 112)     # Neptune (Dark Blue)
]

# Planet data: (radius, orbital speed, distance from Sun)
PLANET_PARAMETERS = [
    {"radius": 4, "orbital_speed": 0.24, "distance": 50},    # Mercury
    {"radius": 7, "orbital_speed": 0.18, "distance": 80},    # Venus
    {"radius": 8, "orbital_speed": 0.15, "distance": 110},   # Earth
    {"radius": 6, "orbital_speed": 0.12, "distance": 150},   # Mars
    {"radius": 12, "orbital_speed": 0.08, "distance": 200},  # Jupiter
    {"radius": 10, "orbital_speed": 0.06, "distance": 260},  # Saturn
    {"radius": 9, "orbital_speed": 0.04, "distance": 320},   # Uranus
    {"radius": 8, "orbital_speed": 0.03, "distance": 380}    # Neptune
]

# Sun's position in the center of the window
SUN_POSITION = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

def draw_sun():
    """Draw the Sun at the center of the window."""
    pygame.draw.circle(WINDOW, SUN_COLOR, SUN_POSITION, 30)

def draw_planet(planet_data, angle, color):
    """Draw a planet based on its orbital parameters."""
    distance = planet_data["distance"]
    radius = planet_data["radius"]

    # Calculate the planet's current position
    x = SUN_POSITION[0] + distance * math.cos(math.radians(angle))
    y = SUN_POSITION[1] + distance * math.sin(math.radians(angle))

    # Draw the planet
    pygame.draw.circle(WINDOW, color, (int(x), int(y)), radius)

def update_orbits(angles, orbital_speeds):
    """Update the angles of planets based on their orbital speeds."""
    for i in range(len(angles)):
        angles[i] += orbital_speeds[i]
    return angles

def handle_events():
    """Handle user input events, such as quitting the simulation."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def main():
    """Main function to run the simulation."""
    clock = pygame.time.Clock()
    running = True
    angles = [0] * len(PLANET_PARAMETERS)  # Initialize orbital angles

    while running:
        clock.tick(60)  # Limit to 60 FPS
        WINDOW.fill(BLACK)  # Clear the window

        draw_sun()  # Draw the Sun at the center

        # Draw each planet and update their orbits
        for i, planet_data in enumerate(PLANET_PARAMETERS):
            draw_planet(planet_data, angles[i], PLANET_COLORS[i])

        angles = update_orbits(angles, [planet["orbital_speed"] for planet in PLANET_PARAMETERS])

        running = handle_events()  # Check for user input
        pygame.display.update()  # Refresh the display

    pygame.quit()

# Run the simulation
if __name__ == "__main__":
    main()
