#
# LEVEL-1

# User profile data from DB
user_data = (501, "karan_dev", "karan@gmail.com", "active")
uid, uname, uemail, ustatus = user_data
print(f"\nUser: {uname} (ID: {uid}) - Status: {ustatus}")

print(user_data.count("active"))



# Current user roles
roles = {"user", "editor"}
roles.add("admin")
roles.discard("admin")
print(roles)

#LEVEL 2
# 1. API Role Matching
user_permissions = {"read", "write"}
required_permissions = {"read", "write", "delete"}

missing_permission = required_permissions - user_permissions
print(f"Access Denied! Missing : {missing_permission}")

# 2. Raw IP Traffic Logs
raw_ips = ["192.168.1.1", "192.168.1.2", "192.168.1.1", "10.0.0.1", "192.168.1.2", "172.16.0.5"]
raw_ips = {"192.168.1.1", "192.168.1.2", "192.168.1.1", "10.0.0.1", "192.168.1.2", "172.16.0.5"}
unique_ips = set(raw_ips)
print(len(unique_ips))
# print(len(raw_ips))

