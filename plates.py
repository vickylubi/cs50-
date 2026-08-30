#Program checks if a car plate is valid or not. 
#Get user input
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#Check if the plate is valid
def is_valid(s):
    #Check if the length is between 2 and 6 characters
    if len(s) < 2 or len(s) > 6:
        return False

    #Check if the first two characters are letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False
    
    #Check if there is no number in the middle of the plate and the first number used cannot be a ‘0’.”
    seen_digit = False
    for character in s:
        if character.isdigit():
            if not seen_digit and character == '0':
                return False
            seen_digit = True
        else:
            if seen_digit:
                return False
    
    #Check if there are no special characters in the plate
    if not s.isalnum():
        return False
    return True

main()