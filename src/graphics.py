import pygame
from config import *
import math

# Initialize pygame and window settings
pygame.init()
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Solar System Simulation")
font = pygame.font.Font(None, 24)

def handle_events():
    """Handle user events like quitting, zooming, and panning."""
    global zoom_factor, offset_x, offset_y, dragging, last_mouse_position
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:  # Scroll up (zoom in)
                zoom_factor = min(zoom_factor * 1.1, MAX_ZOOM)
            elif event.button == 5:  # Scroll down (zoom out)
                zoom_factor = max(zoom_factor / 1.1, MIN_ZOOM)
            elif event.button == 1:  # Left click to start dragging
                dragging = True
                last_mouse_position = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:  # Stop dragging
                dragging = False
        elif event.type == pygame.MOUSEMOTION:
            if dragging:
                # Update the offset based on mouse movement
                dx, dy = event.pos[0] - last_mouse_position[0], event.pos[1] - last_mouse_position[1]
                offset_x += dx
                offset_y += dy
                last_mouse_position = event.pos
    return True

def draw_sun():
    """Draw the Sun at the center of the window."""
    pygame.draw.circle(WINDOW, SUN_COLOR, (WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 2 + offset_y),
                       max(int(SUN_RADIUS_KM * KM_TO_PIXELS * zoom_factor), 2))

def draw_orbit_paths(scaled_planets):
    """Draw the orbital paths for all planets."""
    for planet in scaled_planets:
        pygame.draw.circle(WINDOW, (50, 50, 50), (WINDOW_WIDTH // 2 + offset_x, WINDOW_HEIGHT // 2 + offset_y),
                           planet["distance"], 1)

def draw_planet(planet_data, angle, color):
    """Draw a planet at its current orbital position."""
    distance = planet_data["distance"]
    radius = planet_data["radius"]

    # Calculate the current position of the planet
    x = WINDOW_WIDTH // 2 + distance * math.cos(math.radians(angle)) + offset_x
    y = WINDOW_HEIGHT // 2 + distance * math.sin(math.radians(angle)) + offset_y

    # Draw the planet
    pygame.draw.circle(WINDOW, color, (int(x), int(y)), radius)

    # Display the planet's name near its position
    planet_name_text = font.render(planet_data["name"], True, (255, 255, 255))
    WINDOW.blit(planet_name_text, (int(x) + 10, int(y) + 10))
