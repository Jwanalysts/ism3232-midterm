# ISM3232 Midterm: Copper Kettle Coffee Roasters

**Name:** Jackson Williams  
**Version:** ZETA  
**Date:** October 24, 2026

## What This Program Does

This program calculates coffee bean shipment costs for different customers. It figures out discounts, shipping costs, and whether an order needs prepayment or a pallet. It also prints a report showing each customer's shipment and a summary of all the orders.

## Business Rules

1. The cost of the coffee beans is calculated by multiplying the price per bag by the number of bags.
2. Customers receive bulk discounts depending on how many bags they order. Partners can receive an additional discount.
3. Shipping costs are added to smaller orders, while orders that meet the free-shipping requirement do not pay the shipping fee.
4. Orders totaling $1,500 or more require prepayment.
5. Orders need a pallet if they have more than 60 bags or their total is over $700.
6. The program calculates the total value of all shipments and identifies the customer with the largest shipment.

## How to Run

Open the project folder in your terminal and run these commands:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 main.py
```

This runs the program and displays the shipment report.

## How to Test

Run these commands in the terminal:

```bash
ruff check .
ruff format --check .
pytest -v
```

I wrote 29 automated tests to check the business functions, including different order amounts and boundary values. All 29 tests passed during testing.

## Files in This Repository

- `business_rules.py` - Contains the calculations and business rules.
- `main.py` - Runs the program and prints the shipment report.
- `tests/test_business_rules.py` - Contains the 29 automated tests.
- `tests/__init__.py` - Marks the tests folder as a Python package.
- `requirements.txt` - Lists the packages needed for the project.
- `.gitignore` - Keeps unnecessary files out of Git.
- `commands.md` - Documents the terminal commands and their outputs.
- `README.md` - Explains the project and how to run it.

## AI Use Statement

I did not use AI on this exam