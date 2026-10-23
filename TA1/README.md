# TA1: Random Walk Simulation Using Agent-Based Modeling

This repository contains the required output for TA1. The project simulates multiple agents moving randomly across a grid while avoiding collisions and visualizes their motion using an animated plot.

## Files
- `TA_randomwalk.py` - Python script that implements the random walk simulation
- `TA1 _Calingasan.pdf` - output document for the activity
- `README.md` - project overview

## Description
The program uses the `agentpy` library to model autonomous agents moving on a 2D grid. Each agent chooses a direction randomly and attempts to move to an unoccupied neighboring cell. The simulation also records each agent's path and displays the final movement trajectories.

## Features
- Multiple agents moving simultaneously on a grid
- Randomized movement with collision avoidance
- Customizable number of agents, grid size, and steps
- Real-time animation of agent positions
- Final position and path tracking for each agent

## How to Run
1. Open a terminal in the project folder.
2. Install the required libraries:
   ```bash
   pip install agentpy matplotlib
   ```
3. Run the Python script:
   ```bash
   python TA_randomwalk.py
   ```
4. Enter the desired values for:
   - number of agents
   - grid size
   - number of steps
5. Observe the animation and review the final positions and path history printed in the console.

## Author
Dwayne Giusseppe P. Calingasan

## Course and Section
BSCSSE AN41
