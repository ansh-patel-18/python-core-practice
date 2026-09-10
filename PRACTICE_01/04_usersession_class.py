class UserSession:

    def __init__(self, username: str, token: str):
        self.username = username
        self.token = token
        self.is_active = True


    def logout(self) -> None:
        self.is_active = False
        print(f"[AUTH] User '{self.username}' logged out successfully.")


    def check_access(self) -> bool:
        if self.is_active:
            print(f"[ACCESS GRANTED] Token valid for {self.username}")
            return True
        else:
            print(f"[ACCESS DENIED] Session expired for {self.username}")
            return False


# --- Execution Block ---
if __name__ == "__main__":
    # Session 1 create kiya
    session1 = UserSession(username="ansh_dev", token="xyz_token_99")
    
    # Check access (Active state)
    session1.check_access()

    # Logout trigger kiya
    session1.logout()

    # Dobara access check kiya (Inactive state)
    session1.check_access()
