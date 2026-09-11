class app:
    def __init__(self, user_id:str, user_name:str):
        self.user_id = user_id
        self.username = user_name
        self.is_active = True

    def log_out(self):
        self.is_active = False
        print(f"\nUser ID [{self.user_id}] logged out successfully")

    def session_check(self):
        if self.is_active:
            print(f"\n[Access Granted] session active for User Id : {self.user_id}")
        else:
            print(f"\n[Access Denied] session expired for User Id : {self.user_id}")

if __name__ == "__main__":
    u1 = app(user_id = "ansh_patel_155", user_name = "Ansh Patel")
    
    u1.log_out()
    u1.session_check()