# ISM3232 Midterm - Commands

## 1. Setting Up My Project

These are the commands I used to create my project, set up Python, and connect everything to GitHub.

```bash
cd ~
mkdir ism3232-midterm
cd ism3232-midterm
pwd
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
pip freeze > requirements.txt
mkdir tests
touch business_rules.py main.py tests/__init__.py tests/test_business_rules.py
printf '.venv/\n__pycache__/\n' > .gitignore
git init
git branch -M main
git add .
git commit -m "Initialize midterm project structure and dependencies"
git remote add origin https://github.com/jwanalysts/ism3232-midterm.git
git push -u origin main
code .
```

I started by making my project folder. After that, I set up my virtual environment, installed the packages I needed, created my Python files, and pushed the project to GitHub.

## 2. Checking My Python Environment

Command:

```bash
which python3
```

Output:

```text
/home/jackson/ism3232-midterm/.venv/bin/python3
```

This shows that I'm using Python from my virtual environment.

## 3. Checking My Project Files

Command:

```bash
tree -L 2
```

Output:

```text
.
├── __pycache__
│   └── business_rules.cpython-314.pyc
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

4 directories, 7 files
```

This shows how I organized my project. I kept my main program, business functions, and tests separate. My `.gitignore` keeps the virtual environment and Python cache files out of Git.

## 4. Finding My Functions

Command:

```bash
rg 'def '
```

Output:

```text
business_rules.py
17:def calculate_bean_cost(bag_price: float, bags: int) -> float:
22:def get_bulk_discount(bags: int, partner: bool = False) -> float:
38:def calculate_shipment_total(
53:def requires_prepayment(total: float) -> bool:
58:def needs_pallet(bags: int, total: float) -> bool:
63:def total_shipped(shipments: list) -> float:
78:def largest_shipment(shipments: list) -> str:
97:def format_shipment_line(

tests/test_business_rules.py
13:def test_bean_cost_ten_bags():
17:def test_bean_cost_zero_bags():
21:def test_bean_cost_decimal_price():
25:def test_discount_below_20_bags():
29:def test_discount_at_20_bags():
33:def test_discount_at_79_bags():
37:def test_discount_at_80_bags():
41:def test_partner_below_20_bags():
45:def test_partner_at_20_bags():
49:def test_partner_at_80_bags():
53:def test_shipment_total_with_shipping():
57:def test_shipment_total_with_bulk_discount():
61:def test_shipment_total_with_partner_discount():
65:def test_shipping_fee_below_250():
69:def test_no_shipping_fee_at_250():
73:def test_prepayment_below_threshold():
77:def test_prepayment_at_threshold():
81:def test_prepayment_above_threshold():
85:def test_pallet_at_60_bags():
89:def test_pallet_at_61_bags():
93:def test_pallet_at_700_total():
97:def test_pallet_above_700_total():
101:def test_total_shipped_multiple_shipments():
109:def test_total_shipped_empty_list():
113:def test_largest_shipment():
121:def test_largest_shipment_tie_returns_first():
129:def test_largest_shipment_empty_list():
133:def test_format_shipment_line():
138:def test_format_shipment_line_with_requirements():
```

I found 8 functions in `business_rules.py` and 29 test functions. That gives me 37 functions altogether.

## 5. Checking Print Statements

Command:

```bash
rg -l 'print'
```

Output:

```text
main.py
```

Only `main.py` showed up, which is what I wanted. My business functions return values, and my main file handles printing the report.

## 6. Checking My Git Commits

Command:

```bash
git log --oneline
```

Output:

```text
36c75bd (HEAD -> main, origin/main) Add 29 automated tests for business rules
3eceed1 Add shipment report and summary calculations
c053c4b Add shipment aggregation and report formatting functions
5a85162 Add prepayment and pallet requirement functions
ca87e98 Add bean cost, bulk discount, and shipment total functions
5743c50 Initialize midterm project structure and dependencies
```

I had 6 commits when I ran this command. Each commit shows a different part of the project I worked on.