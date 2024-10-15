import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import argparse

# Constants
G = 6.67430e-11  # Gravitational constant in m^3 kg^-1 s^-2
AU = 1.496e11    # 1 Astronomical Unit in meters (distance from Earth to Sun)
DAY = 86400      # Number of seconds in a day

# Planet class to store properties of a planet
class Planet:
    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = np.array(position, dtype='float64')  # Position vector (x, y)
        self.velocity = np.array(velocity, dtype='float64')  # Velocity vector (vx, vy)
        self.acceleration = np.array([0, 0], dtype='float64')
        self.trajectory_x = [position[0]]  # Track x positions for plotting
        self.trajectory_y = [position[1]]  # Track y positions for plotting

    # Update position using the velocity and time step
    def update_position(self, delta_t):
        self.position += self.velocity * delta_t
        self.trajectory_x.append(self.position[0])
        self.trajectory_y.append(self.position[1])

    # Update velocity using the calculated acceleration and time step
    def update_velocity(self, delta_t):
        self.velocity += self.acceleration * delta_t

# Function to calculate the gravitational force between two planets
def gravitational_force(planet1, planet2):
    r = np.linalg.norm(planet2.position - planet1.position)  # Distance between planets
    if r == 0:
        return np.array([0, 0], dtype='float64')  # Avoid division by zero
    force_magnitude = G * planet1.mass * planet2.mass / r**2
    force_direction = (planet2.position - planet1.position) / r
    return force_magnitude * force_direction

# Function to update the simulation
def update_simulation(planets, delta_t):
    # Calculate forces and update accelerations
    for planet1 in planets:
        total_force = np.array([0, 0], dtype='float64')
        for planet2 in planets:
            if planet1 != planet2:
                total_force += gravitational_force(planet1, planet2)
        planet1.acceleration = total_force / planet1.mass

    # Update velocities and positions
    for planet in planets:
        planet.update_velocity(delta_t)
        planet.update_position(delta_t)

# Setup the animation
def animate(i):
    update_simulation(planets, delta_t)
    ax.clear()  # Clear previous frame
    ax.set_title('Solar System Simulation')
    ax.set_xlim(-3 * AU, 3 * AU)
    ax.set_ylim(-3 * AU, 3 * AU)
    ax.set_xlabel('Distance in AU')
    ax.set_ylabel('Distance in AU')
    ax.grid()
    
    # Plot the planets
    for planet in planets:
        ax.plot(planet.trajectory_x, planet.trajectory_y, label=planet.name, alpha=0.5)  # Trail line
        ax.scatter(planet.position[0], planet.position[1], s=100, edgecolor='black', label=planet.name)  # Larger dot for the planet
    
    ax.scatter(0, 0, color='yellow', label='Sun', s=300)  # Sun at the center, larger size
    ax.legend()
    ax.axis('equal')  # Keep aspect ratio equal

# Main simulation
def simulate_solar_system(speed_multiplier=1):
    # Time step and total time in seconds
    global delta_t
    delta_t = DAY * speed_multiplier  # Adjust the time step based on the speed multiplier
    total_steps = 730  # Simulate for 2 Earth years

    # Define planets (mass in kg, position and velocity in meters and meters/second)
    global planets
    sun = Planet('Sun', 1.989e30, [0, 0], [0, 0])
    earth = Planet('Earth', 5.972e24, [AU, 0], [0, 29.78e3])  # Earth's velocity is about 29.78 km/s
    mars = Planet('Mars', 6.39e23, [1.524 * AU, 0], [0, 24.07e3])  # Mars' velocity is about 24.07 km/s

    # List of planets to simulate
    planets = [sun, earth, mars]

    # Create the figure and axis for the plot
    global ax
    fig, ax = plt.subplots(figsize=(8, 8))

    # Create the animation
    ani = FuncAnimation(fig, animate, frames=total_steps, repeat=False)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run solar system simulation.")
    parser.add_argument('--speed', type=int, default=1, help='Speed multiplier for the simulation (days per step)')
    
    # Parse arguments
    args = parser.parse_args()

    # Run the solar system simulation with the specified speed multiplier
    simulate_solar_system(speed_multiplier=args.speed)
