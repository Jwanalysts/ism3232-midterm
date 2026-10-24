# Copper Kettle Coffee Roasters

ISM3232 Midterm Project

This program calculates coffee bean shipment costs for different customers. It includes bulk discounts, shipping fees, prepayment requirements, and pallet requirements.

The program also prints a shipment report showing each customer's total and a summary of all shipments.

## Files

- business_rules.py - Calculates prices, discounts, and shipment requirements.
- main.py - Runs the program and prints the report.
- tests/test_business_rules.py - Tests the business functions.
- commands.md - Shows the commands I used to build and check the project.
- requirements.txt - Lists the Python packages used.

## How to Run

Activate the virtual environment:

    source .venv/bin/activate

Run the program:

    python3 main.py

Run the tests:

    pytest -v

Check the code:

    ruff check .
    ruff format --check .

## Testing

I created 29 tests to check my business functions, including different prices, discounts, and boundary values.

All 29 tests passed.