import random


def main():
        correct_score = 0
        level = get_level()
    #Game should have 10 rounds 
        for _ in range(10):
            x = generate_integer(level)
            y = generate_integer(level)
    #Each game has 3 attempts         
            for attempt in range(3):
                try:   
                    guess = int(input(f"{x} + {y} = "))
                    if guess == x + y:
                        correct_score += 1
                        break
                    else:
                        print("EEE")
                except ValueError:
                    print("EEE")   
            else: 
                print (f"{x} + {y} = {x+y}")
        print(f"Score: {correct_score}")

def get_level():
#Ask the user to input the game level, only 1,2 or 3
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
#Generate random int if the level is correct 
    if level not in [1,2,3]:
        raise ValueError
    else: 
        return random.randint(10**(level-1), 10**level - 1)


if __name__ == "__main__":
    main()