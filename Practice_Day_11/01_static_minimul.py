class order:
    @staticmethod
    def is_valid(qty):
        return qty > 0 and qty % 25 == 0

if __name__ == "__main__":
    print("50 shares valid or not ?", order.is_valid(50))
    print("50 shares valid lot hai? ->", order.is_valid(30))