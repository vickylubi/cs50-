from validator_collection import validators, errors

def main():
    email = input("Email: ")
    try: 
        validators.email(email)
        print ("Valid email")
    except errors.InvalidEmailError:
        print ("Invalid email")
        

if __name__=="__main__":
    main()