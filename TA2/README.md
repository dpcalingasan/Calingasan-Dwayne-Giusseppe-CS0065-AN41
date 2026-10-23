# TA2: Rule-Based Vacuum Cleaner Agent

This repository contains the required output for TA2. The project simulates a simple vacuum-cleaning agent operating in a two-room environment using rule-based decision making.

## Files
- `TA2_Calingasan.py` - Python program for the vacuum cleaner simulation
- `TA2_Calingasan.pdf` - task output document
- `README.md` - project overview

## Description
The agent continuously perceives the current room and follows a simple decision rule:
- If the current room is dirty, it cleans it.
- If the current room is clean, it moves to the other room.

The simulation accepts room states from the user and runs for a selected number of steps. It prints each action taken and shows the final state of both rooms and the agent's location.

## Features
- Two-room environment simulation
- Rule-based decision logic
- User input validation for room states and steps
- Step-by-step action trace
- Final environment summary

## How to Run
1. Open a terminal in the project folder.
2. Execute the script:
   ```bash
   python TA2_Calingasan.py
