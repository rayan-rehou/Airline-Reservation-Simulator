# Airline Reservation System (Python)

A French-language command-line application in Python that runs an airline booking workflow, with a customer menu and an employee menu.

> **In progress:** a web version built with Flask and HTML for booking flights from a browser (its files will be added to this repo), input checks for every field, and a SQLite database to save bookings.

**Disclaimer:** This is an unofficial personal project. It is not affiliated with, endorsed by, or connected to Air Canada. It does not book real flights. All flight information, fare tables, employee salaries, and customer records are simulated.

## Features

### Customer mode
- Selects a destination from a list of 30 countries.
- Collects traveller details and calculates age-based ticket prices.
- Adds optional meals and beverages for each traveller.
- Generates a flight number, seat number, departure time, and arrival time.
- Prints a final booking receipt with the total cost.

### Employee mode
- Password-protected menu (demo password, not real authentication).
- Shows salaries based on role and years of service.
- Shows a list of sample customers.

## Technologies and concepts
- Python 3 (standard library only)
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

## Current limitations and next steps
- Prices are predefined and flight details are generated randomly, not taken from live airline data.
- Bookings aren't saved yet. A SQLite database to store them is in progress.
- Some invalid inputs (for example letters in the age field) can still cause errors. Input validation is the next step.

## Project files

```
Airline-Reservation-Simulator/
├── main.py       # Python application
├── README.md     # Project documentation
└── .gitignore    # Ignore Python cache files
```
