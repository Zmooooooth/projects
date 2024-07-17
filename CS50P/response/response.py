import validator_collection

def main():
    userin = input("What's your Email address? ").strip().lower()
    validate_email(userin)

def validate_email(email_address):
    try:
        validator_collection.validators.email(email_address)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()
