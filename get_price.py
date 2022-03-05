# Adapted from a Java code in the "Refactoring" book by Martin Fowler.

# TODO: Replace temporary variable with extracted method/query

def get_discount(base_price):
  if base_price > 1000:
    return 0.95
  else:
    return 0.98

def get_price(quantity, item_price):
  base_price = quantity * item_price
  discount_factor = get_discount(base_price)

  return base_price * discount_factor
