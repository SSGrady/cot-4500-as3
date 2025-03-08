# cot-4500-as3
This repository provides two numerical solutions to ordinary differential equations using Euler and Runge-Kutta methods, as per directions of assignment 3.

## System Requirements
- Python 3.6 or higher
- NumPy (install using `pip install numpy`)

## Setup
### 1. Clone with SSH and Run Python
```bash
git clone git@github.com:SSGrady/cot-4500-as3.git
cd cot-4500-as3/
python3 src/main/assignment_3.py
```

### 2. Run Tests
```bash
python3 -m unittest src/test/test_assignment_3.py
```

## Usage
The `assignment_3.py` script calculates and prints the approximate solutions for the ordinary differential equations using both Euler's and Runge Kutta method.

## More Info
- My implementation avoids the use of `scipy` as per assigment directions
- The `test_assignment_3.py` file contains unit tests to verify the correctness of the numerical methods