# TA4: Classroom Comfort Adviser

This repository contains the required output for TA4. The project demonstrates a classroom comfort advisory system using both rule-based reasoning and case-based reasoning.

## Files
- `TA4_Basister-Calingasan.py` - Python script implementing the adviser
- `TA4_Basister-Calingasan.pdf` - output document for the task
- `README.md` - project overview

## Description
The system evaluates classroom conditions such as temperature, humidity, weather, and occupancy. It uses a rule-based approach to infer required actions, then compares the problem with past cases to recommend a suitable action based on similarity.

The program includes:
- Rule-based reasoning using IF-THEN rules
- Case retrieval from a stored case base
- Reuse and revision of past solutions
- Retention of newly solved cases during the session

## Features
- Classroom condition analysis
- Rule-based inference for actions
- Case-based reasoning workflow
- Similarity-based case retrieval
- Action revision and case retention
- Demo mode for reproducible output

## How to Run
1. Open a terminal in the project folder.
2. Run the script:
   ```bash
   python TA4_Basister-Calingasan.py
   ```
3. Optional demo mode:
   ```bash
   python TA4_Basister-Calingasan.py --demo
   ```
4. Review the inferred rules, selected case, and final recommended action.

## Author
Dwayne Giusseppe P. Calingasan

## Course and Section
BSCSSE AN41
