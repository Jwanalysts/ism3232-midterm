MIN_BULK_BAGS = 20
HIGH_BULK_BAGS = 80

STANDARD_DISCOUNT = 0.09
HIGH_BULK_DISCOUNT = 0.14
PARTNER_BONUS_DISCOUNT = 0.04

SHIPPING_FEE = 35.00
FREE_SHIPPING_THRESHOLD = 250.00

PREPAYMENT_THRESHOLD = 1500.00

PALLET_BAG_THRESHOLD = 60
PALLET_TOTAL_THRESHOLD = 700.00


def calculate_bean_cost(bag_price: float, bags: int) -> float:
    """Calculate the bean cost before discounts."""
    return bag_price * bags


def get_bulk_discount(bags: int, partner: bool = False) -> float:
    """Return the bulk discount rate for a shipment."""
    if bags < MIN_BULK_BAGS:
        return 0.0

    if bags >= HIGH_BULK_BAGS:
        discount = HIGH_BULK_DISCOUNT
    else:
        discount = STANDARD_DISCOUNT

    if partner:
        discount += PARTNER_BONUS_DISCOUNT

    return discount


def calculate_shipment_total(
    bag_price: float, bags: int, partner: bool = False
) -> float:
    """Calculate the shipment total after discounts and shipping."""
    bean_cost = calculate_bean_cost(bag_price, bags)
    discount = get_bulk_discount(bags, partner)

    discounted_cost = bean_cost * (1 - discount)

    if discounted_cost < FREE_SHIPPING_THRESHOLD:
        return discounted_cost + SHIPPING_FEE

    return discounted_cost
