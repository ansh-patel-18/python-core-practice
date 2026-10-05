def calculate_share_price(total_amount_raw, qty):
    amount = float(total_amount_raw)
    per_share = amount / qty
    return per_share

test_inputs = [("10000", 0),
               ("paisa", 10),
               ("5000", 25)
            ]

for raw_amt, quantity in test_inputs:
    print(f"\nTrying: amount='{raw_amt}', qty={quantity}")


    try:
        result = calculate_share_price(raw_amt, quantity)
        print(f"SUCCESS: 1 share ka price Rs.: {result}")

    except ZeroDivisionError:
        print("[HANDLED]: Quantity 0 nahi ho sakti, division impossible hai.")
    
    except ValueError:
        print(
        f"[HANDLED]: '{raw_amt}' number nahi hai, float mein convert nahi ho"
        " sakta."
    )
    print("\nprogram is still alive.")