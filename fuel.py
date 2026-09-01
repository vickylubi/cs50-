def main():
    while True: 
        try: 
            fraction = input ("Fraction:")
            numbers = fraction.split("/")
            x = int(numbers[0])
            y = int(numbers[1])
            if x < 0 or y <= 0 or x > y:
                continue
            else:
                efficiency = x / y
                percentage = round(efficiency * 100)
            break
        except ValueError:
            pass    
    if percentage <= 1: 
        print ("E")
    elif percentage >= 99:
        print ("F")
    else:
        print(f"{percentage}%")
        
main()

