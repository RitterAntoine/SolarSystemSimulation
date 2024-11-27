# Real constants (radii in km, distances in AU)
SUN_RADIUS_KM = 696000  # Radius of the Sun in km
PLANET_DATA = [
    {"name": "Mercury", "radius_km": 2439.7, "distance_au": 0.387, "orbital_speed": 0.24},
    {"name": "Venus", "radius_km": 6051.8, "distance_au": 0.723, "orbital_speed": 0.18},
    {"name": "Earth", "radius_km": 6371.0, "distance_au": 1.0, "orbital_speed": 0.15},
    {"name": "Mars", "radius_km": 3389.5, "distance_au": 1.524, "orbital_speed": 0.12},
    {"name": "Jupiter", "radius_km": 69911, "distance_au": 5.203, "orbital_speed": 0.08},
    {"name": "Saturn", "radius_km": 58232, "distance_au": 9.58, "orbital_speed": 0.06},
    {"name": "Uranus", "radius_km": 25362, "distance_au": 19.19, "orbital_speed": 0.04},
    {"name": "Neptune", "radius_km": 24622, "distance_au": 30.06, "orbital_speed": 0.03}
]

# Scaling factors (adjustable)
KM_TO_PIXELS = 1 / 40000   # Scale for planet radii
AU_TO_PIXELS = 100          # Scale for distances

# Zoom settings
zoom_factor = 1.0           # Zoom level (1.0 = default)
MIN_ZOOM = 0.2
MAX_ZOOM = 5.0

# Window settings
WINDOW_WIDTH, WINDOW_HEIGHT = 1400, 800

# Colors
BLACK = (0, 0, 0)
SUN_COLOR = (255, 223, 0)
PLANET_COLORS = [
    (192, 192, 192),  # Mercury
    (255, 215, 0),    # Venus
    (0, 191, 255),    # Earth
    (255, 69, 0),     # Mars
    (255, 165, 0),    # Jupiter
    (218, 165, 32),   # Saturn
    (0, 206, 209),    # Uranus
    (25, 25, 112)     # Neptune
]

# Panning offset
offset_x = 0
offset_y = 0
dragging = False
last_mouse_position = (0, 0)
