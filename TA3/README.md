# TA3: Intelligent Tutoring System Using Case-Based Reasoning

This repository contains the required output for TA3. The project demonstrates an intelligent tutoring system that uses case-based reasoning to support students with recurring learning errors.

## Files
- `TA3_Basister-Calingasan.py` - Python implementation of the tutoring system
- `TA3_Basister-Calingasan.pdf` - task output document
- `README.md` - project overview

## Description
The system analyzes a new learning problem and compares it with previous successful cases stored in a case base. It retrieves the most similar case, adapts the learning strategy to the current student, revises the intervention after a follow-up quiz, and retains the new case for future use.

The workflow includes:
- problem validation
- similarity-based retrieval
- adaptation of feedback and practice plan
- revision based on quiz performance
- retention of solved cases

## Features
- Case-based reasoning workflow
- Weighted similarity scoring
- Student error and topic matching
- Personalized feedback and practice recommendations
- Follow-up evaluation and case retention
- Interactive mode for custom student profiles

## How to Run
1. Open a terminal in the project folder.
2. Run the default demonstration:
   ```bash
   python TA3_Basister-Calingasan.py
