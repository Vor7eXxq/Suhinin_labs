def calculate_discount(price,discount_percent, is_member = False):
    calculated = price - (price/discount_percent)
    if is_member:
        calculated = calculated-(calculated/5)
    print(calculated)
calculate_discount(500,20,True)