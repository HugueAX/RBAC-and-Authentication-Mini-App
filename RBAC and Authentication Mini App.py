# This code shows the Condfidentiality element of the CIA triad by allowing user 
# and admin roles to access their respective areas while restricting access by the 
# other roles through Role_Based Acess Control

# Simulated database
USERS = {
    "admin": {"role": "admin"},
    "user": {"role": "user"}
}

# Authentication
def login(username):
    if username in USERS:
        print(f"Logged in as {username}")
        return USERS[username]
    print("Access Denied: Username not found.")
    return None

# Authorization
def requiresRole(requiredRole, userSession):
    if not userSession:
        return False
    return userSession["role"] == requiredRole

# Endpoints
def adminProfile(userSession):
    if requiresRole("admin", userSession):
        print("Access to admin profile granted")
    else:
        print("Access to admin profile denied")

def userProfile(userSession):
    if requiresRole("user", userSession):
        print("Access to user profile granted")
    else:
        print("Access to user profile denied")

# Simulations

currentSession = login("admin")
adminProfile(currentSession)

currentSession = login("admin")
userProfile(currentSession)

currentSession = login("user")
adminProfile(currentSession)

currentSession = login("user")
userProfile(currentSession)