# Autonomous Solar System Simulation

This project simulates the motion of celestial bodies in our solar system using a simple physics engine. The simulation is visualized with a graphical interface, allowing users to observe the orbits of planets around the Sun.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Customization](#customization)

## Features

- **Realistic Simulation**: Simulates the gravitational interactions between the Sun, Earth, Mars, and other celestial bodies.
- **Visual Representation**: Displays the orbits and positions of the planets in a user-friendly graphical interface.
- **Speed Control**: Allows users to adjust the simulation speed through command-line arguments.
- **Open Source**: This project is open for contributions and improvements.

## Installation

To run this simulation, you need Python installed on your system. You can follow these steps to set up the project:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/RitterAntoine/Handwritten_Digit_Recognition.git
    cd Handwritten_Digit_Recognition/src
    ```

2. **Install Required Packages**:
   This project uses `uv` as the package manager. To install the necessary packages, run:
   ```bash
   uv install numpy matplotlib argparse
   ```

## Usage

To run the solar system simulation, use the following command in your terminal:

```bash
uv run src/solar_system.py --speed <multiplier>
```

- Replace `<multiplier>` with the number of days each simulation step should represent (e.g., `1`, `5`, `10`). 
- For example, to run the simulation at a speed of 10 days per step:
  ```bash
  uv run src/solar_system.py --speed 10
  ```

## Code Overview

### Main Components

- **Planet Class**: Represents each planet with its mass, position, velocity, and trajectory.
- **Gravitational Force Calculation**: Computes the gravitational forces between planets to update their positions and velocities.
- **Animation Function**: Visualizes the simulation using `matplotlib`, updating the positions of planets in real time.

### Key Functions

- `simulate_solar_system(speed_multiplier)`: Initializes the simulation with the specified speed.
- `update_simulation(planets, delta_t)`: Updates the positions and velocities of all planets.
- `animate(i)`: Handles the graphical updates for each frame of the animation.

## Customization

You can customize the simulation by:

- Adding more celestial bodies: Extend the `Planet` class and add new instances in the `simulate_solar_system` function.
- Adjusting the gravitational constant or masses of the planets for different scenarios.
- Modifying the visual representation (e.g., colors, sizes) of the planets and trails.