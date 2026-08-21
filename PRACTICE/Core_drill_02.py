# prices_in_inr = [150, 450, 1200, 80, 2300, 500, 90]
# final_price=[]
# for price in prices_in_inr:
#     if price>=500:
#         gst_price = price*1.18
#         final_price.append(gst_price)
    
# print(final_price)

#################################################################################

# cart_prices = [120, 850, 40, 1200, 300, 2500]
# final_price=[]
# for price in cart_prices:
#     if price>=500:
#         discount_price = price * 0.80
#         final_price.append(discount_price)
# print(final_price)
# final_price = [price*0.80 for price in cart_prices if price >= 500]
# print(final_price)

#################################################################################

# raw_emails = ["  aman@gmail.com ", "RAHUL@YAHOO.COM", "  invalid_user  ", "PRIYA@GMAIL.COM "]
# final_mail = []
# for mail in raw_emails:
#     if '@' in mail:
#         clean_mail=mail.strip().lower()
#         final_mail.append(clean_mail)
# print(final_mail)

# final_mail = [mail.strip().lower() for mail in raw_emails if '@' in mail]
# print(final_mail)

#################################################################################

# raw_txns = [
#     "TXN_01:CREDIT:1500:SUCCESS",
#     "TXN_02:DEBIT:400:SUCCESS",
#     "TXN_03:CREDIT:300:SUCCESS",
#     "TXN_04:CREDIT:4500:FAILED",
#     "TXN_05:CREDIT:3200:SUCCESS",
#     "INVALID_ENTRY_LOG",
#     "TXN_06:CREDIT:8000:SUCCESS"
# ]

# clean_txns = []

# for txn in raw_txns:
#     # 1. Check: Kya isme CREDIT aur SUCCESS dono hain?
#     if ":CREDIT:" in txn and txn.endswith(":SUCCESS"):
#         # print(txn)
#         # 2. String ko tod kar amount nikaalo
#         parts = txn.split(":")
#         amount = int(parts[2])
#         # print(amount)
        
#         # 3. Filter: Kya amount 1000 ya usse bada hai?
#         if amount >= 1000:
#             # print(amount)
#             txn = amount * 0.98
#             clean_txns.append(txn)
#             # 4. 2% fee kaat kar list mein daalo (amount * 0.98)
#             # Yahan append ka logic likh...

# print(clean_txns)

#################################################################################

# marks = {
#     "maths": 85,
#     "english": 72,
#     "science": 90
# }
# # print(marks["science"])

# total = 0
# for sub, result in marks.items():
#     total += result
# print(total)
# comp_marks = marks.get("computer","Subject not found")
# print(comp_marks)

#################################################################################

# daily_expenses = {
#     "tea": 20,
#     "lunch": 120,
#     "petrol": 100,
#     "snacks": 40
# }
# print(f"Petrol Expence : {daily_expenses["petrol"]}\n")

# dinner_exp=daily_expenses.get("Dinner","No Dinner Record\n")
# print("Dinner Expence : ",dinner_exp)

# daily_expenses["medicine"]=150
# print("Medical Expence Add : ",daily_expenses["medicine"])
# print("")

# total=0
# for exp,price in daily_expenses.items():
#     if price>=50:
#         total += price
# print(total)

#################################################################################

phonebook = {
    "Aman": "9898011111",
    "Rahul": "9123422222"
}

phonebook["Rohit"] = "9999933333"
print(phonebook["Rohit"])
print(phonebook)