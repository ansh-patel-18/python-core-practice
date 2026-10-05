def process_order(payload: dict):
    if "symbol" not in payload or "qty" not in payload:
        raise KeyError("Payload invalid hai: 'symbol' and 'qty' keys missing hai.")

    symbol = payload["symbol"]
    qty = payload["qty"]

    if not isinstance(qty, int):
        raise TypeError(
            f"'qty' ka type integer hona chahiye, mila {type(qty).__name__}."
        )

    if qty<=0:
        raise ValueError(f"Quantity positive honi chahiye, invalid value mili: {qty}")

    return f"SUCCESS : {qty} shares of {symbol} processed."

if __name__ == "__main__":
    test_cases = [{"symbol":"INFY"},
                  {"symbol":"TCS","qty":"ten"},
                  {"symbol":"RELIANCE", "qty":-50},
                  {"symbol":"TATAMOTORS", "qty":10}
                ]

    for index, data in enumerate(test_cases, 1):
        print(f"\n--- RUNNING TEST CASE {index} ---")
        
        try:
            result = process_order(data)
            print(result)
        except KeyError as err:
            # HTTP 422 / Bad payload
            print(f"[REJECTED - MISSING FIELD]: {err}")

        except TypeError as err:
            # HTTP 400 / Wrong format
            print(f"[REJECTED - WRONG DATA TYPE]: {err}")

        except ValueError as err:
            # HTTP 400 / Invalid parameter value
            print(f"[REJECTED - INVALID VALUE]: {err}")