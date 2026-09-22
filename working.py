import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #Get starting and ending times 
    parts = s.split(" to ")
    if len(parts) != 2:
        raise ValueError("Invalid format")
    start_text, end_text = parts
    
    # Extract 12-hour time components: (hour, optional ":MM", AM/PM)
    def parse_time(value):
        match = re.search(r"^(\d{1,2})(?::(\d{2}))? (AM|PM)$", value)
        #Check if the input matched the format 
        if not match:
            raise ValueError("Invalid format")
        
        #Get matched input saved into variables 
        hour = int(match.group(1))
        minutes = int(match.group(2) or 0)
        ampm = match.group(3)
        
        #Check if matches are valid
        if not (1 <= hour <= 12):
            raise ValueError("Invalid hour")
        if not (0 <= minutes <= 59):
            raise ValueError("Invalid minutes")
            
        #Converting hours based on AM/PM 
        if ampm == "AM":
            if hour == 12:
                hour = 0
        else:
            if hour != 12:
                hour += 12    
        
        return hour, minutes
    
    start_hour, start_minutes = parse_time(start_text)
    end_hour, end_minutes = parse_time(end_text)
    return f"{start_hour:02d}:{start_minutes:02d} to {end_hour:02d}:{end_minutes:02d}"

if __name__ == "__main__":
    main()