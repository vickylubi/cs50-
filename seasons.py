import sys 
from datetime import date
import inflect


def main():
#Get input, validate it's in YYYY-MM-DD format, sys.exit if not.
    birthdate_input = input("When were you born? Write in YYYY-MM-DD: ")

    try: 
        birth_date = date.fromisoformat(birthdate_input)
    except ValueError:
        sys.exit("Invalid date")
        
    minutes = calculate_lifetime(birth_date)
    print(convert_to_words(minutes))
    
#Calculate the difference between today and that date, in minutes.
def calculate_lifetime(birth_date):
    lifetime = date.today() - birth_date
    return lifetime.days*24*60
   
#Convert that number into English words
def convert_to_words(minutes):  
    p = inflect.engine()
    minutes_in_words = p.number_to_words(minutes, andword="")
    return f"{minutes_in_words.replace(',','').capitalize()} minutes"


if __name__ == "__main__":
    main()
    
