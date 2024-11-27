# Autonomous Solar System Simulation

This project simulates the motion of celestial bodies in our solar system using a simple physics engine. The simulation is visualized with a graphical interface, allowing users to observe the orbits of planets around the Sun.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)

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
   This project uses `uv` as the package manager, so you don't need to install it separately.

## Usage

To run the solar system simulation, use the following command in your terminal:

```bash
uv run src/main.py
```

## File Structure

The project is organized into several files and directories:

- `src/`: Contains the main source code for the simulation.
  - `config.py`: Defines constants and configurations for the simulation.
  - `main.py`: The main entry point for the simulation.
  - `planets.py`: Contains functions for updating the positions and orbits of the planets.
  - `solar_system.py`: Contains the main simulation logic.
  - `utils.py`: Contains utility functions for converting between degrees and radians.
- `uv.lock`: Lock file for the `uv` package manager.
- `pyproject.toml`: Configuration file for the `uv` package manager.
- `gitignore`: Specifies files and directories to be ignored by Git.
- `README.md`: This file.