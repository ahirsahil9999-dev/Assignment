# Write a Python script that demonstrates the lifetime of a local variable
# inside a function versus a global variable by printing their values before
# , during, and after a function call. Use variable names similar to
# 'user_status' and 'app_status', inspired by WhatsApp online/offline status.

app_status = "Offline"

def update_status():
    user_status = "Online"

    print("Inside function:")
    print("User status:", user_status)
    print("App status:", app_status)


print("Before function call:")
print("App status:", app_status)

update_status()

print("After function call:")
print("App status:", app_status)