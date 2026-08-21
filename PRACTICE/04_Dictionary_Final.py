server_health = {
    "db_server": "active",
    "auth_service": "down",
    "payment_gateway": "active"
}
print(server_health["db_server"])
print("")

analistic = server_health.get("analistics_service","Service not configured")
print("Analistics Service : ",analistic)
print("")

server_health["email_service"]="active"
print(server_health)
print("")

server_health["auth_service"]="active"
print(server_health)

final_server=0

for data, status in server_health.items():
    if status == "active":
        final_server+=1
print(final_server)