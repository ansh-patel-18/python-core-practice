# # User records: (user_id, role, is_active)
# users = [
#     (101, "admin", True),
#     (102, "guest", False),
#     (103, "admin", True),
#     (104, "guest", True),
#     (105, "admin", False)
# ]

# allowed_roles = {"admin"}
# active_admins = set()

# for userid, role, is_active in users:
#     if is_active == True and role in allowed_roles:
#         active_admins.add(userid)
# print(active_admins)

########################################################################################

# Order data: (order_id, city, is_paid)
# orders = [
#     (1001, "Ahmedabad", True),
#     (1002, "Mumbai", True),
#     (1003, "Surat", False),
#     (1004, "Surat", True),
#     (1005, "Delhi", False)
# ]

# allowed_cities = {"Ahmedabad", "Surat"}
# shipped_orders = set()

# for order_id, city, paid in orders:
#     if paid == True and city in allowed_cities:
#         shipped_orders.add(order_id)
# print(shipped_orders)


########################################################################################


# Streaming session logs: (session_id, user_id, device, is_active)
stream_requests = [
    (501, "karan_99", "tv", True),
    (502, "rohit_dev", "laptop", True),
    (503, "priya_ai", "mobile", False),
    (504, "aman_py", "mobile", True),
    (505, "simran_qa", "tv", True)
]

allowed_devices = {"tv", "mobile"}
granted_users = set()

for session_id, user_id, device, is_active in stream_requests:
    if is_active == True and device in allowed_devices:
        granted_users.add(user_id)
print(granted_users)


########################################################################################


# # Applicants: (candidate_id, name, skill, experience_years)
applicants = [
    (1, "Rahul", "Python", 3),
    (2, "Sneha", "Java", 4),
    (3, "Amit", "FastAPI", 1),
    (4, "Pooja", "FastAPI", 2),
    (5, "Vikas", "Python", 1)
]

target_skills = {"Python", "FastAPI"}
shortlisted_ids = set()

for candidate_id, name, skill, experience_years in applicants:
    if experience_years >= 2 and skill in target_skills:
        shortlisted_ids.add(candidate_id)
print(shortlisted_ids)