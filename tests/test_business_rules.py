from business_rules import (
    calculate_bean_cost,
    calculate_shipment_total,
    format_shipment_line,
    get_bulk_discount,
    largest_shipment,
    needs_pallet,
    requires_prepayment,
    total_shipped,
)


def test_bean_cost_ten_bags():
    assert calculate_bean_cost(14.00, 10) == 140.00


def test_bean_cost_zero_bags():
    assert calculate_bean_cost(14.00, 0) == 0.00


def test_bean_cost_decimal_price():
    assert calculate_bean_cost(12.50, 3) == 37.50


def test_discount_below_20_bags():
    assert get_bulk_discount(19) == 0.0


def test_discount_at_20_bags():
    assert get_bulk_discount(20) == 0.09


def test_discount_at_79_bags():
    assert get_bulk_discount(79) == 0.09


def test_discount_at_80_bags():
    assert get_bulk_discount(80) == 0.14


def test_partner_below_20_bags():
    assert get_bulk_discount(19, True) == 0.0


def test_partner_at_20_bags():
    assert round(get_bulk_discount(20, True), 2) == 0.13


def test_partner_at_80_bags():
    assert round(get_bulk_discount(80, True), 2) == 0.18


def test_shipment_total_with_shipping():
    assert round(calculate_shipment_total(14.00, 10), 2) == 175.00


def test_shipment_total_with_bulk_discount():
    assert round(calculate_shipment_total(13.00, 40), 2) == 473.20


def test_shipment_total_with_partner_discount():
    assert round(calculate_shipment_total(12.00, 50, True), 2) == 522.00


def test_shipping_fee_below_250():
    assert round(calculate_shipment_total(249.99, 1), 2) == 284.99


def test_no_shipping_fee_at_250():
    assert round(calculate_shipment_total(250.00, 1), 2) == 250.00


def test_prepayment_below_threshold():
    assert requires_prepayment(1499.99) is False


def test_prepayment_at_threshold():
    assert requires_prepayment(1500.00) is True


def test_prepayment_above_threshold():
    assert requires_prepayment(2000.00) is True


def test_pallet_at_60_bags():
    assert needs_pallet(60, 800.00) is False


def test_pallet_at_61_bags():
    assert needs_pallet(61, 800.00) is True


def test_pallet_at_700_total():
    assert needs_pallet(61, 700.00) is False


def test_pallet_above_700_total():
    assert needs_pallet(61, 700.01) is True


def test_total_shipped_multiple_shipments():
    shipments = [
        {"buyer": "A", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "B", "bag_price": 13.00, "bags": 40, "partner": False},
    ]
    assert round(total_shipped(shipments), 2) == 648.20


def test_total_shipped_empty_list():
    assert total_shipped([]) == 0.0


def test_largest_shipment():
    shipments = [
        {"buyer": "Small", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Large", "bag_price": 11.00, "bags": 200, "partner": False},
    ]
    assert largest_shipment(shipments) == "Large"


def test_largest_shipment_tie_returns_first():
    shipments = [
        {"buyer": "First", "bag_price": 14.00, "bags": 10, "partner": False},
        {"buyer": "Second", "bag_price": 14.00, "bags": 10, "partner": False},
    ]
    assert largest_shipment(shipments) == "First"


def test_largest_shipment_empty_list():
    assert largest_shipment([]) == ""


def test_format_shipment_line():
    result = format_shipment_line("Uptown Bakery", 175.00, False, False)
    assert result == "Uptown Bakery: $175.00 | prepayment: no | pallet: no"


def test_format_shipment_line_with_requirements():
    result = format_shipment_line("Zenith Grocers", 1892.00, True, True)
    assert result == "Zenith Grocers: $1892.00 | prepayment: yes | pallet: yes"
