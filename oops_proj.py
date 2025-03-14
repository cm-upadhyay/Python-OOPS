class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.loggedin = False
        self.menu()


    def menu(self):
        user_input = input("""Welcome to Chatbook !! How would you like to proceed?"
                            1. Press 1 to Signup
                            2. Press 2 to Signin
                            3. Press 3 to Write a Post
                            4. Press 4 to Message a Friend
                            5. Press any other key to Exit
                            Enter your Input: """)
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
    
    def signup(self):
        email = input("Enter your email here -> ")
        pwd = input("Enter your password here -> ")
        self.username = email
        self.password = pwd
        print("you have signed in successfully")
        print("\n")
        self.menu()

    def signin(self):
        if self.username == "" and self.password == "":
            print ("Please signup first by pressing 1")
        else:
            uname = input("Enter your email/username here -> ")
            pwd = input("Enter your password here -> ")
            if self.username == uname and self.password == pwd:
                print("you have signed up successfully")
                self.loggedin = True
            else:
                "Please input correct credentials"
        print("\n")
        self.menu()

obj = chatbook()