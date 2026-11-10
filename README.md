# Airline Reservation Simulator (Python)

A beginner-friendly, **French-language command-line application** that simulates an airline booking workflow using Python.

> **Disclaimer:** This is an unofficial educational project. It is **not affiliated with, endorsed by, or connected to Air Canada**. It does not book real flights. All flight information, fare tables, employee salaries, and customer records are simulated.

## Features

### Customer mode
- Selects a destination from a list of 30 countries.
- Collects basic traveler details and calculates age-based ticket prices.
- Adds optional meals and beverages for each traveler.
- Generates a simulated flight number, seat number, departure time, and arrival time.
- Prints a final booking summary with the total cost.

### Employee demo mode
- Demonstrates a simple password-protected menu (for learning purposes only).
- Displays sample salaries based on role and years of service.
- Displays a hardcoded list of sample customers.

## Technologies and concepts

- **Python 3** (standard library only)
- Dictionaries and lists
- `if` / `elif` / `else` statements
- `for` loops
- User input and calculations
- `random` module

## Run the project

1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder and run:

   ```bash
   python main.py
   ```

   On some systems, use `python3 main.py` instead.
4. Follow the French prompts in the terminal.

**Dependencies:** No external packages are required.

## Limitations

This is an early Python learning project, not a production reservation system. It uses predefined prices and randomly generated flight details rather than live airline data. It does not save bookings to a database or connect to a real airline API. The employee password is hardcoded for demonstration, so it is **not secure authentication**. Some invalid inputs may cause errors.

## Project files

```text
Airline-Reservation-Simulator/
├── main.py      # Original Python application
├── README.md    # Project documentation
└── .gitignore   # Ignore Python cache files
```
