# def apply_discount(price : float, coupen : str):
#     if coupen == "FLAT50":    
#         return price - 50
#     elif coupen=="SAVE10":
#         return price * 0.90
#     else:
#         return price

# enter_price = float(input("Enter item price : "))
# enter_coupen = input("Enter coupen code : ").upper()

# a = apply_discount(enter_price, enter_coupen)
# print(f"\nYour final bill {a}")

###################################################################################################

# def can_access_dashboard(is_authenticated : bool, role : str = 'guest'):
#     if is_authenticated == True and role == "admin":
#         return True
#     elif is_authenticated == True and role == 'manager':
#         return True
#     elif is_authenticated == False and role == "":
#         return False
#     else:
#         return False

# authenicate = bool(input("You are authenicate : "))
# roles = input("What is your role : ")

# verify = can_access_dashboard(authenicate, roles)
# print(verify)

# print(can_access_dashboard(True, "admin"))    
# print(can_access_dashboard(True, "manager"))  
# print(can_access_dashboard(True))             
# print(can_access_dashboard(False, "admin"))   

###################################################################################################

# def get_discounted_bill(price:float, is_member:bool = False):
#     if is_member == True:
#         return price*0.90
#     else:
#         return price

# print(get_discounted_bill(1000.0, True))   
# print(get_discounted_bill(1000.0))         

###################################################################################################

# def build_user_payload(username:str, role:str='guest'):
#     allowed_role = {"admin","user","guest"}

#     if role not in allowed_role:
#         role = "guest"

#     if role =="admin":
#         access = "FULL"
#     else:
#         access = "Risricted"
    
#     return {"usename":username,
#             "Role":role,
#             "Access":access
#     }
# user = input("Enter username : ")
# role = input("Enter your role : ").lower()
# if role == "":
#     role = "guest"
    
# total = build_user_payload(user, role)
# print("")
# print(total)

###################################################################################################

# def get_subscription_tier(plan: str, is_verified: bool = False):
#     if plan=="pro":
#         storage_gb = 50
#         final_plan = "pro"
#     elif plan=="enterprice":
#         storage_gb = 500
#         final_plan = "enterprise"    
#     else:
#         storage_gb = 5
#         final_plan = "free"
    
#     if is_verified==True:
#             status = "Active"
#     else:
#          status = "PENDING_VERIFICATION"    

#     return{
#         "plan":final_plan,
#         "Storage_gb":storage_gb,
#         "status":status
#     }

# # print(get_subscription_tier("pro",True))

# user_plan = input("Enter your plan : ")
# user_verification = bool(input("Your plan is varify (True or False) : "))

# final_data = get_subscription_tier(user_plan, user_verification)
# print(final_data)

###################################################################################################

