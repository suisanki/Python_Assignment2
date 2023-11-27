import random

def password_generator():
    filepass = input("Please enter the absolute pass to the file: ")
    username = input("Please enter your Username: ")
    password = ""
    
    #Define error when there is no username input
    if username == "":
        raise ValueError("Username is empty. Try again.\n")
        
    for i in range(14):
        random.seed()
        """Number, alphabet and special character (but space) of basic latin
        falls between 33 and 126 in decimal Unicode. Select one randomly and 
        add to password string. Repeat it 14 times."""
        password = password+chr(random.randint(33,126))
    
    with open(filepass, "a") as txt:
        txt.write(f'Username: {username} \nPassword: {password}\n\n')

        print("Password generated.\nPassword and username saved in the file.")
    
if __name__ == "__main__":
    while True:
        try: 
            password_generator()
            break
        
        except ValueError as msg:
            print(msg)
        #Tells when the absolute pass is not right.
        except FileNotFoundError:
            print("Incorrect pass. Try again.\n")
