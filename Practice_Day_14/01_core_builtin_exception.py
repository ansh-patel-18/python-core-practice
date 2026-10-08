# ==============================================================================
# 6 CORE BUILT-IN EXCEPTIONS: ISOLATED WORKFLOWS
# ==============================================================================


def demo_value_error():
  """Case 1: ValueError - Type string hai, lekin integer conversion impossible hai."""
  user_input = "one_hundred"
  return int(user_input)


def demo_type_error():
  """Case 2: TypeError - Incompatible data types par math operation."""
  item_price = 450
  currency_symbol = "INR "
  return currency_symbol + item_price  # Python string + int allow nahi karta


def demo_key_error():
  """Case 3: KeyError - Payload structure mein expected key missing hai."""
  client_payload = {"account_id": "ACC_101", "broker": "AngelOne"}
  return client_payload["auth_token"]  # 'auth_token' exist hi nahi karta


def demo_index_error():
  """Case 4: IndexError - Array length se zyada ka index access."""
  active_orders = ["ORD_01", "ORD_02"]
  return active_orders[4]  # Sirf 0 aur 1 index valid hain


def demo_attribute_error():
  """Case 5: AttributeError - Object ke paas mangi hui property/method nahi hai."""
  user_balance = None  # DB query empty aane par variable None reh gaya
  return (
      user_balance.strip()
  )  # NoneType object ke paas .strip() method nahi hota


def demo_zero_division_error():
  """Case 6: ZeroDivisionError - Zero se mathematical division."""
  total_pnl = 12500
  executed_trades = 0
  return total_pnl / executed_trades  # 0 se divide karne par math fail hota hai


# ==============================================================================
# TEST RUNNER & EXCEPTION CATCHING HARNESS
# ==============================================================================

if __name__ == "__main__":
  scenarios = [
      ("ValueError Test", demo_value_error, ValueError),
      ("TypeError Test", demo_type_error, TypeError),
      ("KeyError Test", demo_key_error, KeyError),
      ("IndexError Test", demo_index_error, IndexError),
      ("AttributeError Test", demo_attribute_error, AttributeError),
      (
          "ZeroDivisionError Test",
          demo_zero_division_error,
          ZeroDivisionError,
      ),
  ]

for test_name, func, expected_error in scenarios:
    print(f"\n[RUNNING]: {test_name}")
    try:
      func()
      print("Status: FAILED (Error aani chahiye thi par nahi aayi)")
    except expected_error as err:
      print(f"Status: SUCCESS (Caught {expected_error.__name__})")
      print(f"Internal Reason: {err}")