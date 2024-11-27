from config import *

def update_scaled_planets():
    """Update planet sizes and distances based on the zoom factor."""
    scaled_planets = [
        {
            "name": planet["name"],
            "radius": max(int((planet["radius_km"] * KM_TO_PIXELS) * zoom_factor), 1),  # Scale radius
            "distance": int((planet["distance_au"] * AU_TO_PIXELS) * zoom_factor),  # Scale distance
            "orbital_speed": planet["orbital_speed"]
        }
        for planet in PLANET_DATA
    ]
    return scaled_planets


def update_orbits(angles, orbital_speeds):
    """Update the orbital angles of the planets based on their speeds."""
    for i in range(len(angles)):
        angles[i] += orbital_speeds[i]
    return angles
