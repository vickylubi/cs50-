import inflect
p = inflect.engine()

def main():
    names = []

    while True:
        try: 
            name = input("Name ")
            names.append(name)
        except EOFError:
            break
    print(f"Adieu, adieu, to {p.join(names)}")
    
if __name__ == "__main__":
    main()